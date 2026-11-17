---
layout: post
title: "임대수익률 계산법, 오피스텔 실질 수익률과 대출 레버리지 총정리 📊"
date: 2026-11-18 07:00:00 +0900
lang: ko
permalink: /2026/11/18/rental-yield-calculation/
page_id: 2026-11-18-rental-yield-calculation
image: /assets/og/2026-11-18-rental-yield-calculation-ko.png
summary: "임대수익률은 연 월세를 매매가에서 보증금을 뺀 실투자금으로 나눠 구합니다. 다만 광고에 나오는 표면 수익률에는 취득세 4.6%·중개보수 같은 부대비용, 보유세·수선비, 공실 손실이 빠져 있어 실제보다 높게 보이기 쉽습니다. 매매가 2억·보증금 1천만·월세 80만 원 오피스텔을 예로 표면 수익률 5.05%가 실질 4.15%로 낮아지는 과정과, 대출 금리가 실질 수익률보다 높으면 레버리지가 오히려 수익률을 깎는 원리를 계산기와 함께 정리했습니다."
description: "임대수익률 계산법을 표면·실질·대출 레버리지 수익률로 나눠 정리하고, 취득세·공실·이자를 넣은 오피스텔 사례와 임대수익률 계산기를 담았습니다."
categories: [부동산]
tags: [임대수익률, 임대수익률계산, 오피스텔수익률, 수익형부동산, 실질수익률, 표면수익률, 레버리지, 실투자금, 오피스텔취득세, 공실률, 월세수익, 적정매수가, 임대수익률계산기]
---

임대수익률은 1년 치 월세를 실제로 들어간 내 돈(매매가 − 보증금 + 부대비용)으로 나눈 값입니다. 광고에 나오는 수익률은 대부분 취득세·중개보수·공실·대출이자를 빼지 않은 숫자라서, 같은 오피스텔도 비용을 다 넣으면 수익률이 1%포인트 안팎 낮아지는 경우가 흔합니다. 📊

**핵심 요약 (TL;DR)**

- 표면 수익률 = 연 월세 ÷ (매매가 − 보증금), 실질 수익률 = (연 월세 − 연간 비용 − 공실 손실) ÷ (매매가 − 보증금 + 취득 부대비용)입니다.
- 오피스텔은 주거용이든 업무용이든 매매 취득세가 지방세를 합쳐 4.6%라서 부대비용 비중이 큽니다.
- 대출 금리가 실질 수익률보다 높으면 대출을 늘릴수록 내 돈 기준 수익률이 오히려 떨어집니다.

## 임대수익률 공식 세 가지 📐

수익형 부동산의 수익률은 무엇을 빼고 무엇으로 나누느냐에 따라 세 가지로 나뉩니다. 분양 광고나 중개 현장에서 말하는 수익률이 어느 쪽인지부터 확인해야 비교가 됩니다.

| 구분 | 분자 | 분모 | 쓰임 |
|---|---|---|---|
| 표면(단순) 수익률 | 연 월세(월세 × 12) | 매매가 − 보증금 | 매물 간 1차 비교, 광고 수치 |
| 실질 수익률 | 연 월세 − 연간 비용 − 공실 손실 | 매매가 − 보증금 + 취득 부대비용 | 실제 투자 판단 |
| 레버리지 수익률 | 실질 순수익 − 연 대출이자 | 위 실투자금 − 대출금 | 대출을 낀 경우 내 돈 기준 수익률 |

보증금을 분모에서 빼는 건 세입자 보증금이 매수 대금 일부를 대신 치러 주기 때문입니다. 다만 이 돈은 계약이 끝나면 돌려줘야 하니 이자 없는 대출이나 마찬가지입니다. 보증금을 크게 받을수록 분모가 줄어 수익률은 올라가지만, 대개 월세가 그만큼 낮아집니다. 보증금과 월세 사이 비율은 [전월세 전환율 계산법](/2026/09/02/jeonse-wolse-conversion-rate-calculation/)에서 따로 다뤘습니다.

한국부동산원 통계의 오피스텔 수익률은 조사 표본의 임대료와 매매가로 산출하는 시장 평균 지표입니다. 개별 매물의 취득세·공실·이자가 빠져 있어 내 물건의 실질 수익률과 곧바로 비교하기는 어렵습니다.

## 취득 부대비용, 오피스텔은 4.6%부터 🧾

