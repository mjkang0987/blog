---
layout: post
title: "DSR 계산법과 주담대 한도 계산기 — 스트레스DSR 40% 총정리 🏠"
date: 2026-09-23 07:00:00 +0900
lang: ko
permalink: /2026/09/23/dsr-loan-limit-calculation/
page_id: 2026-09-23-dsr-loan-limit-calculation
image: /assets/og/2026-09-23-dsr-loan-limit-calculation-ko.png
summary: "주택담보대출 한도를 좌우하는 것은 집값(LTV)이 아니라 결국 내 소득(DSR)입니다. DSR은 '모든 대출의 연간 원리금 상환액 ÷ 연소득'으로 계산하며, 은행권은 40%, 제2금융권은 50%를 넘으면 신규 대출이 막힙니다. 여기에 스트레스 DSR이 더해져 실제 금리보다 높은 심사금리로 한도를 산정하는데, 2025년 10월부터 수도권·규제지역 주담대는 스트레스 금리 3.0%가 적용됩니다. DSR 공식과 한도 산출 원리, 그리고 내 조건을 넣으면 최대 한도가 바로 나오는 계산기를 함께 정리했습니다."
description: "DSR 계산법과 주담대 한도 산출을 계산기와 함께 정리했습니다. 은행권 40%·스트레스DSR 3% 심사금리 반영, 연소득만 넣으면 내 최대 대출한도가 바로 나옵니다."
categories: [부동산]
tags: [DSR, DSR계산법, 주택담보대출한도, 주담대한도, 스트레스DSR, 스트레스금리, DSR40%, 총부채원리금상환비율, 대출한도계산기, 원리금균등상환, 심사금리, LTV, 제2금융권50%, 주담대계산기, 가계대출규제]
---

집을 살 때 대출이 얼마나 나오느냐는 질문의 답은, 사실 집값이 아니라 **내 소득**에 달려 있습니다. 주택담보대출 한도는 **DSR(총부채원리금상환비율)**이라는 규제로 정해지고, 은행권에서는 **연소득의 40%를 넘는 원리금**이 잡히는 대출은 아예 받을 수 없기 때문입니다. 여기에 2025년부터 시행된 **스트레스 DSR**이 더해지면서, 실제 금리보다 높은 금리로 심사를 하다 보니 같은 소득이라도 한도는 예전만 못해졌습니다. 🏠

**핵심 요약 (TL;DR)**

- DSR = (모든 대출의 연간 원리금 상환액 합계 ÷ 연소득) × 100, 은행권 **40%**·제2금융권 **50%**가 상한입니다.
- 스트레스 DSR은 실제 금리에 **가산금리(스트레스 금리)**를 얹은 심사금리로 한도를 매기며, 수도권·규제지역 주담대는 2025년 10월 16일부터 **3.0%**가 적용됩니다.
- 아래 계산기에 연소득·금리·만기를 넣으면 DSR 40% 기준 **최대 대출한도**가 바로 나옵니다.

## DSR이란 무엇인가 — 소득으로 갚을 수 있는 만큼만 💡

DSR은 '내가 1년 동안 갚아야 하는 모든 대출의 원리금이 연소득에서 차지하는 비율'을 말합니다. 공식 자체는 간단합니다.

> **DSR(%) = (연간 원리금 상환액 합계 ÷ 연소득) × 100**

여기서 중요한 건 '모든 대출'을 다 합친다는 점입니다. 새로 받으려는 주택담보대출은 물론이고 기존 신용대출, 카드론, 자동차 할부, 제2금융권 대출까지 1년치 원리금을 빠짐없이 더합니다. 그래서 신용대출이나 마이너스통장을 이미 쓰고 있으면 그만큼 주담대 한도가 깎입니다.

예전에 쓰던 DTI(총부채상환비율)는 주담대만 원리금을 보고 다른 대출은 '이자만' 반영했습니다. 반면 DSR은 모든 대출의 **원금과 이자를 함께** 계산에 넣습니다. 규제가 훨씬 빡빡해진 이유가 여기에 있습니다.

## 은행권 40%, 제2금융권 50% — 넘으면 대출이 막힌다 📊

DSR은 차주(대출받는 사람) 단위로 따지고, 금융권마다 상한이 다릅니다.

| 구분 | DSR 상한 | 초과 시 |
|---|---|---|
| 제1금융권 (은행) | **40%** | 신규 대출 사실상 불가 |
| 제2금융권 (저축은행·보험·상호금융 등) | **50%** | 신규 대출 사실상 불가 |

