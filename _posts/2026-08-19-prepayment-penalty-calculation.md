---
layout: post
title: "중도상환수수료 계산법 총정리 — 슬라이딩 공식·3년 면제 기준과 갈아타기 손익 계산기 🏠"
date: 2026-08-19 07:00:00 +0900
lang: ko
permalink: /2026/08/19/prepayment-penalty-calculation/
page_id: 2026-08-19-prepayment-penalty-calculation
image: /assets/og/2026-08-19-prepayment-penalty-calculation-ko.png
summary: "중도상환수수료는 '중도상환원금 × 요율 × (부과기간 잔여기간 ÷ 부과기간)'으로 시간이 지날수록 줄어드는 슬라이딩 방식이며, 보통 대출일로부터 3년이 지나면 면제됩니다. 2025년 실비 기반 개편으로 낮아진 요율, 계산 공식, 갈아타기 손익 판단법을 계산기와 함께 정리했습니다."
description: "중도상환수수료 계산법을 슬라이딩 공식과 부과기간 3년 면제 기준, 계산기로 정리했습니다. 2025년 요율 인하와 대출 갈아타기 손익 판단까지 확인하세요."
categories: [부동산]
tags: [중도상환수수료, 중도상환수수료계산, 주택담보대출, 대출갈아타기, 대환대출, 중도상환수수료율, 슬라이딩방식, 대출중도상환, 중도상환수수료면제, 대출상환, 부동산대출, 금융위원회, 중도상환수수료개편, 주담대, 대출비용]
---

**핵심 요약 (TL;DR)**

- 중도상환수수료는 '중도상환원금 × 요율 × (부과기간 잔여기간 ÷ 부과기간)'으로 계산되며, 시간이 지날수록 줄어드는 슬라이딩 방식입니다.
- 부과기간은 대부분 3년으로, 대출일로부터 3년이 지나면 남은 대출을 갚아도 수수료가 붙지 않습니다.
- 2025년 1월 13일 이후 새로 받은 대출은 실비 기반으로 요율이 낮아져, 5대 은행 주택담보대출 평균 요율이 고정 1.4%→0.65%, 변동 1.2%→0.65% 수준으로 내려갔습니다.

대출을 만기 전에 갚거나 더 낮은 금리로 갈아탈 때 마지막에 부딪히는 비용이 중도상환수수료입니다. 결론부터 말하면, 중도상환수수료는 **남은 대출을 일찍 갚을 때 은행이 부과하는 수수료로, '중도상환원금 × 요율 × (부과기간 잔여기간 ÷ 부과기간)' 공식으로 계산되며 시간이 지날수록 줄어듭니다.** 부과기간은 보통 3년이라, 3년만 지나면 수수료 없이 자유롭게 갚을 수 있습니다.

아래 계산기에 중도상환할 원금과 요율, 대출 후 지난 기간만 넣으면 예상 수수료가 바로 나옵니다. 이어지는 설명에서 공식과 갈아타기 손익 판단법까지 확인하실 수 있습니다. 💡