실질 수익률 분모에 가장 먼저 들어가는 것이 취득 부대비용입니다. 오피스텔은 아파트와 달리 매매가와 관계없이 취득세 4%, 지방교육세 0.4%, 농어촌특별세 0.2%를 합한 4.6%가 기본입니다. 3억 원짜리 오피스텔이라면 취득세 1,200만 원, 지방교육세 120만 원, 농어촌특별세 60만 원, 모두 합쳐 1,380만 원입니다.

| 항목 | 세율·요율 | 매매가 2억 원 기준 |
|---|---|---|
| 취득세 | 4% | 800만 원 |
| 지방교육세 | 0.4% | 80만 원 |
| 농어촌특별세 | 0.2% | 40만 원 |
| 중개보수(상한 가정) | 0.5% | 100만 원 |
| 합계 | 5.1% | 1,020만 원 |

중개보수는 전용 85㎡ 이하에 부엌·화장실 등을 갖춘 주거용 오피스텔이면 매매 0.5% 이내이고, 그 밖의 오피스텔은 0.9% 이내에서 협의합니다. 부가가치세는 별도입니다. 요율 구조는 [중개보수 계산법](/2026/09/30/brokerage-fee-calculation/)에 정리해 두었습니다. 분양받을 때는 건물분 부가가치세가 붙습니다. 일반임대사업자로 등록하면 환급받을 수 있지만, 나중에 주거용으로 바꾸면 남은 기간만큼 다시 내야 할 수 있으니 미리 따져 봐야 합니다.

## 연간 비용과 공실 손실 🏚️

분자에서 빼는 비용은 집주인이 부담하는 것만 셉니다. 관리비는 보통 세입자 몫이라 공실 기간이 아니면 넣지 않아도 됩니다.

- 재산세: 업무용은 건물분 0.25%, 주거용은 주택 세율을 적용합니다. 과세표준은 공시가격에 공정시장가액비율을 곱해 구합니다.
- 수선·유지비와 화재보험료: 도배·보일러·에어컨 교체 같은 비용을 연 단위로 나눠 잡습니다.
- 공실 손실: 세입자가 바뀌는 사이 비는 기간의 월세와 관리비입니다.

공실이 1개월이면 연 월세의 12분의 1이 사라집니다. 아래 사례 오피스텔(실투자금 약 2억 원, 월세 80만 원)로 공실 기간만 바꿔 보면 차이가 분명합니다.

| 공실 기간(연) | 실질 수익률 |
|---|---|
| 0개월 | 4.55% |
| 1개월 | 4.15% |
| 2개월 | 3.75% |
| 3개월 | 3.35% |

공실이 한 달 늘 때마다 수익률이 약 0.4%포인트씩 떨어집니다. 역세권이 아니거나 주변에 신축 공급이 많은 지역이라면 공실을 넉넉히 잡는 편이 안전합니다.

## 사례로 보는 실질 수익률 계산 💰

매매가 2억 원, 보증금 1,000만 원, 월세 80만 원인 오피스텔을 대출 없이 산다고 가정해 보겠습니다. 연간 비용(재산세·수선비·보험)은 50만 원, 공실은 연 1개월로 잡았습니다.

1단계: 표면 수익률 = 960만 ÷ (2억 − 1,000만) = 960만 ÷ 1억 9,000만 = 5.05%

2단계: 실질 순수익 = 960만 − 50만 − 80만(공실 1개월) = 830만 원

3단계: 실투자금 = 2억 − 1,000만 + 1,020만(부대비용 5.1%) = 2억 20만 원

4단계: 실질 수익률 = 830만 ÷ 2억 20만 = 4.15%

표면 수익률 5.05%가 비용을 넣자 4.15%로 0.9%포인트 내려갔습니다. 임대소득세까지 따지면 세후 수익률은 더 내려갑니다. 주거용으로 임대하면 주택임대소득 과세 기준을 따르니 [주택임대소득세 계산법](/2026/11/04/housing-rental-income-tax-calculation/)을 함께 확인하시기 바랍니다.

## 대출 레버리지, 금리가 수익률을 넘으면 손해 ⚖️

같은 오피스텔을 1억 원 대출을 끼고 산다면 내 돈은 1억 20만 원으로 줄어듭니다. 결과는 대출 금리에 따라 정반대로 갈립니다.