가령 연소득이 5,000만 원이라면, 은행에서는 모든 대출의 연간 원리금을 더한 값이 **2,000만 원(40%)**을 넘어가는 대출은 받을 수 없습니다. 만약 이미 신용대출 원리금으로 연 500만 원을 갚는 중이라면, 새 주담대에 쓸 수 있는 여력은 1,500만 원까지 쪼그라듭니다.

## 스트레스 DSR — 실제 금리보다 높은 '심사금리'로 잰다 ⚠️

여기서 한 겹이 더 붙습니다. **스트레스 DSR**은 '앞으로 금리가 더 오를 수도 있다'는 상황을 미리 반영하는 제도로, 실제 대출금리에 **스트레스 금리(가산금리)**를 얹은 심사금리로 한도를 계산합니다. 내가 실제로 내는 이자는 그대로지만, 한도를 잴 때만 더 높은 금리를 대입해 대출을 보수적으로 조입니다.

3단계 스트레스 DSR은 2025년 7월 1일부터 전 금융권·모든 가계대출에 적용됐고, 기본 스트레스 금리는 **1.5%**입니다. 다만 지역에 따라 갈립니다.

| 구분 | 적용 스트레스 금리 | 시행 |
|---|---|---|
| 수도권·규제지역 주담대 | **3.0%** | 2025년 10월 16일부터 |
| 지방 주담대 | 한 단계 낮은 수준(유예) | 2026년 6월 30일까지 유예 |
| 신용대출(1억 원 초과분) | 1.5% 기준 | 2025년 7월 1일부터 |

스트레스 금리는 하한 1.5%에서 상한 3.0% 사이에서 정해지는데, 수도권은 규제 탓에 사실상 상한인 3.0%가 그대로 붙었습니다. 그래서 예컨대 연소득 1억 원인 차주가 수도권에서 변동금리로 주담대를 받을 경우, 한도가 약 5억 8,700만 원에서 5억 100만 원으로 **14.7%가량 줄어든** 사례도 나왔습니다.

## 내 주담대 한도 직접 계산하기 🧮

