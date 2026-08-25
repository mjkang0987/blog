---
layout: post
title: "보유세 계산법 총정리 — 재산세·종합부동산세 세율과 1주택 계산 예시 🏠"
date: 2026-08-26 07:00:00 +0900
lang: ko
permalink: /2026/08/26/property-holding-tax-calculation/
page_id: 2026-08-26-property-holding-tax-calculation
image: /assets/og/2026-08-26-property-holding-tax-calculation-ko.png
summary: "보유세는 재산세와 종합부동산세를 합한 세금으로, '공시가격 × 공정시장가액비율 = 과세표준'을 구한 뒤 누진세율을 적용해 계산합니다. 재산세 공정시장가액비율은 1주택자 43~45%, 종부세는 60%이며 1세대 1주택 종부세 공제는 12억 원입니다. 세율표와 1주택 계산 예시, 계산기까지 정리했습니다."
description: "보유세(재산세·종합부동산세) 계산법을 공정시장가액비율과 세율표, 1주택 계산 예시로 정리했습니다. 종부세 12억 공제 기준과 계산기까지 확인하세요."
categories: [부동산]
tags: [보유세, 보유세계산, 재산세, 종합부동산세, 종부세, 재산세계산, 공정시장가액비율, 재산세율, 종부세율, 1세대1주택, 재산세계산기, 보유세계산기, 공시가격, 지방교육세, 부동산세금]
---

**핵심 요약 (TL;DR)**

- 보유세는 재산세와 종합부동산세를 합한 세금으로, '공시가격 × 공정시장가액비율 = 과세표준'을 먼저 구한 뒤 구간별 누진세율을 적용합니다.
- 재산세 공정시장가액비율은 1세대 1주택자가 공시가격에 따라 43~45%, 종합부동산세는 60%이며, 1세대 1주택 종부세 기본공제는 12억 원입니다.
- 공시가격 12억 원(1주택) 이하라면 종부세 대상이 아니어서 대부분의 1주택자는 재산세만 냅니다.

6월 1일에 집을 가지고 있으면 그해 재산세와 종합부동산세를 내게 됩니다. **보유세는 '공시가격 × 공정시장가액비율'로 과세표준을 구하고 여기에 누진세율을 곱해 계산하며, 재산세는 모든 주택 보유자가, 종합부동산세는 공시가격 합계가 공제 기준(1세대 1주택 12억 원)을 넘는 사람만 추가로 냅니다.** 계산 구조는 둘이 똑같고, 종부세가 고가·다주택에만 얹힐 뿐입니다.

아래 계산기에 공시가격과 보유 형태만 넣으면 재산세와 종부세 예상액이 바로 나옵니다. 세율표와 1주택 계산 예시는 그 아래에서 이어집니다. 💡