| 조건 | 연 이자 | 이자 차감 순수익 | 내 돈(실투자금) | 수익률 | 월 현금흐름 |
|---|---|---|---|---|---|
| 대출 없음 | 0원 | 830만 원 | 2억 20만 원 | 4.15% | 약 69만 원 |
| 1억 원, 금리 3.5% | 350만 원 | 480만 원 | 1억 20만 원 | 4.79% | 약 40만 원 |
| 1억 원, 금리 4.5% | 450만 원 | 380만 원 | 1억 20만 원 | 3.79% | 약 32만 원 |
| 1억 4,000만 원, 금리 4.5% | 630만 원 | 200만 원 | 6,020만 원 | 3.32% | 약 17만 원 |

금리 3.5%일 때는 대출이 수익률을 4.15%에서 4.79%로 끌어올리지만, 4.5%에서는 오히려 3.79%로 끌어내립니다. 대출을 1억 4,000만 원까지 늘리면 3.32%까지 떨어집니다. 갈림길이 되는 금리는 대출 없는 실질 수익률(이 사례에서는 약 4.15%)입니다. 대출 금리가 이보다 낮으면 레버리지가 득이 되고, 높으면 빌린 돈이 많을수록 손해가 커집니다.

표의 월 현금흐름은 이자만 낸다고 가정한 값입니다. 원리금을 함께 갚으면 매달 손에 쥐는 돈은 더 줄어듭니다. 상환 방식별 차이는 [주담대 상환방식 비교](/2026/10/14/mortgage-repayment-methods-calculation/)에서 계산해 볼 수 있습니다.

## 광고 수익률을 다시 계산해 보는 법 🔍

"수익률 5% 이상 보장" 같은 분양 광고는 대개 대출을 최대로 받았다고 가정한 뒤 취득세·공실은 그대로 두고 대출이자만 차감해 계산합니다. 위 사례를 이 방식으로 계산하면 (960만 − 450만) ÷ (2억 − 1,000만 − 1억) = 510만 ÷ 9,000만 = 5.67%가 나옵니다. 비용을 모두 넣은 3.79%보다 1.9%포인트 가까이 높습니다.

광고 숫자를 보면 아래 네 가지를 차례로 확인해 보시기 바랍니다.

- 분모에 취득세 4.6%와 중개보수가 들어갔는가
- 공실 기간을 몇 개월로 잡았는가(0개월이면 비현실적)
- 대출 금리를 지금 실제로 받을 수 있는 금리로 넣었는가
- 월세가 주변 실거래 시세와 맞는가, 분양 초기 임대 보장 기간 이후에도 유지될 수 있는가

## 목표 수익률로 적정 매수가 거꾸로 구하기 🎯

공식을 뒤집으면 원하는 수익률에 맞는 매수가도 구할 수 있습니다. 부대비용률을 c, 목표 실질 수익률을 y라고 하면 적정 매수가 = (실질 순수익 ÷ y + 보증금) ÷ (1 + c)입니다.

| 목표 실질 수익률 | 적정 매수가(사례 기준) |
|---|---|
| 4.5% | 약 1억 8,501만 원 |
| 5.0% | 약 1억 6,746만 원 |
| 6.0% | 약 1억 4,114만 원 |

사례 오피스텔로 실질 5%를 내려면 호가 2억 원보다 3,000만 원 이상 낮게 사야 합니다. 매도 호가를 협상할 때 기준선으로 쓰기 좋습니다.

## 임대수익률 계산기 🔢

매매가·보증금·월세와 비용, 대출 조건을 넣으면 표면·실질·레버리지 수익률과 손익분기 금리를 한 번에 계산합니다. 금액은 만 원 단위입니다.

