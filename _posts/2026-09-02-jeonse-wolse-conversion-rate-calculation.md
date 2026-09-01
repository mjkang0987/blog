---
layout: post
title: "전월세 전환율 계산법과 법정 상한(기준금리+2%) 총정리 🏠"
date: 2026-09-02 07:00:00 +0900
lang: ko
permalink: /2026/09/02/jeonse-wolse-conversion-rate-calculation/
page_id: 2026-09-02-jeonse-wolse-conversion-rate-calculation
image: /assets/og/2026-09-02-jeonse-wolse-conversion-rate-calculation-ko.png
summary: "전월세 전환율은 '(월세 × 12) ÷ (전세보증금 − 전환 후 보증금) × 100'으로 계산하며, 법정 상한은 '기준금리 + 2%'와 '연 10%' 중 낮은 쪽입니다. 기준금리가 연 3.00%인 2026년 9월 현재 상한은 연 5.0%로, 계산 공식과 법적 근거, 계산기를 함께 정리했습니다."
description: "전월세 전환율 계산법과 법정 상한(기준금리+2%)을 계산기와 함께 정리했습니다. 전세를 월세로, 월세를 전세로 바꿀 때 월세와 환산보증금을 확인하세요."
categories: [부동산]
tags: [전월세전환율, 전월세전환율계산, 전세월세전환, 월세전세환산, 주택임대차보호법, 전환율상한, 법정전환율, 기준금리, 계약갱신요구권, 임대차, 보증금, 월세계산, 전세보증금, 임대료계산, 렌트홈]
---

**핵심 요약 (TL;DR)**

- 전월세 전환율은 '(월세 × 12) ÷ (전세보증금 − 전환 후 보증금) × 100'으로 계산하며, 전세를 월세로 바꿀 때 전환하는 보증금에 이 비율을 곱해 12로 나누면 월세가 나옵니다.
- 법으로 정한 상한은 '한국은행 기준금리 + 연 2%'와 '연 10%' 중 낮은 쪽이며, 기준금리가 연 3.00%인 2026년 9월 현재 상한은 연 5.0%입니다.
- 이 상한은 계약 기간 중 전환이나 계약갱신요구권 행사 때만 강제되고, 새로 맺는 신규 계약에는 적용되지 않습니다.

전세를 월세로 돌리거나 반대로 월세를 전세로 환산할 때 기준이 되는 값이 전월세 전환율입니다. 쉽게 말해 **보증금과 월세를 서로 바꿀 때 적용하는 연이율로, '(월세 × 12) ÷ (전세보증금 − 전환 후 보증금) × 100' 공식으로 구하며, 법정 상한은 기준금리에 2%를 더한 값과 연 10% 중 낮은 쪽입니다.** 기준금리가 연 3.00%인 지금은 상한이 연 5.0%입니다.

아래 계산기에 전세보증금과 전환 후 남길 보증금, 전환율만 넣으면 예상 월세가 바로 나오고, 반대로 월세를 전세보증금으로 환산할 수도 있습니다. 이어지는 설명에서 공식과 법적 근거, 실제 적용 방법까지 짚어 보겠습니다. 💡