{% raw %}
<div class="htax-calc" id="htax-calc">
  <style>
    .htax-calc { border: 1px solid #e2e2e2; border-radius: 12px; padding: 20px; margin: 8px 0 4px; background: #fafafa; }
    .htax-calc .htax-calc__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px 18px; }
    .htax-calc .htax-calc__label { display: block; font-size: 13px; color: #555; margin-bottom: 4px; }
    .htax-calc .htax-calc__field { width: 100%; box-sizing: border-box; height: 38px; padding: 0 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; background: #fff; }
    .htax-calc .htax-calc__hint { font-size: 12px; color: #1b4fa0; margin-top: 4px; min-height: 16px; }
    .htax-calc .htax-calc__cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-top: 18px; align-items: start; }
    .htax-calc .htax-calc__card { background: #fff; border: 1px solid #ececec; border-radius: 8px; padding: 14px; }
    .htax-calc .htax-calc__card-label { font-size: 13px; color: #666; }
    .htax-calc .htax-calc__card-value { font-size: 18px; font-weight: 600; margin-top: 4px; }
    .htax-calc .htax-calc__card-sub { font-size: 12px; color: #999; margin-top: 2px; }
    .htax-calc .htax-calc__final { background: #eef4ff; border: 1px solid #cdddff; border-radius: 12px; padding: 16px 18px; margin-top: 14px; }
    .htax-calc .htax-calc__final-label { font-size: 13px; color: #1b4fa0; }
    .htax-calc .htax-calc__final-value { font-size: 26px; font-weight: 700; color: #1b4fa0; margin-top: 2px; }
    .htax-calc .htax-calc__note { font-size: 12px; color: #888; margin-top: 12px; line-height: 1.5; }
  </style>
  <div class="htax-calc__grid">
    <div>
      <label class="htax-calc__label" for="htax-price">주택 공시가격 (원)</label>
      <input class="htax-calc__field" id="htax-price" type="number" inputmode="numeric" min="0" step="10000000" value="800000000">
      <p class="htax-calc__hint" id="htax-price-hint" aria-live="polite"></p>
    </div>
    <div>
      <label class="htax-calc__label" for="htax-type">보유 형태</label>
      <select class="htax-calc__field" id="htax-type">
        <option value="single" selected>1세대 1주택</option>
        <option value="multi">다주택·법인 등</option>
      </select>
      <p class="htax-calc__hint" id="htax-type-hint" aria-live="polite"></p>
    </div>
  </div>
  <div class="htax-calc__cards">
    <div class="htax-calc__card">
      <div class="htax-calc__card-label">재산세 과세표준</div>
      <div class="htax-calc__card-value" id="htax-base">-</div>
      <div class="htax-calc__card-sub" id="htax-ratio">-</div>
    </div>
    <div class="htax-calc__card">
      <div class="htax-calc__card-label">재산세 (지방교육세·도시지역분 포함)</div>
      <div class="htax-calc__card-value" id="htax-property">-</div>
      <div class="htax-calc__card-sub" id="htax-property-sub">-</div>
    </div>
    <div class="htax-calc__card">
      <div class="htax-calc__card-label">종합부동산세 (개략 추정)</div>
      <div class="htax-calc__card-value" id="htax-jongbu">-</div>
      <div class="htax-calc__card-sub" id="htax-jongbu-sub">-</div>
    </div>
  </div>
  <div class="htax-calc__final">
    <div class="htax-calc__final-label">연간 보유세 합계 (개략)</div>
    <div class="htax-calc__final-value" id="htax-total">-</div>
  </div>
  <p class="htax-calc__note">재산세는 표준·특례세율과 공정시장가액비율을 반영한 값입니다. 종합부동산세는 재산세 중복분 공제·고령자·장기보유 세액공제 등을 빼기 전 산출세액 기준의 개략 추정치로, 실제 고지액은 이보다 낮아질 수 있습니다. 세부담상한, 1주택 특례세율의 공시가격 9억 원 한도는 계산에 반영했습니다. 정확한 세액은 위택스·홈택스 또는 관할 세무서에서 확인하시기 바랍니다.</p>
  <script>
    (function () {
      var priceEl = document.getElementById('htax-price');
      var typeEl = document.getElementById('htax-type');
      var won = function (n) { return Math.round(n).toLocaleString('ko-KR') + '원'; };
      var eok = function (n) { return (n / 100000000).toLocaleString('ko-KR', { maximumFractionDigits: 2 }) + '억 원'; };

      function propertyFairRatio(price) {
        if (price <= 300000000) return 0.43;
        if (price <= 600000000) return 0.44;
        return 0.45;
      }
      // 재산세 산출세액 (표준세율)
      function propertyStandard(base) {
        if (base <= 60000000) return base * 0.001;
        if (base <= 150000000) return 60000 + (base - 60000000) * 0.0015;
        if (base <= 300000000) return 195000 + (base - 150000000) * 0.0025;
        return 570000 + (base - 300000000) * 0.004;
      }
      // 1세대 1주택 특례세율 (공시가격 9억 이하)
      function propertySpecial(base) {
        if (base <= 60000000) return base * 0.0005;
        if (base <= 150000000) return 30000 + (base - 60000000) * 0.001;
        if (base <= 300000000) return 120000 + (base - 150000000) * 0.002;
        return 420000 + (base - 300000000) * 0.0035;
      }
      // 종부세 1주택 일반세율 누진 (과세표준 기준)
      function jongbuTax(base) {
        if (base <= 0) return 0;
        var brackets = [
          [300000000, 0.005, 0],
          [600000000, 0.007, 1500000],
          [1200000000, 0.010, 3600000],
          [2500000000, 0.013, 9600000],
          [5000000000, 0.015, 26500000],
          [9400000000, 0.020, 64000000]
        ];
        for (var i = 0; i < brackets.length; i++) {
          if (base <= brackets[i][0]) {
            var prevCap = i === 0 ? 0 : brackets[i - 1][0];
            return brackets[i][2] + (base - prevCap) * brackets[i][1];
          }
        }
        return 152000000 + (base - 9400000000) * 0.027;
      }

      function calc() {
        var price = Number(priceEl.value) || 0;
        var isSingle = typeEl.value === 'single';

        var ratio = isSingle ? propertyFairRatio(price) : 0.60;
        var base = price * ratio;

        var propTax;
        if (isSingle && price <= 900000000) {
          propTax = propertySpecial(base);
        } else {
          propTax = propertyStandard(base);
        }
        var eduTax = propTax * 0.20;         // 지방교육세
        var cityTax = base * 0.0014;         // 도시지역분
        var propertyTotal = propTax + eduTax + cityTax;

        // 종부세
        var deduction = isSingle ? 1200000000 : 900000000;
        var jongbuBase = Math.max(0, (price - deduction)) * 0.60;
        var jongbu = jongbuTax(jongbuBase);
        var jongbuEdu = jongbu * 0.20;       // 농어촌특별세
        var jongbuTotal = jongbu > 0 ? jongbu + jongbuEdu : 0;

        document.getElementById('htax-base').textContent = won(base);
        document.getElementById('htax-ratio').textContent = '공정시장가액비율 ' + Math.round(ratio * 100) + '%';
        document.getElementById('htax-property').textContent = won(propertyTotal);
        document.getElementById('htax-property-sub').textContent = '재산세 ' + won(propTax) + ' + 부가세';
        document.getElementById('htax-jongbu').textContent = jongbuTotal > 0 ? won(jongbuTotal) : '대상 아님';
        document.getElementById('htax-jongbu-sub').textContent = jongbuTotal > 0 ? ('공제 ' + eok(deduction) + ' 초과분') : ('공시 ' + eok(deduction) + ' 이하');
        document.getElementById('htax-total').textContent = won(propertyTotal + jongbuTotal);

        var pHint = document.getElementById('htax-price-hint');
        pHint.textContent = price > 0 ? ('약 ' + eok(price)) : '';
        var tHint = document.getElementById('htax-type-hint');
        tHint.textContent = isSingle ? '종부세 공제 12억 원 적용' : '종부세 공제 9억 원 적용';
      }

      priceEl.addEventListener('input', calc);
      typeEl.addEventListener('change', calc);
      calc();
    })();
  </script>
</div>
{% endraw %}

## 보유세는 재산세와 종합부동산세, 두 가지입니다 🏠

'보유세'는 세금 하나의 이름이 아닙니다. 집을 가지고 있을 때 내는 재산세와 종합부동산세를 묶어 부르는 말입니다. 두 세금 모두 매년 6월 1일 현재 주택을 소유한 사람에게 부과됩니다. 잔금을 6월 1일에 치렀다면 그해 보유세는 매수인이, 5월 31일에 치렀다면 매도인이 냅니다. 하루 차이로 납세자가 갈리는 셈입니다.

재산세는 지방세라 모든 주택 보유자가 냅니다. 부과된 세액은 7월과 9월에 절반씩 나눠 내고, 20만 원 이하면 7월에 한 번에 냅니다. 종합부동산세는 국세로, 개인이 보유한 주택 공시가격을 모두 합해 일정 기준을 넘을 때 그 초과분에만 붙으며, 납부는 매년 12월입니다.

두 세금의 공통 계산 구조는 다음과 같습니다.

**공시가격 × 공정시장가액비율 = 과세표준 → 과세표준 × 세율 = 산출세액**

여기서 '공시가격'은 국토교통부가 매년 발표하는 주택의 공적 가격으로, 실거래가보다 대체로 낮습니다. '공정시장가액비율'은 그 공시가격 가운데 실제 과세 대상으로 잡는 비율을 말합니다. 이 두 개념만 손에 익으면 보유세 계산은 절반 넘게 끝난 것이나 다름없습니다.

## 재산세 세율과 공정시장가액비율 📊

재산세 과세표준은 공시가격에 공정시장가액비율을 곱해 구합니다. 2026년 기준으로 1세대 1주택자는 공시가격에 따라 비율이 달라지고, 다주택자와 법인은 일률적으로 60%입니다.

| 구분 | 공시가격 | 공정시장가액비율 |
| --- | --- | --- |
| 1세대 1주택 | 3억 원 이하 | 43% |
| 1세대 1주택 | 3억~6억 원 | 44% |
| 1세대 1주택 | 6억 원 초과 | 45% |
| 다주택·법인 | 전체 | 60% |

과세표준이 정해지면 아래 4단계 누진세율을 매깁니다. 1세대 1주택이면서 공시가격이 9억 원 이하이면 구간마다 0.05%포인트 낮은 특례세율이 적용됩니다.

| 과세표준 | 표준세율 | 1주택 특례세율(공시 9억 이하) |
| --- | --- | --- |
| 6,000만 원 이하 | 0.1% | 0.05% |
| 6,000만~1.5억 원 | 6만 원 + 초과분 0.15% | 3만 원 + 초과분 0.1% |
| 1.5억~3억 원 | 19.5만 원 + 초과분 0.25% | 12만 원 + 초과분 0.2% |
| 3억 원 초과 | 57만 원 + 초과분 0.4% | 42만 원 + 초과분 0.35% |

여기에 부가세 두 가지가 더 붙습니다. 재산세액의 20%가 **지방교육세**, 과세표준의 0.14%가 **도시지역분**(도시계획구역 내 주택)입니다. 흔히 말하는 '재산세 고지서 금액'은 이 부가세까지 다 합친 값입니다.

공시가격이 갑자기 뛰어도 세금이 한꺼번에 오르지 않도록 **세부담상한제**도 있습니다. 전년도 대비 공시가격 3억 원 이하는 105%, 3억~6억 원은 110%, 6억 원 초과는 130%를 넘겨 오르지 못합니다.

## 종합부동산세는 12억 원을 넘어야 냅니다 💡

종합부동산세는 개인별로 보유한 주택 공시가격을 합산한 뒤, 1세대 1주택자는 12억 원, 그 외에는 9억 원을 공제하고 남는 금액에만 부과됩니다. 그래서 공시가격 12억 원(실거래가로는 대략 16억~17억 원 수준) 이하인 1주택자는 종부세 대상이 아니며, 실수요 1주택자 대부분은 재산세만 내고 끝납니다.

종부세 과세표준은 '(공시가격 합계 − 기본공제) × 공정시장가액비율(60%)'로 구한 다음, 아래 누진세율(2주택 이하 일반세율)을 매깁니다.

| 종부세 과세표준 | 세율 |
| --- | --- |
| 3억 원 이하 | 0.5% |
| 3억~6억 원 | 0.7% |
| 6억~12억 원 | 1.0% |
| 12억~25억 원 | 1.3% |
| 25억~50억 원 | 1.5% |
| 50억~94억 원 | 2.0% |
| 94억 원 초과 | 2.7% |

산출된 종부세에서는 이미 낸 재산세 중 겹치는 부분을 먼저 빼줍니다. 여기에 1세대 1주택자라면 만 60세 이상 고령자 세액공제(연령별 20~40%)와 5년 이상 장기보유 세액공제(보유기간별 20~50%)를 최대 80%까지 합쳐 받을 수 있습니다. 덕분에 공시가격이 같아도 고령의 장기보유 1주택자는 실제 종부세가 훨씬 가벼워집니다. 마지막으로 종부세에는 세액의 20%가 농어촌특별세로 붙습니다.

## 실전 계산 예시 — 공시가격 8억 원과 15억 원 🏠

이제 숫자를 직접 따라가 보겠습니다. 두 사례 모두 1세대 1주택 기준입니다.

**사례 A — 공시가격 8억 원 (종부세 없음)**

- 공정시장가액비율 45%(6억 초과) → 과세표준 = 8억 × 45% = 3억 6,000만 원
- 공시 9억 이하라 특례세율 적용 → 42만 원 + (3.6억 − 3억) × 0.35% = 42만 원 + 21만 원 = 63만 원
- 지방교육세 63만 × 20% = 12만 6,000원, 도시지역분 3.6억 × 0.14% = 50만 4,000원
- 재산세 합계 ≈ **126만 원**
- 공시가격 8억 원 < 12억 원 → 종부세 대상 아님

**사례 B — 공시가격 15억 원 (종부세 대상)**

- 재산세: 공시 9억 초과라 표준세율, 과세표준 = 15억 × 45% = 6억 7,500만 원 → 57만 원 + (6.75억 − 3억) × 0.4% = 207만 원
- 지방교육세 41만 4,000원 + 도시지역분 94만 5,000원 → 재산세 합계 ≈ **342만 9,000원**
- 종부세: 과세표준 = (15억 − 12억) × 60% = 1억 8,000만 원 → 1.8억 × 0.5% = 90만 원(농어촌특별세 포함 약 108만 원, 재산세 중복분·세액공제 전 개략치)
- 두 세금을 합하면 대략 450만 원 안팎이며, 고령·장기보유 공제가 있으면 종부세 부분이 더 줄어듭니다.

공시가격이 8억 원에서 15억 원으로 약 1.9배 오르는 사이, 보유세 부담은 3배 이상으로 불어납니다. 누진세율에 종부세까지 겹치니 고가주택일수록 부담이 가파르게 뛰는 것입니다.

## 알아두면 좋은 점 — 2026년 세제개편 논의 📌

2026년 세제개편안에서는 종합부동산세 기본공제를 실거주 1주택 14억 원, 비거주 9억 원으로 조정하고 공정시장가액비율을 단계적으로 올리는 방안이 논의되고 있습니다. 다만 아직은 국회 심의를 거쳐야 확정되는 안이고, 통과되더라도 그 이후 연도 납세분부터 적용됩니다. 그러니 지금 내는 보유세는 위에서 정리한 현행 기준(1주택 공제 12억 원, 종부세 공정시장가액비율 60%)으로 계산해야 맞습니다.

## 총평

보유세는 복잡해 보여도 '공시가격 × 공정시장가액비율 = 과세표준, 과세표준 × 누진세율 = 세액'이라는 한 줄만 잡으면 직접 어림할 수 있습니다. 재산세는 누구나 내고, 종합부동산세는 1주택 기준 공시가격 12억 원을 넘어야 얹힌다는 점만 기억하면 됩니다. 그리고 6월 1일이라는 과세 기준일 하나로 그해 세금 부담자가 갈리니, 매매 잔금일을 잡을 때는 세율표만큼이나 이 날짜도 꼭 챙기시기 바랍니다.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

**출처**

- [지방세법 시행령 (재산세 공정시장가액비율)](https://www.law.go.kr/LSW/lumLsLinkPop.do?lspttninfSeq=120262)
- [한국세정신문 — 1주택자 공정시장가액비율 43∼45% 유지](https://taxtimes.co.kr/mobile/article.html?no=274811)
- [한국세정신문 — 2026년 세제개편안 목차](https://www.taxtimes.co.kr/news/article.html?no=276259)
- [심플택스 — 2026 재산세율표·1세대 1주택 특례](https://simpletax.kr/taxRate/propertyTaxRate)
- [택스고 — 종합부동산세 기준 2026년 과세대상·세율 정리](https://hometax-go.kr/comprehensive-property-tax/)