연소득과 금리, 만기를 넣으면 DSR 한도 기준 최대 대출금액을 확인할 수 있습니다. 심사금리(실제 금리 + 스트레스 금리)로 원리금을 계산하고, 상환방식은 원리금균등을 기준으로 삼았습니다.
{% raw %}
<div class="dsrcalc" id="dsrcalc">
  <style>
    .dsrcalc { border: 1px solid #e2e2e2; border-radius: 12px; padding: 20px; margin: 8px 0 4px; background: #fafafa; }
    .dsrcalc .dsrcalc__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px 18px; }
    .dsrcalc .dsrcalc__label { display: block; font-size: 13px; color: #555; margin-bottom: 4px; }
    .dsrcalc .dsrcalc__field { width: 100%; box-sizing: border-box; height: 38px; padding: 0 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; background: #fff; }
    .dsrcalc .dsrcalc__hint { font-size: 12px; color: #1b4fa0; margin-top: 4px; min-height: 16px; }
    .dsrcalc .dsrcalc__cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-top: 18px; align-items: start; }
    .dsrcalc .dsrcalc__card { background: #fff; border: 1px solid #ececec; border-radius: 8px; padding: 14px; }
    .dsrcalc .dsrcalc__card-label { font-size: 13px; color: #666; }
    .dsrcalc .dsrcalc__card-value { font-size: 18px; font-weight: 600; margin-top: 4px; }
    .dsrcalc .dsrcalc__card-sub { font-size: 12px; color: #999; margin-top: 2px; }
    .dsrcalc .dsrcalc__final { background: #eef4ff; border: 1px solid #cdddff; border-radius: 12px; padding: 16px 18px; margin-top: 14px; }
    .dsrcalc .dsrcalc__final-label { font-size: 13px; color: #1b4fa0; }
    .dsrcalc .dsrcalc__final-value { font-size: 26px; font-weight: 700; color: #1b4fa0; margin-top: 2px; }
    .dsrcalc .dsrcalc__note { font-size: 12px; color: #888; margin-top: 12px; line-height: 1.5; }
  </style>
  <div class="dsrcalc__grid">
    <div>
      <label class="dsrcalc__label" for="dsr-income">연소득 (만원)</label>
      <input class="dsrcalc__field" id="dsr-income" type="number" inputmode="numeric" min="0" step="100" value="6000">
      <p class="dsrcalc__hint" id="dsr-income-hint" aria-live="polite"></p>
    </div>
    <div>
      <label class="dsrcalc__label" for="dsr-rate">실제 대출금리 (연 %)</label>
      <input class="dsrcalc__field" id="dsr-rate" type="number" inputmode="decimal" min="0" step="0.1" value="4.5">
    </div>
    <div>
      <label class="dsrcalc__label" for="dsr-stress">스트레스 금리 (연 %)</label>
      <input class="dsrcalc__field" id="dsr-stress" type="number" inputmode="decimal" min="0" step="0.1" value="3.0">
      <p class="dsrcalc__hint" id="dsr-stress-hint" aria-live="polite">수도권·규제지역 3.0% 기준</p>
    </div>
    <div>
      <label class="dsrcalc__label" for="dsr-term">대출 만기 (년)</label>
      <input class="dsrcalc__field" id="dsr-term" type="number" inputmode="numeric" min="1" max="50" step="1" value="30">
    </div>
    <div>
      <label class="dsrcalc__label" for="dsr-existing">기존 대출 연간 원리금 (만원)</label>
      <input class="dsrcalc__field" id="dsr-existing" type="number" inputmode="numeric" min="0" step="10" value="0">
      <p class="dsrcalc__hint" id="dsr-existing-hint" aria-live="polite">신용대출·기존 주담대 등 합계</p>
    </div>
    <div>
      <label class="dsrcalc__label" for="dsr-limit">DSR 한도</label>
      <select class="dsrcalc__field" id="dsr-limit">
        <option value="40" selected>은행권 40%</option>
        <option value="50">제2금융권 50%</option>
      </select>
    </div>
  </div>
  <div class="dsrcalc__cards">
    <div class="dsrcalc__card">
      <div class="dsrcalc__card-label">심사금리 (스트레스 포함)</div>
      <div class="dsrcalc__card-value" id="dsr-review">-</div>
      <div class="dsrcalc__card-sub">실제금리 + 스트레스금리</div>
    </div>
    <div class="dsrcalc__card">
      <div class="dsrcalc__card-label">연간 상환여력</div>
      <div class="dsrcalc__card-value" id="dsr-capacity">-</div>
      <div class="dsrcalc__card-sub" id="dsr-capacity-sub">연소득 × DSR − 기존 원리금</div>
    </div>
    <div class="dsrcalc__card">
      <div class="dsrcalc__card-label">실제금리 기준 월 상환액</div>
      <div class="dsrcalc__card-value" id="dsr-monthly">-</div>
      <div class="dsrcalc__card-sub">참고용(실제 납입 예상)</div>
    </div>
  </div>
  <div class="dsrcalc__final">
    <div class="dsrcalc__final-label">DSR 기준 최대 대출한도</div>
    <div class="dsrcalc__final-value" id="dsr-max">-</div>
  </div>
  <p class="dsrcalc__note">원리금균등상환·심사금리(실제금리+스트레스금리) 기준의 개략 추정치입니다. 실제 한도는 LTV(담보인정비율)·소득 산정 방식·은행별 가산금리·지역별 스트레스 금리 적용에 따라 달라질 수 있으며, 이 계산기는 DSR 한도만 반영합니다. 정확한 한도는 해당 금융기관에 문의하시기 바랍니다.</p>
  <script>
    (function () {
      var ids = ['dsr-income', 'dsr-rate', 'dsr-stress', 'dsr-term', 'dsr-existing', 'dsr-limit'];
      var num = function (id) { return parseFloat(document.getElementById(id).value) || 0; };
      var man = function (v) { return Math.round(v).toLocaleString('ko-KR') + '만원'; };
      var eok = function (v) { return '약 ' + (v / 10000).toLocaleString('ko-KR', { maximumFractionDigits: 2 }) + '억 원'; };

      // 원리금균등: 원금 1당 월 상환액 계수
      function monthlyFactor(monthlyRate, months) {
        if (monthlyRate <= 0) return 1 / months;
        var p = Math.pow(1 + monthlyRate, months);
        return monthlyRate * p / (p - 1);
      }

      function calc() {
        var income = num('dsr-income');
        var rate = num('dsr-rate');
        var stress = num('dsr-stress');
        var term = num('dsr-term');
        var existing = num('dsr-existing');
        var limitPct = num('dsr-limit') / 100;

        var reviewRate = rate + stress;
        var months = Math.max(1, Math.round(term * 12));
        var rmReview = reviewRate / 100 / 12;
        var rmReal = rate / 100 / 12;

        var capacity = income * limitPct - existing; // 연간 상환여력(만원)
        document.getElementById('dsr-review').textContent = reviewRate.toFixed(1) + '%';
        document.getElementById('dsr-capacity').textContent = capacity > 0 ? man(capacity) : '0원';

        if (capacity <= 0) {
          document.getElementById('dsr-max').textContent = '0원 (한도 없음)';
          document.getElementById('dsr-monthly').textContent = '-';
          return;
        }

        var monthlyCapacity = capacity / 12; // 월 상환여력(만원)
        var fReview = monthlyFactor(rmReview, months);
        var maxLoan = monthlyCapacity / fReview; // 최대 원금(만원)

        var fReal = monthlyFactor(rmReal, months);
        var realMonthly = maxLoan * fReal; // 실제금리 월 상환액(만원)

        document.getElementById('dsr-max').textContent = man(maxLoan) + ' (' + eok(maxLoan) + ')';
        document.getElementById('dsr-monthly').textContent = man(realMonthly);
      }

      for (var i = 0; i < ids.length; i++) {
        document.getElementById(ids[i]).addEventListener('input', calc);
        document.getElementById(ids[i]).addEventListener('change', calc);
      }
      calc();
    })();
  </script>
</div>
{% endraw %}

## 계산 예시 — 연소득 6,000만 원이라면 📈

연소득 6,000만 원에 실제 금리 4.5%, 스트레스 금리 3.0%, 만기 30년, 기존 대출은 없는 경우로 한번 계산해 보겠습니다.

- 연간 상환여력 = 6,000만 원 × 40% = **2,400만 원** (월 200만 원)
- 심사금리 = 4.5% + 3.0% = **7.5%**
- 심사금리 7.5%·30년 원리금균등 기준 최대 한도 ≈ **약 2억 8,600만 원**

같은 조건에서 스트레스 금리가 없다고 보면(심사금리 4.5%) 한도는 약 3억 9,400만 원까지 올라갑니다. 스트레스 금리 3.0%포인트가 붙는 것만으로 한도가 **1억 원 넘게** 깎이는 셈입니다. 반대로 기존 신용대출 원리금이 연 600만 원 있으면 상환여력이 1,800만 원으로 줄고, 최대 한도도 그만큼 내려갑니다.

여기에 실제 대출은 **LTV(담보인정비율)** 한도까지 함께 적용받습니다. DSR로 따진 한도와 LTV로 따진 한도 가운데 **더 낮은 금액**이 실제로 빌릴 수 있는 돈이 됩니다. 소득이 넉넉해도 담보가 모자라면 LTV에서, 담보가 충분해도 소득이 모자라면 DSR에서 한도가 잘립니다.

## 총평 — 한도를 늘리는 현실적인 지렛대 🔑

DSR 체계에서 한도를 좌우하는 변수는 결국 세 가지입니다. **소득을 늘리거나, 기존 대출 원리금을 줄이거나, 만기를 늘리는 것**이죠. 그중에서도 기존 신용대출이나 카드론을 정리하면 그 원리금만큼 주담대 여력이 곧바로 되살아납니다. 만기를 늘리면 해마다 갚을 원리금이 줄어 한도는 커지지만, 대신 총이자 부담이 늘어난다는 점도 같이 따져 봐야 합니다.

대출을 생각하고 있다면 매물을 보러 다니기 전에 내 DSR부터 먼저 계산해 보길 권합니다. 살 수 있는 집의 가격대는 이미 소득에서 정해져 있으니까요.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

**출처**

- [3단계 스트레스 DSR 시행방안 확정·발표 (금융위원회 보도자료)](https://www.fsc.go.kr/no010101/84617)
- [3단계 스트레스 DSR 7월부터 시행 (대한민국 정책브리핑)](https://www.korea.kr/news/policyNewsView.do?newsId=148943522)
- [스트레스 DSR 3단계 시행, 대출 한도 얼만큼 줄었을까? (KB의 생각)](https://kbthink.com/loan-guide/stressdsr.html)
- [스트레스 DSR 3단계 시행돼요 (토스뱅크)](https://www.tossbank.com/articles/stressdsr3)
- [스트레스금리 개요 (전국은행연합회 소비자포털)](https://portal.kfb.or.kr/compare/stress_loan_overview.php)
