# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "강북구 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 강북구"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "강북구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 삼양동, 미아동, 송중동, 송천동, 삼각산동, 번동, 수유동, 우이동, 인수동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "수유역이나 미아사거리역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "번1동과 수유1동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "번1·2·3동은 번동 페이지, 수유1·2·3동은 수유동 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "테마별 관리는 어디에서 확인하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다."
      }}
    }}
  ]
}}
</script>
"""

_NAVER = '<meta name="naver-site-verification" content="f28a7fc6e16bb412121b85a57ef4a0d0a94277d8">\n'

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 강북구 전지역</p>
    <h1>강북 출장마사지·홈타이<br>예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>9개</strong><span>대표 행정동</span></li>
      <li><strong>11개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>강북 출장마사지·홈타이 서비스 안내</h2>
<p>강북구에서 방문 마사지와 홈타이 예약을 찾는 분들을 위해 가능 지역, 예약 절차, 코스 선택 기준, 이용 전 확인사항을 한곳에 정리했습니다. 이 페이지는 강북구 전체 구조를 설명하는 허브 역할을 하며, 더 자세한 내용은 지역별·지하철역별·생활권별·테마별 안내 페이지에서 확인하실 수 있습니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 처음 이용하시는 분도 어렵지 않게 예약할 수 있도록 각 단계를 명확하게 안내해 드립니다. 강북구는 4호선과 우이신설선이 지나는 지역이라 역 기준으로 위치를 설명하시는 분이 많은데, 어느 기준으로 찾으셔도 같은 내용에 닿도록 페이지를 연결해 두었습니다.</p>
</section>

<section id="coverage">
<h2>강북구 전지역 방문 가능 안내</h2>
<p>강북구 지역 안내는 삼양동, 미아동, 송중동, 송천동, 삼각산동, 번동, 수유동, 우이동, 인수동 아홉 개 대표 동을 중심으로 구성되어 있습니다. 번1동부터 번3동, 수유1동부터 수유3동처럼 숫자로 나뉜 행정동은 별도 페이지를 만들지 않고 각 대표 동 페이지에서 통합하여 안내합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하는 것보다, 동 단위로 묶어 생활권 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 정확하기 때문입니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 안내</h2>
<p>지역별 안내는 강북구 대표 동 기준으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간, 어울리는 테마를 동마다 고유한 내용으로 설명합니다. 아래에서 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/gangbuk/samyang-dong/">삼양동</a></li>
<li><a href="/gangbuk/mia-dong/">미아동</a></li>
<li><a href="/gangbuk/songjung-dong/">송중동</a></li>
<li><a href="/gangbuk/songcheon-dong/">송천동</a></li>
<li><a href="/gangbuk/samgaksan-dong/">삼각산동</a></li>
<li><a href="/gangbuk/beon-dong/">번동</a></li>
<li><a href="/gangbuk/suyu-dong/">수유동</a></li>
<li><a href="/gangbuk/ui-dong/">우이동</a></li>
<li><a href="/gangbuk/insu-dong/">인수동</a></li>
</ul>
<p>강북구 전체 구조가 궁금하시면 <a href="/gangbuk/">강북구 전체 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>지하철역 인근 안내</h2>
<p>지하철역별 안내는 강북구를 지나는 4호선과 우이신설선 주요 역세권을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표 동, 예약 가능 시간, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 같은 역을 노선별·방향별로 나누지 않고 역마다 한 페이지만 운영합니다.</p>
<ul class="card-grid">
<li><a href="/gangbuk/stations/miasageori-station/">미아사거리역</a></li>
<li><a href="/gangbuk/stations/mia-station/">미아역</a></li>
<li><a href="/gangbuk/stations/suyu-station/">수유역</a></li>
<li><a href="/gangbuk/stations/bukhansan-ui-station/">북한산우이역</a></li>
<li><a href="/gangbuk/stations/solbat-park-station/">솔밭공원역</a></li>
<li><a href="/gangbuk/stations/april19-cemetery-station/">4.19민주묘지역</a></li>
<li><a href="/gangbuk/stations/gaori-station/">가오리역</a></li>
<li><a href="/gangbuk/stations/hwagye-station/">화계역</a></li>
<li><a href="/gangbuk/stations/samyang-station/">삼양역</a></li>
<li><a href="/gangbuk/stations/samyang-sageori-station/">삼양사거리역</a></li>
<li><a href="/gangbuk/stations/solsaem-station/">솔샘역</a></li>
</ul>
</section>

<section id="districts">
<h2>생활권·주요 거점 안내</h2>
<p>행정동이나 역 이름보다 익숙한 생활권 기준으로 위치를 떠올리는 분들을 위해, 강북구의 대표 거점을 따로 정리했습니다. 수유역 상권, 미아사거리 생활권, 번동 북서울꿈의숲 인근, 우이동 북한산 입구처럼 실제 검색 수요가 있는 거점만 골라 페이지로 만들었습니다. 각 생활권 페이지는 행정동·역 페이지와 내용이 겹치지 않도록 거점의 성격에 초점을 맞춰 설명합니다.</p>
<ul class="card-grid">
<li><a href="/gangbuk/areas/suyu-station-area/">수유역 상권</a></li>
<li><a href="/gangbuk/areas/miasageori-area/">미아사거리 생활권</a></li>
<li><a href="/gangbuk/areas/bukseoul-dream-forest-area/">번동 북서울꿈의숲 인근</a></li>
<li><a href="/gangbuk/areas/bukhansan-ui-area/">우이동 북한산 입구</a></li>
<li><a href="/gangbuk/areas/samyang-sageori-area/">삼양사거리 생활권</a></li>
<li><a href="/gangbuk/areas/gaori-area/">가오리역 생활권</a></li>
<li><a href="/gangbuk/areas/hwagye-area/">화계역 생활권</a></li>
<li><a href="/gangbuk/areas/solsaem-samgaksan-area/">솔샘역·삼각산 생활권</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 해 드립니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>코스는 이용 목적과 그날의 컨디션에 따라 선택하시는 것이 좋습니다. 누적된 피로를 풀고 싶은 분, 편안한 휴식이 필요한 분, 운동 후 근육 이완이 필요한 분, 숙소로 방문을 원하시는 분, 커플이 함께 받고 싶은 분 등 상황에 맞는 선택 기준을 <a href="/courses/">코스안내</a> 페이지에서 자세히 다룹니다. 고민되시면 예약 전화에서 상태를 말씀해 주세요. 함께 정해 드립니다.</p>
</section>

<section id="how">
<h2>예약 진행 방식</h2>
<p>예약은 다섯 단계로 진행됩니다. 먼저 희망 지역 또는 역 인근 위치를 확인하고, 희망 시간을 확인한 뒤, 코스와 인원을 정하고, 방문 가능 여부를 안내받은 다음, 예약을 확정합니다. 저녁 시간대나 주말에는 문의가 몰릴 수 있으므로 한두 시간 이상 여유를 두고 예약하시기를 권장합니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>원활한 방문 관리를 위해 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 확인해 주시면 좋습니다. 숙소나 오피스텔로 방문을 요청하실 때는 건물 출입 안내와 예약 시간대 연락 가능 여부를 함께 알려주세요. 준비사항 전체는 <a href="/guide/">이용가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>건전하고 안전한 방문 관리를 위해 위생 기준, 예약 정보 확인, 개인정보 보호, 금지행위 안내를 명확히 제공합니다. 이용 전 서비스 범위와 유의사항을 확인해 주시고, 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않는다는 기준을 분명히 안내드립니다. 예약 정보는 관리 목적 외에 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>강북구 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내 페이지에서 삼양동, 미아동, 송중동, 송천동, 삼각산동, 번동, 수유동, 우이동, 인수동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>수유역이나 미아사거리역 근처도 가능한가요?</h3>
<p>주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>번1동과 수유1동은 왜 따로 없나요?</h3>
<p>번1·2·3동은 번동 대표 페이지, 수유1·2·3동은 수유동 대표 페이지에서 통합 안내하여 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 저녁 시간대와 주말은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>테마별 관리는 어디에서 확인하나요?</h3>
<p>스웨디시, 타이마사지, 홈케어 등 테마별 안내 페이지에서 특징과 추천 대상을 확인할 수 있습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>강북구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "강북 출장마사지·홈타이 | 강북구 전지역 방문 마사지 예약 안내",
    "desc": "강북 출장마사지·홈타이 예약 전 행정동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "강북 출장마사지·홈타이 예약 안내",
    "body": _BODY,
    "extra_head": _NAVER + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