{% raw %}
<div class="jwc-calc" id="jwc-calc">
  <style>
    .jwc-calc { border: 1px solid #e2e2e2; border-radius: 12px; padding: 20px; margin: 8px 0 4px; background: #fafafa; }
    .jwc-calc .jwc-calc__modes { display: flex; gap: 18px; margin-bottom: 16px; flex-wrap: wrap; }
    .jwc-calc .jwc-calc__mode { font-size: 14px; color: #333; }
    .jwc-calc .jwc-calc__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px 18px; }
    .jwc-calc .jwc-calc__label { display: block; font-size: 13px; color: #555; margin-bottom: 4px; }
    .jwc-calc .jwc-calc__input { width: 100%; box-sizing: border-box; padding: 9px 11px; font-size: 15px; border: 1px solid #ccc; border-radius: 8px; }
    .jwc-calc .jwc-calc__hint { font-size: 12px; color: #0a7d33; margin-top: 5px; min-height: 16px; }
    .jwc-calc .jwc-calc__result { margin-top: 18px; padding: 16px; background: #fff; border: 1px solid #e2e2e2; border-radius: 10px; }
    .jwc-calc .jwc-calc__row { display: flex; justify-content: space-between; align-items: baseline; padding: 6px 0; border-bottom: 1px dashed #eee; }
    .jwc-calc .jwc-calc__row:last-child { border-bottom: none; }
    .jwc-calc .jwc-calc__key { font-size: 13px; color: #666; }
    .jwc-calc .jwc-calc__val { font-size: 17px; font-weight: 700; color: #111; }
    .jwc-calc .jwc-calc__sub { font-size: 12px; color: #888; margin-top: 8px; }
    .jwc-calc .jwc-hidden { display: none; }
  </style>

  <fieldset class="jwc-calc__modes" id="jwc-modes">
    <label class="jwc-calc__mode"><input type="radio" name="jwc-mode" value="j2w" checked> 전세 → 월세</label>
    <label class="jwc-calc__mode"><input type="radio" name="jwc-mode" value="w2j"> 월세 → 전세</label>
  </fieldset>

  <div class="jwc-calc__grid">
    <div>
      <label class="jwc-calc__label" for="jwc-rate">전환율 (연 %)</label>
      <input class="jwc-calc__input" id="jwc-rate" type="number" inputmode="decimal" min="0" step="0.1" value="5.0">
      <p class="jwc-calc__hint" id="jwc-rate-hint" aria-live="polite"></p>
    </div>
    <div class="jwc-j2w">
      <label class="jwc-calc__label" for="jwc-deposit">전세보증금 (만원)</label>
      <input class="jwc-calc__input" id="jwc-deposit" type="number" inputmode="numeric" min="0" step="100" value="30000">
    </div>
    <div class="jwc-j2w">
      <label class="jwc-calc__label" for="jwc-keep">전환 후 남길 보증금 (만원)</label>
      <input class="jwc-calc__input" id="jwc-keep" type="number" inputmode="numeric" min="0" step="100" value="10000">
    </div>
    <div class="jwc-w2j jwc-hidden">
      <label class="jwc-calc__label" for="jwc-base">유지 보증금 (만원)</label>
      <input class="jwc-calc__input" id="jwc-base" type="number" inputmode="numeric" min="0" step="100" value="10000">
    </div>
    <div class="jwc-w2j jwc-hidden">
      <label class="jwc-calc__label" for="jwc-rent">월세 (만원)</label>
      <input class="jwc-calc__input" id="jwc-rent" type="number" inputmode="numeric" min="0" step="1" value="83">
    </div>
  </div>

  <div class="jwc-calc__result" id="jwc-result" aria-live="polite">
    <div class="jwc-calc__row">
      <span class="jwc-calc__key" id="jwc-out1-key">전환 대상 보증금</span>
      <span class="jwc-calc__val" id="jwc-out1-val">-</span>
    </div>
    <div class="jwc-calc__row">
      <span class="jwc-calc__key" id="jwc-out2-key">예상 월세</span>
      <span class="jwc-calc__val" id="jwc-out2-val">-</span>
    </div>
    <p class="jwc-calc__sub" id="jwc-out-sub"></p>
  </div>

  <script>
  (function(){
    function el(id){ return document.getElementById(id); }
    var CAP = 5.0; // 2026-09 법정 상한: 기준금리 3.00% + 2% = 5.0%
    function eokMan(v){
      v = Math.round(v);
      var eok = Math.floor(v / 10000);
      var man = v % 10000;
      var out = "";
      if(eok > 0){ out += eok + "억"; }
      if(man > 0){ out += (out ? " " : "") + man.toLocaleString() + "만원"; }
      return out || "0원";
    }
    function mode(){
      var r = document.getElementsByName("jwc-mode");
      for(var i = 0; i < r.length; i++){ if(r[i].checked){ return r[i].value; } }
      return "j2w";
    }
    function toggle(){
      var m = mode();
      var j = document.getElementsByClassName("jwc-j2w");
      var w = document.getElementsByClassName("jwc-w2j");
      var i;
      for(i = 0; i < j.length; i++){ j[i].className = "jwc-j2w" + (m === "j2w" ? "" : " jwc-hidden"); }
      for(i = 0; i < w.length; i++){ w[i].className = "jwc-w2j" + (m === "w2j" ? "" : " jwc-hidden"); }
    }
    function rateHint(){
      var rate = +el("jwc-rate").value || 0;
      var msg = "2026년 9월 법정 상한은 연 " + CAP + "% (기준금리 3.00% + 2%)입니다.";
      if(rate > CAP){ msg += " ⚠ 입력값이 상한을 초과합니다 — 계약 중 전환·갱신이라면 무효 소지."; }
      el("jwc-rate-hint").textContent = msg;
    }
    function calc(){
      var m = mode();
      var rate = +el("jwc-rate").value || 0;
      if(m === "j2w"){
        var deposit = (+el("jwc-deposit").value || 0) * 10000;
        var keep = (+el("jwc-keep").value || 0) * 10000;
        var conv = deposit - keep;
        if(conv < 0){ conv = 0; }
        var monthly = conv * (rate / 100) / 12;
        el("jwc-out1-key").textContent = "전환 대상 보증금";
        el("jwc-out1-val").textContent = eokMan(conv / 10000);
        el("jwc-out2-key").textContent = "예상 월세";
        el("jwc-out2-val").textContent = Math.round(monthly).toLocaleString() + "원";
        el("jwc-out-sub").textContent = "연 환산 " + Math.round(conv * (rate / 100)).toLocaleString() + "원 ÷ 12개월 · 전환율 " + rate + "% 적용";
      } else {
        var base = (+el("jwc-base").value || 0) * 10000;
        var rent = (+el("jwc-rent").value || 0) * 10000;
        var addBond = rate > 0 ? (rent * 12) / (rate / 100) : 0;
        var totalJeonse = base + addBond;
        el("jwc-out1-key").textContent = "월세의 보증금 환산액";
        el("jwc-out1-val").textContent = eokMan(addBond / 10000);
        el("jwc-out2-key").textContent = "전세 환산 총보증금";
        el("jwc-out2-val").textContent = eokMan(totalJeonse / 10000);
        el("jwc-out-sub").textContent = "월세 연 " + Math.round(rent * 12).toLocaleString() + "원 ÷ 전환율 " + rate + "% + 유지 보증금";
      }
      rateHint();
    }
    var modes = document.getElementsByName("jwc-mode");
    for(var k = 0; k < modes.length; k++){
      modes[k].addEventListener("change", function(){ toggle(); calc(); });
    }
    var ids = ["jwc-rate", "jwc-deposit", "jwc-keep", "jwc-base", "jwc-rent"];
    ids.forEach(function(id){
      var node = el(id);
      node.addEventListener("input", calc);
      node.addEventListener("change", calc);
    });
    toggle();
    calc();
  })();
  </script>
</div>
{% endraw %}

## 📐 전월세 전환율의 뜻과 계산 원리

전월세 전환율은 보증금과 월세를 맞바꿀 때 얼마의 연이율을 적용할지 정하는 값입니다. 전세보증금 가운데 일부를 월세로 돌린다고 하면, 월세로 전환하는 보증금에 전환율을 곱한 값이 1년치 월세가 되고, 이를 12로 나누면 매달 내는 월세가 됩니다. 반대로 월세를 전세로 환산할 때는 1년치 월세를 전환율로 나눠 보증금으로 되돌립니다.

식으로 정리하면 이렇습니다. 전세를 월세로 바꿀 때 월세는 '전환 보증금 × 전환율 ÷ 12'로 구하는데, 여기서 전환 보증금은 기존 전세보증금에서 전환 후 남기기로 한 보증금을 뺀 금액입니다. 시장에서 형성된 전환율을 거꾸로 알고 싶다면 '(월세 × 12) ÷ (전세보증금 − 월세보증금) × 100'으로 계산합니다. 전환율이 높을수록 같은 보증금을 월세로 돌렸을 때 월세 부담이 커지니, 세입자로서는 전환율이 낮을수록 유리합니다.

## ⚖️ 법으로 정한 전환율 상한

전월세 전환율에는 세입자를 보호하려는 법정 상한이 있습니다. 주택임대차보호법 제7조의2와 같은 법 시행령 제9조는 보증금을 월세로 전환할 때 적용할 수 있는 비율의 상한을 두 가지로 정해 두고, 그중 낮은 쪽을 넘지 못하게 하고 있습니다. 하나는 시행령이 정한 연 10%이고, 다른 하나는 한국은행이 공시한 기준금리에 시행령이 정한 연 2%를 더한 값입니다.

한국은행 기준금리는 2026년 8월 인상으로 연 3.00%가 되었습니다. 이를 대입하면 '기준금리 + 2%'는 연 5.0%가 되고, 연 10%보다 낮으므로 2026년 9월 현재 적용되는 법정 상한은 연 5.0%입니다. 기준금리가 바뀌면 상한도 함께 움직이니, 전환을 논의하는 시점의 기준금리를 확인하는 것이 중요합니다.

한 가지 주의할 점은 이 상한이 적용되는 범위입니다. 법정 상한은 이미 맺은 계약의 기간 중에 보증금 일부를 월세로 돌리거나, 세입자가 계약갱신요구권을 행사해 계약을 이어 갈 때 강제됩니다. 반면 집주인이 바뀌거나 완전히 새 임차인과 처음부터 조건을 정하는 신규 계약에는 그대로 적용되지 않습니다. 상한을 넘겨 받은 월세가 있다면 초과분은 무효이므로, 세입자는 낮춰 달라고 요구하거나 이미 낸 금액을 돌려받을 수 있습니다.

## 🧮 계산 예시로 확인하기

숫자로 짚어 보겠습니다. 전세보증금 3억원인 집에서 보증금 1억원은 그대로 두고 나머지 2억원을 월세로 돌린다고 해 보겠습니다. 전환하는 보증금은 3억원에서 1억원을 뺀 2억원이고, 법정 상한인 연 5.0%를 적용하면 1년치 월세는 2억원 × 5.0% = 1,000만원, 이를 12로 나눈 월세는 약 83만원입니다. 만약 집주인이 상한을 넘겨 연 6.0%를 적용하려 하면 월세는 100만원으로 뛰지만, 계약 기간 중 전환이나 갱신 상황이라면 5.0%를 넘는 부분은 요구할 수 없습니다.

아래 표는 같은 조건에서 전환율에 따라 월세가 어떻게 달라지는지 보여 줍니다.

| 전환 보증금 | 적용 전환율 | 연간 환산액 | 월세(근사) |
| --- | --- | --- | --- |
| 2억원 | 4.0% | 800만원 | 약 67만원 |
| 2억원 | 5.0%(법정 상한) | 1,000만원 | 약 83만원 |
| 2억원 | 6.0% | 1,200만원 | 약 100만원 |

전환율이 1%포인트만 달라져도 월세가 매달 16만~17만원씩 차이가 나니, 전환율이 상한 안에 있는지 반드시 확인하셔야 합니다.

## ✅ 확인해 두면 좋은 것들

전월세 전환에서 자주 놓치는 대목을 짚어 보겠습니다. 먼저 법정 상한은 계약 기간 중 전환과 갱신 때만 강제되고 신규 계약에는 적용되지 않으니, 내 상황이 어디에 해당하는지부터 확인해야 합니다. 기준금리가 바뀌면 상한도 달라지므로 전환을 협의하는 시점의 기준금리를 봐야 하고, 과거 계약 당시의 상한을 그대로 적용해서는 안 됩니다. 전환율이 낮을수록 세입자에게 유리하니 시장에서 형성된 전환율과 법정 상한을 함께 견줘 보는 편이 좋습니다. 여기에 한국부동산원 임대료 계산기나 렌트홈 같은 공적 도구로 교차 확인하면 실수를 줄일 수 있습니다.

## 📝 총평

전월세 전환율은 '전환 보증금 × 전환율 ÷ 12'로 월세를 구하고, '기준금리 + 2%'와 '연 10%' 중 낮은 쪽이 법정 상한이라는 두 줄로 간추릴 수 있습니다. 기준금리가 연 3.00%인 2026년 9월 현재 상한은 연 5.0%이며, 계약 기간 중 전환이나 갱신 때 힘을 발휘합니다. 보증금과 월세를 맞바꾸는 협의를 앞두고 있다면, 제시받은 전환율이 상한 안에 있는지 먼저 따져 보고 월세 부담을 직접 계산해 보시길 권합니다. 정확한 기준금리와 상한은 한국은행 공시와 관계 법령으로 확인하는 것이 가장 안전합니다.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

**출처**

- [국가법령정보센터 — 주택임대차보호법 제7조의2(월차임 전환 시 산정률의 제한)](https://www.law.go.kr/법령/주택임대차보호법)
- [국가법령정보센터 — 주택임대차보호법 시행령 제9조](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=130112&chrClsCd=010202)
- [국토교통부 — 전월세 전환율 하향 조정 안내](https://www.molit.go.kr/policy/rent/rent_f_02.jsp)
- [한국부동산원 임대차분쟁조정위원회 — 전월세전환 계산](https://adrhome.reb.or.kr/adrhome/reb/transfer/transferCalculatorForm.do?Key=10404000000002022101900)
- [한국은행 — 기준금리 추이](https://www.bok.or.kr/portal/singl/baseRate/list.do?dataSeCd=01&menuNo=200643)
