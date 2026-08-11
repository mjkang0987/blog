---
layout: post
title: "부동산 중개보수 계산법 총정리 — 매매·전세·월세 구간별 상한요율과 복비 계산기 🏠"
date: 2026-08-12 07:00:00 +0900
lang: ko
permalink: /2026/08/12/brokerage-commission-calculation/
page_id: 2026-08-12-brokerage-commission-calculation
image: /assets/og/2026-08-12-brokerage-commission-calculation-ko.png
summary: "부동산 중개보수(복비)는 거래금액에 구간별 상한요율을 곱한 금액 안에서 중개인과 협의해 정하며, 낮은 구간에는 한도액이 따로 있습니다. 주택 매매·전세·월세와 오피스텔·상가별 요율표, 월세 거래금액 환산법, 실전 계산 예시와 계산기를 한 번에 정리했습니다."
description: "부동산 중개보수(복비) 계산법을 매매·전세·월세 구간별 상한요율표와 계산기로 정리했습니다. 거래금액별 한도액과 부가세·협의 요령까지 확인하세요."
categories: [부동산]
tags: [중개보수, 부동산복비, 중개수수료, 복비계산, 중개보수계산기, 상한요율, 부동산수수료, 매매중개보수, 전세중개보수, 월세중개보수, 오피스텔중개보수, 공인중개사법, 한도액, 부동산거래비용, 중개보수요율표]
---

**핵심 요약 (TL;DR)**

- 중개보수는 '거래금액 × 구간별 상한요율' 이내에서 중개인과 협의해 정하며, 상한요율과 한도액을 넘을 수 없습니다.
- 주택 매매는 6단계(0.6%→0.4%→0.7%), 임대차는 6단계(0.5%→0.3%→0.6%)로 나뉘고, 낮은 두 구간에만 한도액이 붙습니다.
- 월세는 '보증금 + 월차임 × 100'을 거래금액으로 보며, 이 값이 5,000만원 미만이면 곱셈 배수가 70으로 낮아집니다. 부가가치세는 별도입니다.

집을 사거나 전셋집을 구할 때 마지막에 마주치는 비용이 부동산 중개보수, 흔히 '복비'입니다. 중개보수는 정해진 정액이 아니라 **거래금액에 구간별 상한요율을 곱한 상한선 안에서 협의로 정하는 금액**입니다. 상한요율은 「공인중개사법 시행규칙」과 각 시·도 조례에 정해져 있어서, 이 표만 알면 내가 낼 복비의 최대치를 직접 계산해 볼 수 있습니다.

아래 계산기에 거래금액만 넣으면 적용 구간과 상한 중개보수가 바로 나옵니다. 이어지는 요율표와 예시를 보면 계산 원리까지 확인하실 수 있습니다.

