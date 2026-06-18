#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 (Bing·Naver·Yandex·Seznam 등 IndexNow 참여 엔진).

IndexNow는 한 엔진에 제출하면 참여 엔진끼리 URL을 공유하는 프로토콜입니다.
네이버와 빙(Bing)이 모두 참여하므로, 이 스크립트 한 번으로 두 곳에 즉시 통보됩니다.
(구글은 IndexNow에 참여하지 않습니다 → tools/google_indexing.py 사용)

사용법:
  python tools/indexnow.py
      → sitemap.xml 의 모든 URL을 일괄 통보 (첫 등록·대량 갱신용)

  python tools/indexnow.py https://gangbuk-swedish-massage.pages.dev/magazine/새글/
      → 지정한 URL만 즉시 통보 (글 하나 올렸을 때)

  python tools/indexnow.py /magazine/새글/ /gangbuk/suyu-dong/
      → 경로만 줘도 BASE_URL 기준으로 통보

먼저 `python build.py` 로 사이트와 키 파일(/{KEY}.txt)을 생성해 두세요.
키 파일이 실제 도메인에서 200으로 응답해야 통보가 수락됩니다.
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
HOST = urlsplit(BASE).netloc

# IndexNow 제출 엔드포인트(아무 곳에나 제출하면 참여 엔진끼리 공유됨).
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://yandex.com/indexnow",
]


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    tree = ET.parse(path)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text.strip() for el in tree.findall(".//s:loc", ns)]


def normalize(args):
    urls = []
    for a in args:
        if a.startswith("http://") or a.startswith("https://"):
            urls.append(a)
        else:
            urls.append(BASE + "/" + a.lstrip("/"))
    return urls


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }).encode("utf-8")

    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"  {r.status} {r.reason:12} ← {ep}")
        except urllib.error.HTTPError as e:
            # 202/200 외 코드도 의미가 있으므로 그대로 출력
            print(f"  {e.code} {e.reason:12} ← {ep}")
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR        ← {ep}  ({e})")


def main():
    args = sys.argv[1:]
    urls = normalize(args) if args else sitemap_urls()
    print(f"호스트: {HOST}  키: {INDEXNOW_KEY}")
    print(f"통보 URL {len(urls)}개:")
    for u in urls:
        print("  -", u)
    print("제출 결과 (200/202 = 수락):")
    submit(urls)
    print("\n완료. 키 파일이 실제 도메인에서 열려야 최종 수락됩니다:")
    print(f"  {BASE}/{INDEXNOW_KEY}.txt")


if __name__ == "__main__":
    main()
