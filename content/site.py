# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://gangbuk-swedish-massage.pages.dev"

BRAND = "바로GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# IndexNow 공유 키 — 빙·네이버 등 IndexNow 참여 검색엔진 즉시 색인 통보용.
# 이 키는 빌드 시 /{INDEXNOW_KEY}.txt 파일로 사이트 루트에 생성된다.
INDEXNOW_KEY = "48c66c365d6f7192b249fa124edd51d6"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("강북 출장마사지", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("전지역 방문 안내", "/massage/#coverage"),
        ("지하철역 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/gangbuk/", [
        ("강북구 전체", "/gangbuk/"),
        ("삼양동", "/gangbuk/samyang-dong/"),
        ("미아동", "/gangbuk/mia-dong/"),
        ("송중동", "/gangbuk/songjung-dong/"),
        ("송천동", "/gangbuk/songcheon-dong/"),
        ("삼각산동", "/gangbuk/samgaksan-dong/"),
        ("번동", "/gangbuk/beon-dong/"),
        ("수유동", "/gangbuk/suyu-dong/"),
        ("우이동", "/gangbuk/ui-dong/"),
        ("인수동", "/gangbuk/insu-dong/"),
    ]),
    ("지하철역별 안내", "/gangbuk/stations/", [
        ("역 전체", "/gangbuk/stations/"),
        ("미아사거리역", "/gangbuk/stations/miasageori-station/"),
        ("미아역", "/gangbuk/stations/mia-station/"),
        ("수유역", "/gangbuk/stations/suyu-station/"),
        ("북한산우이역", "/gangbuk/stations/bukhansan-ui-station/"),
        ("솔밭공원역", "/gangbuk/stations/solbat-park-station/"),
        ("4.19민주묘지역", "/gangbuk/stations/april19-cemetery-station/"),
        ("가오리역", "/gangbuk/stations/gaori-station/"),
        ("화계역", "/gangbuk/stations/hwagye-station/"),
        ("삼양역", "/gangbuk/stations/samyang-station/"),
        ("삼양사거리역", "/gangbuk/stations/samyang-sageori-station/"),
        ("솔샘역", "/gangbuk/stations/solsaem-station/"),
    ]),
    ("생활권·거점 안내", "/gangbuk/areas/", [
        ("생활권 전체", "/gangbuk/areas/"),
        ("수유역 상권", "/gangbuk/areas/suyu-station-area/"),
        ("미아사거리 생활권", "/gangbuk/areas/miasageori-area/"),
        ("번동 북서울꿈의숲 인근", "/gangbuk/areas/bukseoul-dream-forest-area/"),
        ("우이동 북한산 입구", "/gangbuk/areas/bukhansan-ui-area/"),
        ("삼양사거리 생활권", "/gangbuk/areas/samyang-sageori-area/"),
        ("가오리역 생활권", "/gangbuk/areas/gaori-area/"),
        ("화계역 생활권", "/gangbuk/areas/hwagye-area/"),
        ("솔샘역·삼각산 생활권", "/gangbuk/areas/solsaem-samgaksan-area/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("매거진", "/magazine/", [
        ("전체 글", "/magazine/"),
        ("마사지 비교 가이드", "/magazine/swedish-vs-thai/"),
        ("처음 이용 가이드", "/magazine/first-time-guide/"),
        ("수면과 마사지", "/magazine/sleep-and-massage/"),
        ("운동 후 회복", "/magazine/post-workout-timing/"),
        ("어깨·목 결림 관리", "/magazine/neck-shoulder-care/"),
        ("부모님 선물 가이드", "/magazine/parents-gift/"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