{% raw %}
<div class="broker-calc" id="broker-calc">
  <style>
    .broker-calc { border: 1px solid #e2e2e2; border-radius: 12px; padding: 20px; margin: 8px 0 4px; background: #fafafa; }
    .broker-calc .broker-calc__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px 18px; }
    .broker-calc .broker-calc__label { display: block; font-size: 13px; color: #555; margin-bottom: 4px; }
    .broker-calc .broker-calc__field { width: 100%; box-sizing: border-box; height: 38px; padding: 0 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; background: #fff; }
    .broker-calc .broker-calc__hint { font-size: 12px; color: #1b4fa0; margin-top: 4px; min-height: 16px; }
    .broker-calc .broker-calc__cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 18px; align-items: start; }
    .broker-calc .broker-calc__card { background: #fff; border: 1px solid #ececec; border-radius: 8px; padding: 14px; }
    .broker-calc .broker-calc__card-label { font-size: 13px; color: #666; }
    .broker-calc .broker-calc__card-value { font-size: 18px; font-weight: 600; margin-top: 4px; }
    .broker-calc .broker-calc__card-sub { font-size: 12px; color: #999; margin-top: 2px; }
    .broker-calc .broker-calc__final { background: #eef4ff; border: 1px solid #cdddff; border-radius: 12px; padding: 16px 18px; margin-top: 14px; }
    .broker-calc .broker-calc__final-label { font-size: 13px; color: #1b4fa0; }
    .broker-calc .broker-calc__final-value { font-size: 26px; font-weight: 700; color: #1b4fa0; margin-top: 2px; }
    .broker-calc .broker-calc__final-sub { font-size: 12px; color: #5a78ad; margin-top: 4px; }
    .broker-calc .broker-calc__note { font-size: 12px; color: #888; margin-top: 12px; line-height: 1.6; }
  </style>

  <div class="broker-calc__grid">
    <div>
      <label class="broker-calc__label" for="broker-type">물건 유형</label>
      <select class="broker-calc__field" id="broker-type">
        <option value="house">주택 (아파트·빌라·단독 등)</option>
        <option value="offi-small">오피스텔 (전용 85㎡ 이하·설비 요건 충족)</option>
        <option value="etc">그 밖의 부동산 (그 외 오피스텔·상가·토지)</option>
      </select>
    </div>
    <div>
      <label class="broker-calc__label" for="broker-deal">거래 유형</label>
      <select class="broker-calc__field" id="broker-deal">
        <option value="sale">매매·교환</option>
        <option value="jeonse">전세</option>
        <option value="wolse">월세</option>
      </select>
    </div>
  </div>

  <div class="broker-calc__grid" style="margin-top:14px;">
    <div id="broker-amount-wrap">
      <label class="broker-calc__label" for="broker-amount">거래금액 (만원)</label>
      <input class="broker-calc__field" type="number" id="broker-amount" value="50000" min="0" step="1000">
      <div class="broker-calc__hint" id="broker-amount-hint"></div>
    </div>
    <div id="broker-deposit-wrap" style="display:none;">
      <label class="broker-calc__label" for="broker-deposit">보증금 (만원)</label>
      <input class="broker-calc__field" type="number" id="broker-deposit" value="10000" min="0" step="100">
    </div>
    <div id="broker-rent-wrap" style="display:none;">
      <label class="broker-calc__label" for="broker-rent">월차임 (만원)</label>
      <input class="broker-calc__field" type="number" id="broker-rent" value="50" min="0" step="1">
    </div>
    <div>
      <label class="broker-calc__label" for="broker-nego">협의 요율 (%, 선택)</label>
      <input class="broker-calc__field" type="number" id="broker-nego" placeholder="비우면 상한요율 적용" min="0" step="0.01">
    </div>
  </div>

  <div class="broker-calc__cards">
    <div class="broker-calc__card">
      <div class="broker-calc__card-label">적용 거래금액</div>
      <div class="broker-calc__card-value" id="broker-base">–</div>
      <div class="broker-calc__card-sub" id="broker-base-sub"></div>
    </div>
    <div class="broker-calc__card">
      <div class="broker-calc__card-label">적용 상한요율</div>
      <div class="broker-calc__card-value" id="broker-rate">–</div>
      <div class="broker-calc__card-sub" id="broker-cap"></div>
    </div>
  </div>

  <div class="broker-calc__final" aria-live="polite">
    <div class="broker-calc__final-label">예상 중개보수 (부가세 별도)</div>
    <div class="broker-calc__final-value" id="broker-fee">–</div>
    <div class="broker-calc__final-sub" id="broker-fee-sub"></div>
  </div>

  <p class="broker-calc__note">서울특별시 주택 중개보수 조례(2021.12.30 시행)와 「공인중개사법 시행규칙」 상한요율 기준 추정치입니다. 실제 요율은 시·도 조례로 정해져 지역마다 다를 수 있고, 최종 금액은 상한 이내에서 중개인과 협의해 결정됩니다. 부가가치세는 별도이며, 원 단위는 반올림했습니다.</p>

  <script>
  (function(){
    var el = function(id){ return document.getElementById(id); };
    function won(v){ return Math.round(v).toLocaleString() + "원"; }
    function brief(v){
      v = Math.round(v);
      if(v >= 10000 && v % 10000 === 0){ return (v / 10000).toLocaleString() + "만원"; }
      if(v >= 10000){ return "약 " + Math.round(v / 10000).toLocaleString() + "만원"; }
      return v.toLocaleString() + "원";
    }
    function eokMan(v){
      v = Math.round(v);
      var eok = Math.floor(v / 100000000);
      var man = Math.round((v % 100000000) / 10000);
      var out = "";
      if(eok > 0){ out += eok + "억"; }
      if(man > 0){ out += (out ? " " : "") + man.toLocaleString() + "만원"; }
      return out || "0원";
    }
    var houseSale = [
      [50000000, 0.6, 250000],
      [200000000, 0.5, 800000],
      [900000000, 0.4, 0],
      [1200000000, 0.5, 0],
      [1500000000, 0.6, 0],
      [Infinity, 0.7, 0]
    ];
    var houseRent = [
      [50000000, 0.5, 200000],
      [100000000, 0.4, 300000],
      [600000000, 0.3, 0],
      [1200000000, 0.4, 0],
      [1500000000, 0.5, 0],
      [Infinity, 0.6, 0]
    ];
    function pickBracket(table, base){
      for(var i = 0; i < table.length; i++){
        if(base < table[i][0]){ return { rate: table[i][1], cap: table[i][2] }; }
      }
      return { rate: table[table.length - 1][1], cap: 0 };
    }
    function toggleFields(){
      var deal = el("broker-deal").value;
      var wolse = deal === "wolse";
      el("broker-amount-wrap").style.display = wolse ? "none" : "block";
      el("broker-deposit-wrap").style.display = wolse ? "block" : "none";
      el("broker-rent-wrap").style.display = wolse ? "block" : "none";
    }
    function calc(){
      var type = el("broker-type").value;
      var deal = el("broker-deal").value;
      var base, baseNote = "";
      if(deal === "wolse"){
        var deposit = (+el("broker-deposit").value || 0) * 10000;
        var rent = (+el("broker-rent").value || 0) * 10000;
        base = deposit + rent * 100;
        if(base < 50000000){ base = deposit + rent * 70; baseNote = "5천만원 미만이라 월차임 × 70 적용"; }
        else { baseNote = "보증금 + 월차임 × 100"; }
      } else {
        base = (+el("broker-amount").value || 0) * 10000;
      }

      var rate, cap = 0, rateLabel;
      if(type === "house"){
        var b = pickBracket(deal === "sale" ? houseSale : houseRent, base);
        rate = b.rate; cap = b.cap;
      } else if(type === "offi-small"){
        rate = deal === "sale" ? 0.5 : 0.4;
      } else {
        rate = 0.9;
      }
      rateLabel = rate + "%";

      var negoRaw = el("broker-nego").value;
      var effRate = rate;
      if(negoRaw !== "" && !isNaN(parseFloat(negoRaw))){
        var nego = parseFloat(negoRaw);
        if(nego >= 0 && nego < rate){ effRate = nego; }
      }

      var fee = base * effRate / 100;
      if(cap > 0 && fee > cap){ fee = cap; }

      el("broker-base").textContent = eokMan(base);
      el("broker-base-sub").textContent = baseNote;
      el("broker-rate").textContent = rateLabel + (effRate < rate ? " (협의 " + effRate + "% 적용)" : "");
      el("broker-cap").textContent = cap > 0 ? "한도액 " + brief(cap) : "한도액 없음";
      el("broker-fee").textContent = brief(fee);
      el("broker-fee-sub").textContent = won(fee) + (cap > 0 && Math.round(base * effRate / 100) > cap ? " · 한도액이 적용됐습니다" : "");
    }
    var ids = ["broker-type", "broker-deal", "broker-amount", "broker-deposit", "broker-rent", "broker-nego"];
    ids.forEach(function(id){
      var node = el(id);
      node.addEventListener("input", calc);
      node.addEventListener("change", calc);
    });
    el("broker-deal").addEventListener("change", toggleFields);
    toggleFields();
    calc();
  })();
  </script>
</div>
{% endraw %}

## 🧾 중개보수는 어떻게 정해질까

중개보수를 구하는 공식은 간단합니다. **중개보수 = 거래금액 × 상한요율**이고, 이렇게 나온 금액을 넘지 않는 선에서 의뢰인과 개업공인중개사가 협의해 정합니다. 상한요율은 거래금액이 커질수록 구간별로 달라지며, 금액이 작은 일부 구간에는 '한도액'이라는 상한이 하나 더 붙습니다.

여기서 두 가지를 구분해야 합니다. 첫째, 상한요율은 말 그대로 '최대치'입니다. 실제로는 그보다 낮은 요율로 협의할 수 있고, 중개인이 상한요율을 무조건 다 받아야 하는 것도 아닙니다. 둘째, 요율은 지역별 조례로 정해집니다. 아래 표는 서울특별시 조례와 시행규칙의 상한요율을 기준으로 삼았습니다. 대부분의 지역이 같은 구조를 따르지만, 계약 전에는 해당 시·도 조례나 중개사무소에 게시된 요율표를 확인해 보는 편이 정확합니다.

## 🏠 주택 매매·교환 상한요율

주택 매매는 2021년 개정으로 거래금액 구간이 5단계에서 6단계로 세분화됐습니다. 특히 9억원 이상 고가 구간이 하나의 높은 요율(과거 0.9%)에서 세 단계로 나뉘었는데, 9억~12억원은 오히려 요율이 낮아진 반면 15억원 이상은 0.7%까지 올라갑니다.

| 거래금액 | 상한요율 | 한도액 |
| --- | --- | --- |
| 5,000만원 미만 | 0.6% | 25만원 |
| 5,000만원 이상 ~ 2억원 미만 | 0.5% | 80만원 |
| 2억원 이상 ~ 9억원 미만 | 0.4% | 없음 |
| 9억원 이상 ~ 12억원 미만 | 0.5% | 없음 |
| 12억원 이상 ~ 15억원 미만 | 0.6% | 없음 |
| 15억원 이상 | 0.7% | 없음 |

예를 들어 6억원짜리 아파트를 매매하면 2억~9억원 구간이라 상한요율 0.4%가 적용돼 최대 240만원입니다. 10억원이면 9억~12억원 구간(0.5%)으로 넘어가 최대 500만원, 15억원이면 0.7%가 적용돼 최대 1,050만원까지 올라갑니다. 9억원·12억원·15억원 경계에서 요율이 한 단계씩 뛰기 때문에, 거래금액이 경계에 가까울수록 실제 부담이 크게 달라집니다.

## 📄 주택 임대차(전세·월세) 상한요율

전세와 월세 같은 임대차 거래에는 매매보다 한 단계씩 낮은 요율이 적용됩니다. 구간은 마찬가지로 6단계이고, 5,000만원 미만과 1억원 미만 구간에만 한도액이 있습니다.

| 거래금액 | 상한요율 | 한도액 |
| --- | --- | --- |
| 5,000만원 미만 | 0.5% | 20만원 |
| 5,000만원 이상 ~ 1억원 미만 | 0.4% | 30만원 |
| 1억원 이상 ~ 6억원 미만 | 0.3% | 없음 |
| 6억원 이상 ~ 12억원 미만 | 0.4% | 없음 |
| 12억원 이상 ~ 15억원 미만 | 0.5% | 없음 |
| 15억원 이상 | 0.6% | 없음 |

전세보증금이 3억원이면 1억~6억원 구간(0.3%)이라 최대 90만원, 5억원이면 같은 구간이라 최대 150만원입니다. 임대차는 1억~6억원 구간이 0.3%로 넓게 잡혀 있어서, 서울 평균 전세가 수준의 거래는 대부분 이 구간에 들어갑니다.

## 💰 월세는 거래금액부터 환산해야 합니다

월세는 보증금과 매달 내는 차임이 함께 있어 거래금액을 먼저 환산해야 합니다. 기준은 **보증금 + (월차임 × 100)**입니다. 다만 이렇게 계산한 금액이 5,000만원 미만이면 배수를 낮춰 **보증금 + (월차임 × 70)**으로 다시 계산합니다.

| 계약 조건 | 환산 거래금액 | 적용 구간·요율 | 상한 중개보수 |
| --- | --- | --- | --- |
| 보증금 1억 / 월세 50만원 | 1억 + 5,000만 = 1억 5,000만원 | 1억~6억(0.3%) | 45만원 |
| 보증금 3,000만 / 월세 40만원 | 3,000만 + 4,000만 = 7,000만원 | 5천만~1억(0.4%) | 28만원 |
| 보증금 500만 / 월세 40만원 | (환산 4,500만<5천만) 500만 + 2,800만 = 3,300만원 | 5천만 미만(0.5%·한도 20만) | 16만 5,000원 |

세 번째 사례처럼 처음 계산한 값이 5,000만원 미만이면 곱하는 배수가 70으로 낮아져 거래금액이 더 작아집니다. 소액 월세 세입자의 부담을 줄이기 위한 장치입니다.

## 🏢 오피스텔·상가 등 주택 외 요율

오피스텔은 요건에 따라 요율이 크게 갈립니다. 전용면적 85㎡ 이하이면서 전용 입식 부엌·수세식 화장실·목욕시설 등을 갖춰 주거용으로 쓰기 적합하면 낮은 요율이 적용되고, 그 밖의 오피스텔이나 상가·토지 같은 비주택에는 일률적으로 0.9%가 적용됩니다.

| 대상 | 거래 유형 | 상한요율 |
| --- | --- | --- |
| 오피스텔 (전용 85㎡ 이하·설비 요건 충족) | 매매·교환 | 0.5% |
| 오피스텔 (전용 85㎡ 이하·설비 요건 충족) | 임대차 등 | 0.4% |
| 그 밖의 오피스텔·상가·토지 등 | 매매·교환·임대차 등 | 0.9% |

주거용 오피스텔인지 아닌지에 따라 요율이 최대 두 배 가까이 차이 나므로, 오피스텔은 계약 전에 전용면적과 설비 요건을 충족하는지 확인해 두는 것이 좋습니다.

## 🧮 실전 계산 예시

앞의 요율표를 실제 금액에 적용하면 다음과 같습니다. 모두 상한요율 기준 최대 금액이며, 부가가치세는 별도입니다.

| 거래 | 거래금액 | 구간·요율 | 상한 중개보수 |
| --- | --- | --- | --- |
| 아파트 매매 | 6억원 | 2억~9억(0.4%) | 240만원 |
| 아파트 매매 | 10억원 | 9억~12억(0.5%) | 500만원 |
| 아파트 매매 | 15억원 | 15억 이상(0.7%) | 1,050만원 |
| 전세 | 3억원 | 1억~6억(0.3%) | 90만원 |
| 전세 | 8억원 | 6억~12억(0.4%) | 320만원 |
| 상가 임대차 | 2억원 | 비주택(0.9%) | 180만원 |

같은 매매라도 6억원과 10억원 사이에서 중개보수가 240만원에서 500만원으로 두 배 넘게 뛰는데, 요율이 0.4%에서 0.5%로 오르는 동시에 거래금액 자체가 커지기 때문입니다.

## ✅ 계약 전 확인해야 할 것들

중개보수에서 자주 놓치는 부분을 정리하면 이렇습니다. 상한요율은 최대치일 뿐이라 계약 전에 요율을 협의할 수 있고, 특히 고가 구간일수록 협의 여지가 있습니다. 중개보수에는 부가가치세가 별도로 붙는데, 일반과세 사업자인 중개사무소는 10%, 간이과세자는 그보다 낮은 세율이 더해질 수 있습니다. 또 한 건물에 주택과 상가가 섞여 있으면 주택 면적이 전체의 2분의 1 이상일 때는 주택 요율을, 미만일 때는 주택 외 요율을 적용합니다. 분양권은 계약 당시까지 낸 금액(융자 포함)에 프리미엄을 더한 값을 거래금액으로 봅니다.

지급 시기는 중개인과의 약정에 따르되, 약정이 없으면 거래대금 지급이 완료된 날로 합니다. 중개보수는 계약이 정상적으로 성사된 데 대한 대가이므로, 계약을 앞두고 요율·금액·부가세 포함 여부를 미리 서면으로 확인해 두면 분쟁을 예방할 수 있습니다.

## 📝 총평

부동산 중개보수는 겉으로는 복잡해 보여도 '거래금액 × 구간별 상한요율, 그 안에서 협의'라는 한 문장으로 요약됩니다. 매매는 6단계, 임대차는 그보다 한 단계 낮은 6단계 요율을 기억해 두고, 월세는 보증금과 월차임을 환산해 거래금액부터 구하면 누구나 자기 복비의 상한을 계산할 수 있습니다. 요율은 지역 조례로 정해지므로 계약 전에 해당 시·도 기준과 중개사무소 게시 요율표를 확인하고, 상한선 안에서 합리적으로 협의하시길 권합니다.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

**출처**

- [서울특별시 서울부동산정보광장 — 부동산 중개보수 요율표](https://land.seoul.go.kr/land/broker/brokerageCommission.do)
- [찾기쉬운 생활법령정보 — 부동산 중개보수 산정](https://www.easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=649&ccfNo=2&cciNo=2&cnpClsNo=2)
- [국토교통부 부동산거래 전자계약시스템 — 중개보수 요율표](https://irts.molit.go.kr/com/cmn/popup/fee/rtecsFeeRtoPopup.do)
