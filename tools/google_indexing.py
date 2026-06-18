#!/usr/bin/env python3
"""Google Indexing API 로 URL 색인 통보 (구글은 IndexNow 미참여).

구글에 즉시 색인 신호를 보내는 가장 빠른 공식 경로입니다.
sitemap ping(2023년 폐지)이나 단순 제출보다 빠르며, 변경/삭제를 명시할 수 있습니다.

== 사전 준비 (1회) ==
1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
2) 서비스 계정 생성 → JSON 키 다운로드
3) Google Search Console 에서 해당 사이트(속성)에 그 서비스 계정 이메일을
   "소유자(Owner)" 권한으로 추가
4) 라이브러리 설치:
     pip install google-auth requests

== 사용법 ==
  export GOOGLE_APPLICATION_CREDENTIALS=/경로/service-account.json
  python tools/google_indexing.py                # sitemap.xml 전체 통보
  python tools/google_indexing.py /magazine/새글/ # 특정 URL만
  python tools/google_indexing.py --delete /지운글/ # 삭제 통보(URL_DELETED)

참고: Indexing API 는 일 200 URL 쿼터(기본)와, 공식적으로는 JobPosting/
BroadcastEvent 대상이라는 안내가 있습니다. 일반 페이지에도 동작하지만
대량 색인은 sitemap.xml 제출을 기본으로 두고, 신규 글 위주로 사용하세요.
"""
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    tree = ET.parse(path)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text.strip() for el in tree.findall(".//s:loc", ns)]


def normalize(args):
    out = []
    for a in args:
        if a.startswith("http"):
            out.append(a)
        else:
            out.append(BASE + "/" + a.lstrip("/"))
    return out


def main():
    args = sys.argv[1:]
    notif_type = "URL_UPDATED"
    if args and args[0] == "--delete":
        notif_type = "URL_DELETED"
        args = args[1:]

    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성이 없습니다:  pip install google-auth requests")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스계정 JSON 경로를 설정하세요.")

    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    urls = normalize(args) if args else sitemap_urls()
    print(f"{notif_type}  {len(urls)}개 통보:")
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": notif_type}, timeout=30)
        print(f"  {r.status_code}  {u}")
        if r.status_code >= 400:
            print("     →", r.text[:200])


if __name__ == "__main__":
    main()