{% raw %}
<div class="prepay-calc" id="prepay-calc">
  <style>
    .prepay-calc { border: 1px solid #e2e2e2; border-radius: 12px; padding: 20px; margin: 8px 0 4px; background: #fafafa; }
    .prepay-calc .prepay-calc__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px 18px; }
    .prepay-calc .prepay-calc__label { display: block; font-size: 13px; color: #555; margin-bottom: 4px; }
    .prepay-calc .prepay-calc__field { width: 100%; box-sizing: border-box; height: 38px; padding: 0 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; background: #fff; }
    .prepay-calc .prepay-calc__hint { font-size: 12px; color: #1b4fa0; margin-top: 4px; min-height: 16px; }
    .prepay-calc .prepay-calc__cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-top: 18px; align-items: start; }
    .prepay-calc .prepay-calc__card { background: #fff; border: 1px solid #ececec; border-radius: 8px; padding: 14px; }
    .prepay-calc .prepay-calc__card-label { font-size: 13px; color: #666; }
    .prepay-calc .prepay-calc__card-value { font-size: 18px; font-weight: 600; margin-top: 4px; }
    .prepay-calc .prepay-calc__card-sub { font-size: 12px; color: #999; margin-top: 2px; }
    .prepay-calc .prepay-calc__final { background: #eef4ff; border: 1px solid #cdddff; border-radius: 12px; padding: 16px 18px; margin-top: 14px; }
    .prepay-calc .prepay-calc__final-label { font-size: 13px; color: #1b4fa0; }
    .prepay-calc .prepay-calc__final-value { font-size: 26px; font-weight: 700; color: #1b4fa0; margin-top: 2px; }
    .prepay-calc .prepay-calc__final-sub { font-size: 12px; color: #5a78ad; margin-top: 4px; }
    .prepay-calc .prepay-calc__note { font-size: 12px; color: #888; margin-top: 12px; line-height: 1.6; }
  </style>

  <div class="prepay-calc__grid">
    <div>
      <label class="prepay-calc__label" for="prepay-principal">중도상환 원금 (만원)</label>
      <input class="prepay-calc__field" type="number" id="prepay-principal" value="30000" min="0" step="100">
    </div>
    <div>
      <label class="prepay-calc__label" for="prepay-rate">중도상환수수료율 (%)</label>
      <input class="prepay-calc__field" type="number" id="prepay-rate" value="0.65" min="0" step="0.01">
      <div class="prepay-calc__hint" id="prepay-rate-hint"></div>
    </div>
  </div>

  <div class="prepay-calc__grid" style="margin-top:14px;">
    <div>
      <label class="prepay-calc__label" for="prepay-elapsed">대출 후 지난 기간 (개월)</label>
      <input class="prepay-calc__field" type="number" id="prepay-elapsed" value="12" min="0" step="1">
    </div>
    <div>
      <label class="prepay-calc__label" for="prepay-term">부과기간 (년)</label>
      <select class="prepay-calc__field" id="prepay-term">
        <option value="3" selected>3년 (일반적)</option>
        <option value="2">2년</option>
        <option value="1">1년</option>
      </select>
    </div>
  </div>

  <div class="prepay-calc__cards">
    <div class="prepay-calc__card">
      <div class="prepay-calc__card-label">부과기간 잔여</div>
      <div class="prepay-calc__card-value" id="prepay-left">–</div>
      <div class="prepay-calc__card-sub" id="prepay-left-sub"></div>
    </div>
    <div class="prepay-calc__card">
      <div class="prepay-calc__card-label">적용 비율</div>
      <div class="prepay-calc__card-value" id="prepay-ratio">–</div>
      <div class="prepay-calc__card-sub">잔여기간 ÷ 부과기간</div>
    </div>
  </div>

  <div class="prepay-calc__final" aria-live="polite">
    <div class="prepay-calc__final-label">예상 중도상환수수료</div>
    <div class="prepay-calc__final-value" id="prepay-fee">–</div>
    <div class="prepay-calc__final-sub" id="prepay-fee-sub"></div>
  </div>

  <p class="prepay-calc__note">부과기간을 월 단위로 환산해 '중도상환원금 × 요율 × (잔여개월 ÷ 부과개월)'로 계산한 추정치입니다. 실제 요율·부과기간·잔여기간 산정 방식(일수 기준 등)은 상품과 금융회사마다 다르므로, 정확한 금액은 대출 약정서와 각 사 공시를 확인하시기 바랍니다. 원 단위는 반올림했습니다.</p>

  <script>
  (function(){
    var el = function(id){ return document.getElementById(id); };
    function won(v){ return Math.round(v).toLocaleString() + "원"; }
    function eokMan(v){
      v = Math.round(v);
      var eok = Math.floor(v / 100000000);
      var man = Math.round((v % 100000000) / 10000);
      var out = "";
      if(eok > 0){ out += eok + "억"; }
      if(man > 0){ out += (out ? " " : "") + man.toLocaleString() + "만원"; }
      return out || "0원";
    }
    function calc(){
      var principal = (+el("prepay-principal").value || 0) * 10000;
      var rate = +el("prepay-rate").value || 0;
      var elapsed = +el("prepay-elapsed").value || 0;
      var termMonths = (+el("prepay-term").value || 3) * 12;
      if(elapsed < 0){ elapsed = 0; }
      var leftMonths = termMonths - elapsed;
      if(leftMonths <= 0){ leftMonths = 0; }
      var ratio = termMonths > 0 ? leftMonths / termMonths : 0;
      var fee = principal * (rate / 100) * ratio;

      if(leftMonths <= 0){
        el("prepay-left").textContent = "0개월";
        el("prepay-left-sub").textContent = "부과기간 경과 · 면제";
        el("prepay-ratio").textContent = "0%";
        el("prepay-fee").textContent = "0원 (면제)";
        el("prepay-fee-sub").textContent = "부과기간이 지나 수수료가 붙지 않습니다";
        return;
      }
      el("prepay-left").textContent = leftMonths + "개월";
      el("prepay-left-sub").textContent = "총 " + termMonths + "개월 중";
      el("prepay-ratio").textContent = (Math.round(ratio * 1000) / 10) + "%";
      el("prepay-fee").textContent = eokMan(fee);
      el("prepay-fee-sub").textContent = won(fee) + " · 요율 " + rate + "% 적용";
    }
    function hint(){
      var r = +el("prepay-rate").value || 0;
      var msg = "";
      if(r >= 1.1){ msg = "2025년 개편 전 수준입니다. 최근 신규 대출은 0.5~0.7%대가 많습니다."; }
      else if(r > 0 && r <= 0.75){ msg = "2025년 개편 후 은행권 주담대 평균 수준입니다."; }
      el("prepay-rate-hint").textContent = msg;
    }
    var ids = ["prepay-principal", "prepay-rate", "prepay-elapsed", "prepay-term"];
    ids.forEach(function(id){
      var node = el(id);
      node.addEventListener("input", function(){ calc(); hint(); });
      node.addEventListener("change", function(){ calc(); hint(); });
    });
    calc();
    hint();
  })();
  </script>
</div>
{% endraw %}

## 🧾 중도상환수수료란 무엇인가

중도상환수수료는 약정한 만기보다 대출을 일찍 갚을 때 금융회사가 물리는 비용입니다. 은행은 미리 정해 둔 기간만큼 이자가 들어올 것으로 보고 자금을 굴리는데, 대출자가 중간에 갚아 버리면 그 계획이 어긋납니다. 이때 생기는 자금 운용 손실과 대출을 취급하며 든 행정·모집 비용을 메우자는 명목으로 매기는 것이 바로 이 수수료입니다.

여기서 눈여겨볼 점은, 이 수수료가 정액이 아니라 **시간이 지날수록 줄어드는 구조**라는 것입니다. 대출을 받자마자 갚으면 은행이 떠안는 손실이 크지만, 만기에 가까워질수록 그 손실은 작아집니다. 이렇게 잔여기간에 따라 수수료가 점점 깎여 나가는 방식을 흔히 슬라이딩(체감식) 방식이라고 부릅니다.

## 🧮 계산 공식과 부과기간

중도상환수수료는 다음 공식으로 구합니다.

> **중도상환수수료 = 중도상환원금 × 중도상환수수료율 × (부과기간 잔여기간 ÷ 부과기간)**

부과기간이란 수수료가 매겨지는 전체 구간을 말하는데, 대부분의 대출이 **3년**으로 잡혀 있습니다. 대출을 실행한 날로부터 3년까지만 수수료가 붙고, 그 기간이 지나면 남은 대출을 한꺼번에 갚아도 수수료는 0원입니다. 잔여기간은 부과기간에서 이미 지난 기간을 뺀 값이라, 대출 후 시간이 흐를수록 짧아지고 그만큼 수수료도 줄어듭니다.

| 요소 | 의미 |
| --- | --- |
| 중도상환원금 | 이번에 미리 갚는 대출 원금 |
| 중도상환수수료율 | 상품·금융회사가 공시한 요율(예: 0.65%) |
| 부과기간 | 수수료가 매겨지는 전체 기간(보통 3년) |
| 잔여기간 | 부과기간 − 대출 후 지난 기간 |

가령 부과기간이 3년(36개월)인 대출을 받은 지 1년(12개월) 됐다면, 잔여기간은 24개월이고 적용 비율은 24 ÷ 36, 약 66.7%가 됩니다. 같은 대출을 2년(24개월) 뒤에 갚으면 비율은 12 ÷ 36으로 약 33.3%까지 내려가고, 3년이 지나면 0%가 되어 수수료가 사라집니다.

## 💰 2025년 개편으로 낮아진 요율

2025년 1월 13일, 금융위원회가 제도를 손보면서 중도상환수수료 체계가 달라졌습니다. 그동안 금융회사가 다소 제멋대로 정하던 요율을, 자금 운용 손실과 행정·모집 비용 같은 **실비용 범위 안에서만** 물리도록 못 박은 것이 핵심입니다. 덕분에 요율이 전반적으로 내려갔습니다.

| 구분 | 개편 전(평균) | 개편 후(평균) |
| --- | --- | --- |
| 주택담보대출 고정금리 | 약 1.4% | 약 0.65% |
| 주택담보대출 변동금리 | 약 1.2% | 약 0.65% |

이 요율은 5대 시중은행 주택담보대출 평균을 기준으로 한 것이며, 낮아진 요율은 **2025년 1월 13일 이후 새로 체결된 대출**부터 적용됩니다. 그전에 받은 대출은 기존 약정 요율이 그대로 유지되니, 내 대출이 어느 쪽인지는 약정서나 은행 앱에서 확인해 보셔야 합니다. 이 개편은 2026년 1월 1일부터 농협·수협·새마을금고 같은 상호금융권으로도 넓어집니다. 다만 은행과 상품마다 공시 요율이 제각각이라, 위 수치는 대략적인 눈높이로만 참고하시고 실제 요율은 각 사 공시로 확인하시는 편이 정확합니다.

## 🔍 실전 계산 예시

잔여원금 3억원, 부과기간 3년(36개월)인 주택담보대출을 대출 1년 뒤에 전액 갚는다고 해 보겠습니다. 적용 비율은 24 ÷ 36으로 약 66.7%입니다.

| 요율 기준 | 계산 | 중도상환수수료 |
| --- | --- | --- |
| 개편 후 변동(0.65%) | 3억 × 0.65% × 66.7% | 약 130만원 |
| 개편 전 변동(1.2%) | 3억 × 1.2% × 66.7% | 약 240만원 |

똑같은 조건인데도 요율이 1.2%에서 0.65%로 내려가면서 수수료가 240만원에서 130만원으로, 110만원가량 줄었습니다. 대출 시점이 2025년 1월 13일 이전이냐 이후냐에 따라 이만큼 차이가 나는 셈입니다.

## 🔄 갈아타기, 손익은 이렇게 따집니다

더 낮은 금리로 갈아탈지 고민된다면 **중도상환수수료와 이자 절감액을 견줘 보면** 됩니다. 원리는 단순합니다. 남은 기간 동안 아끼는 이자가 지금 내는 수수료보다 크다면 갈아타는 쪽이 이득입니다.

앞선 예시(잔여원금 3억원, 수수료 130만원)에서 금리를 연 5.0%에서 4.0%로, 1.0%포인트 낮춰 갈아탄다고 해 보겠습니다.

| 항목 | 금액(근사) |
| --- | --- |
| 중도상환수수료 | 약 130만원 |
| 연간 이자 절감액 | 3억 × 1.0% ≈ 약 300만원 |
| 2년간 이자 절감액 | 약 600만원 |
| 순이득(절감 − 수수료) | 약 470만원 |

이 경우 2년만 유지해도 아끼는 이자가 수수료를 훌쩍 넘어서니 갈아타는 게 유리합니다. 다만 이자 절감액은 원금을 갚아 나갈수록 조금씩 작아지므로, 위 600만원은 최대치에 가까운 근사값으로 봐 두는 편이 안전합니다. 거꾸로 남은 기간이 몇 달밖에 없거나 금리 인하폭이 작다면, 절감액이 수수료를 못 넘겨 갈아탈 실익이 없을 수도 있습니다. 여기에 대환하며 새로 드는 인지세·근저당 설정비 같은 부대비용까지 얹어서 따져 보면 판단이 한결 정확해집니다.

## ✅ 확인해 두면 좋은 것들

중도상환수수료에서 자주 놓치는 대목을 짚어 보겠습니다. 첫째, 부과기간(보통 3년)이 지났다면 수수료가 아예 없으니, 3년째가 코앞이라면 조금 기다렸다 갚는 것만으로 수수료를 아낄 수 있습니다. 둘째, 요율과 부과기간, 잔여기간을 개월로 재는지 일수로 재는지 하는 산정 방식은 상품마다 다르므로 약정서를 꼭 확인하셔야 합니다. 셋째, 은행에 따라 일정 금액이나 비율까지는 수수료 없이 갚게 해 주는 조기상환 한도를 두기도 합니다. 끝으로, 2025년 개편으로 낮아진 요율은 신규 대출에만 적용되니 기존 대출자는 자신의 약정 요율을 기준으로 계산해야 합니다.

## 📝 총평

중도상환수수료는 '중도상환원금 × 요율 × (부과기간 잔여기간 ÷ 부과기간)'이라는 한 줄로 간추릴 수 있습니다. 부과기간이 보통 3년이고 시간이 지날수록 줄어든다는 점, 3년이 지나면 면제된다는 점, 이 둘만 기억하면 내 수수료를 직접 어림할 수 있습니다. 2025년 개편으로 요율이 절반 안팎까지 내려간 만큼, 대출을 일찍 갚거나 더 낮은 금리로 갈아탈 때는 수수료와 이자 절감액을 나란히 놓고 저울질해 보시길 권합니다. 정확한 요율과 조건은 대출 약정서와 각 금융회사 공시로 확인하는 것이 가장 안전합니다.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

**출처**

- [금융위원회 — 중도상환수수료 제도개선 방안 보도자료](https://www.fsc.go.kr/no010101/81155)
- [KB국민은행 — 대출 중도상환수수료 종류·계산](https://obank.kbstar.com/quics?page=C016694)
- [토스뱅크 — 중도상환수수료 개편 안내](https://www.tossbank.com/articles/earlyrepaymentfee)
- [뱅크몰 — 2025년 주택담보대출 중도상환수수료율 인하](https://www.bank-mall.co.kr/plus/blog/12039)