{% raw %}
<div class="ryc" id="ryc">
  <style>
    .ryc { border: 1px solid #e2e2e2; border-radius: 12px; padding: 20px; margin: 8px 0 4px; background: #fafafa; }
    .ryc .ryc__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px 18px; }
    .ryc .ryc__label { display: block; font-size: 13px; color: #555; margin-bottom: 4px; }
    .ryc .ryc__field { width: 100%; box-sizing: border-box; height: 38px; padding: 0 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; background: #fff; color: #222; }
    .ryc .ryc__table { width: 100%; border-collapse: collapse; margin-top: 18px; background: #fff; font-size: 14px; color: #222; }
    .ryc .ryc__th, .ryc .ryc__td { border-bottom: 1px solid #ececec; padding: 9px 10px; text-align: left; }
    .ryc .ryc__td--num { text-align: right; font-variant-numeric: tabular-nums; }
    .ryc .ryc__final { background: #eef4ff; border: 1px solid #cdddff; border-radius: 12px; padding: 16px 18px; margin-top: 14px; }
    .ryc .ryc__final-label { font-size: 13px; color: #1b4fa0; }
    .ryc .ryc__final-value { font-size: 24px; font-weight: 700; color: #1b4fa0; margin-top: 2px; }
    .ryc .ryc__note { font-size: 12px; color: #777; margin-top: 12px; line-height: 1.5; }
  </style>
  <form class="ryc__form" id="ryc-form" onsubmit="return false;">
    <div class="ryc__grid">
      <div class="ryc__item"><label class="ryc__label" for="ryc-price">매매가(만 원)</label><input class="ryc__field" id="ryc-price" type="number" min="0" step="100" value="20000" inputmode="numeric"></div>
      <div class="ryc__item"><label class="ryc__label" for="ryc-deposit">보증금(만 원)</label><input class="ryc__field" id="ryc-deposit" type="number" min="0" step="100" value="1000" inputmode="numeric"></div>
      <div class="ryc__item"><label class="ryc__label" for="ryc-rent">월세(만 원)</label><input class="ryc__field" id="ryc-rent" type="number" min="0" step="1" value="80" inputmode="numeric"></div>
      <div class="ryc__item"><label class="ryc__label" for="ryc-acq">취득 부대비용률(%)</label><input class="ryc__field" id="ryc-acq" type="number" min="0" step="0.1" value="5.1" inputmode="decimal"></div>
      <div class="ryc__item"><label class="ryc__label" for="ryc-cost">연간 비용(만 원)</label><input class="ryc__field" id="ryc-cost" type="number" min="0" step="1" value="50" inputmode="numeric"></div>
      <div class="ryc__item"><label class="ryc__label" for="ryc-vacancy">공실 기간</label><select class="ryc__field" id="ryc-vacancy"><option value="0">없음</option><option value="1" selected>연 1개월</option><option value="2">연 2개월</option><option value="3">연 3개월</option></select></div>
      <div class="ryc__item"><label class="ryc__label" for="ryc-loan">대출금(만 원)</label><input class="ryc__field" id="ryc-loan" type="number" min="0" step="100" value="10000" inputmode="numeric"></div>
      <div class="ryc__item"><label class="ryc__label" for="ryc-rate">대출 금리(연 %)</label><input class="ryc__field" id="ryc-rate" type="number" min="0" step="0.1" value="4.5" inputmode="decimal"></div>
    </div>
  </form>
  <table class="ryc__table">
    <caption class="ryc__note">계산 결과</caption>
    <tbody>
      <tr><th class="ryc__th" scope="row">표면 수익률</th><td class="ryc__td ryc__td--num" id="ryc-gross">-</td></tr>
      <tr><th class="ryc__th" scope="row">실질 수익률(대출 없음)</th><td class="ryc__td ryc__td--num" id="ryc-net">-</td></tr>
      <tr><th class="ryc__th" scope="row">실투자금(대출 차감 후)</th><td class="ryc__td ryc__td--num" id="ryc-equity">-</td></tr>
      <tr><th class="ryc__th" scope="row">연 대출이자</th><td class="ryc__td ryc__td--num" id="ryc-interest">-</td></tr>
      <tr><th class="ryc__th" scope="row">월 현금흐름(이자만 납부 가정)</th><td class="ryc__td ryc__td--num" id="ryc-cash">-</td></tr>
      <tr><th class="ryc__th" scope="row">손익분기 금리</th><td class="ryc__td ryc__td--num" id="ryc-breakeven">-</td></tr>
    </tbody>
  </table>
  <div class="ryc__final">
    <div class="ryc__final-label">대출 반영 실질 수익률(내 돈 기준)</div>
    <div class="ryc__final-value" id="ryc-total" aria-live="polite">-</div>
  </div>
  <p class="ryc__note" id="ryc-msg" aria-live="polite"></p>
  <p class="ryc__note">임대소득세·양도차익은 반영하지 않았습니다. 손익분기 금리는 대출 없는 실질 수익률과 같으며, 대출 금리가 이보다 높으면 대출이 수익률을 낮춥니다.</p>
</div>
<script>
  (function () {
    var ids = ['ryc-price', 'ryc-deposit', 'ryc-rent', 'ryc-acq', 'ryc-cost', 'ryc-vacancy', 'ryc-loan', 'ryc-rate'];
    function num(id) { var v = parseFloat(document.getElementById(id).value); return isFinite(v) && v > 0 ? v : 0; }
    function won(v) { return Math.round(v).toLocaleString('ko-KR') + '만 원'; }
    function pct(v) { return (Math.round(v * 100) / 100).toFixed(2) + '%'; }
    function set(id, t) { document.getElementById(id).textContent = t; }
    function calc() {
      var price = num('ryc-price'), deposit = num('ryc-deposit'), rent = num('ryc-rent');
      var acq = num('ryc-acq') / 100, cost = num('ryc-cost'), vacancy = num('ryc-vacancy');
      var loan = num('ryc-loan'), rate = num('ryc-rate') / 100;
      var annual = rent * 12;
      var noi = annual - cost - rent * vacancy;
      var base = price - deposit + price * acq;
      var equity = base - loan;
      var interest = loan * rate;
      var msg = '';
      set('ryc-gross', price - deposit > 0 ? pct(annual / (price - deposit) * 100) : '-');
      set('ryc-net', base > 0 ? pct(noi / base * 100) : '-');
      set('ryc-equity', won(equity));
      set('ryc-interest', won(interest));
      set('ryc-cash', won((noi - interest) / 12));
      set('ryc-breakeven', base > 0 ? pct(noi / base * 100) : '-');
      if (equity <= 0) {
        set('ryc-total', '-');
        msg = '대출금과 보증금이 매수 비용보다 커서 내 돈 기준 수익률을 계산할 수 없습니다.';
      } else {
        set('ryc-total', pct((noi - interest) / equity * 100));
        if (loan > 0 && base > 0) {
          msg = rate * 100 > noi / base * 100 ? '대출 금리가 손익분기 금리보다 높아 대출이 수익률을 낮추고 있습니다.' : '대출 금리가 손익분기 금리보다 낮아 대출이 수익률을 높이고 있습니다.';
        }
      }
      set('ryc-msg', msg);
    }
    for (var i = 0; i < ids.length; i++) {
      document.getElementById(ids[i]).addEventListener('input', calc);
      document.getElementById(ids[i]).addEventListener('change', calc);
    }
    calc();
  })();
</script>
{% endraw %}

## 총평 📊

임대수익률은 공식보다 무엇을 넣고 빼느냐가 중요합니다. 오피스텔은 취득세 4.6%만으로도 수익률이 0.2%포인트 안팎 깎이고, 공실 한 달마다 0.4%포인트 안팎이 더 빠집니다. 한국부동산원 집계로 2026년 3분기 전국 오피스텔 수익률은 5.90%였지만, 개별 매물은 비용과 공실을 모두 넣으면 이보다 낮아지는 경우가 많습니다. 대출을 낄 때는 내 매물의 실질 수익률과 대출 금리를 먼저 비교해 보고, 금리가 더 높다면 대출 비중을 줄이거나 매수가를 낮추는 쪽으로 계산을 다시 해 보시길 권합니다.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

## 출처 📚

- [오피스텔 투자 가이드: 수익률 계산과 세금 — glasswallet](https://glasswallet.com/blog/officetel-investment-guide)
- [오피스텔 임대수익률 계산법 — houseinfo](https://houseinfo.kr/blog/0179-officetel-rental-yield-2025/)
- [오피스텔 취득세·재산세 계산법 — houseinfo](https://houseinfo.kr/blog/0178-officetel-tax-calculation/)
- [임대수익률 계산기 — 더체크](https://thecheck.co.kr/calculators/rental-yield/)
- [수익형 부동산 수익률의 함정 — 이코노미스트(2017.5.28)](https://economist.co.kr/article/view/ecn201705280001)
- [올 3분기 서울 오피스텔, 매매 상승 폭 꺾이고 월세는 1% 뛰어 — SBS Biz(2026.10.15)](https://biz.sbs.co.kr/amp/article/20000340147)
- [3분기 오피스텔 가격동향 — 스마트투데이(2026.10.15)](https://www.smarttoday.co.kr/ko-kr/articles/112727)
