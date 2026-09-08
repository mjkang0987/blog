---
layout: post
title: "양도소득세 계산법 총정리 — 양도차익·장기보유공제·세율로 세금 구하기 🏠"
date: 2026-09-09 07:00:00 +0900
lang: ko
permalink: /2026/09/09/capital-gains-tax-calculation/
page_id: 2026-09-09-capital-gains-tax-calculation
image: /assets/og/2026-09-09-capital-gains-tax-calculation-ko.png
summary: "양도소득세는 '양도가액 − 취득가액 − 필요경비'로 양도차익을 구한 뒤 장기보유특별공제와 기본공제 250만 원을 빼 과세표준을 만들고, 6~45% 기본세율에서 누진공제를 차감해 계산합니다. 여기에 지방소득세 10%가 별도로 붙습니다. 계산 흐름과 2026년 세율표, 장기보유특별공제율, 계산기를 함께 정리했습니다."
description: "양도소득세 계산법을 계산기와 함께 정리했습니다. 양도차익·장기보유특별공제·기본세율(6~45%)·누진공제로 내 부동산 양도세를 직접 계산해 보세요."
categories: [부동산]
tags: [양도소득세, 양도세계산, 양도차익, 장기보유특별공제, 양도소득세율, 누진공제, 기본공제, 지방소득세, 1세대1주택, 단기양도세율, 부동산세금, 취득가액, 필요경비, 과세표준, 부동산양도]
---

**핵심 요약 (TL;DR)**

- 양도차익은 '양도가액 − 취득가액 − 필요경비'로 구하고, 여기서 장기보유특별공제와 기본공제 250만 원을 뺀 과세표준에 6~45% 세율을 매겨 세금을 계산합니다.
- 세액은 '과세표준 × 세율 − 누진공제'로 한 번에 나오며, 이렇게 나온 산출세액의 10%가 지방소득세로 따로 붙습니다.
- 보유 2년을 못 채운 주택은 60~70% 단일세율이 걸려 세율이 확 뛰기 때문에, 언제 파느냐에 따라 세금이 크게 갈립니다.

집을 팔아 남긴 이익에 매기는 세금이 양도소득세입니다. 결국 얼마를 벌었는지(양도차익)에 얼마나 오래 갖고 있었는지(공제·세율)를 곱해 정해지는 구조라, 계산 순서만 익혀 두면 대략의 세금은 직접 뽑아볼 수 있습니다. 이 글에서는 국세청 세액계산 흐름을 따라가며 단계별 공식과 2026년 현재 세율표, 장기보유특별공제율을 정리하고, 값만 넣으면 세금이 나오는 계산기도 함께 실었습니다. 🏠

## 📌 양도소득세는 이렇게 계산됩니다

국세청 세액계산 흐름은 아래 다섯 단계로 이어집니다. 단계마다 무엇을 빼는지가 관건입니다.

| 단계 | 계산식 | 설명 |
| --- | --- | --- |
| ① 양도차익 | 양도가액 − 취득가액 − 필요경비 | 판 값에서 산 값과 경비를 뺀 실제 이익 |
| ② 양도소득금액 | 양도차익 − 장기보유특별공제 | 3년 이상 보유분에 대한 공제를 차감 |
| ③ 과세표준 | 양도소득금액 − 기본공제 250만 원 | 1인당 연 1회, 250만 원 공제 |
| ④ 산출세액 | 과세표준 × 세율 − 누진공제 | 6~45% 누진세율 적용 |
| ⑤ 총부담세액 | 산출세액 + 지방소득세(산출세액의 10%) | 지방소득세가 별도로 가산 |

여기서 필요경비란 취득세·법무사 비용·중개보수처럼 사고팔 때 실제로 든 돈, 그리고 발코니 확장이나 난방 교체 같은 자본적 지출을 가리킵니다. 도배·장판·싱크대 교체 같은 단순 수리비는 필요경비로 쳐 주지 않습니다. 기본공제 250만 원은 한 사람당 1년에 딱 한 번만 적용되므로, 같은 해에 여러 건을 팔아도 공제는 한 번뿐입니다.

## 📊 2026년 양도소득세 기본세율표

보유 기간 2년 이상 자산에 붙는 기본세율은 과세표준 구간에 따라 6%에서 45%까지 올라가는 누진세율입니다. '과세표준 × 세율 − 누진공제'에 값을 넣으면 산출세액이 한 번에 나옵니다.

| 과세표준 | 세율 | 누진공제 |
| --- | --- | --- |
| 1,400만 원 이하 | 6% | – |
| 1,400만 ~ 5,000만 원 | 15% | 126만 원 |
| 5,000만 ~ 8,800만 원 | 24% | 576만 원 |
| 8,800만 ~ 1억 5,000만 원 | 35% | 1,544만 원 |
| 1억 5,000만 ~ 3억 원 | 38% | 1,994만 원 |
| 3억 ~ 5억 원 | 40% | 2,594만 원 |
| 5억 ~ 10억 원 | 42% | 3,594만 원 |
| 10억 원 초과 | 45% | 6,594만 원 |

가령 과세표준이 1억 원이면 세율 35% 구간에 걸리므로 산출세액은 '1억 원 × 35% − 1,544만 원 = 1,956만 원'입니다. 여기에 지방소득세 195만 6,000원이 붙어 실제 부담은 약 2,151만 6,000원이 됩니다.

## ⏱️ 단기 보유는 세율이 확 뜁니다

짧게 사고팔며 차익을 노리는 거래를 막으려고, 보유 기간이 짧으면 누진세율 대신 높은 단일세율을 물립니다. 이때는 장기보유특별공제도 받지 못합니다.

| 자산·보유 기간 | 세율 |
| --- | --- |
| 주택·조합원입주권 (1년 미만) | 70% |
| 주택·조합원입주권 (1년 이상 2년 미만) | 60% |
| 분양권 (1년 미만) | 70% |
| 분양권 (1년 이상) | 60% |
| 일반 부동산 (1년 미만) | 50% |
| 일반 부동산 (1년 이상 2년 미만) | 40% |

이익이 같아도 1년을 못 채우고 팔면 세율이 두 배 넘게 뛸 수 있습니다. 파는 시점을 조금만 미뤄 2년을 넘기면 기본세율(6~45%) 구간으로 내려오는 데다 장기보유특별공제까지 받을 수 있으니, 매도 시기를 언제로 잡느냐가 세금에 큰 차이를 냅니다.

## 🏠 장기보유특별공제, 오래 가질수록 커집니다

장기보유특별공제는 3년 이상 보유한 부동산의 물가상승분을 감안해 양도차익에서 일정 비율을 깎아 주는 제도입니다. 일반 부동산과 1세대 1주택은 공제율이 다릅니다.

| 보유 기간 | 일반 부동산 | 1세대 1주택(보유+거주) |
| --- | --- | --- |
| 3년 이상 | 6% | 최대 24% (보유 12%+거주 12%) |
| 5년 이상 | 10% | 최대 40% (보유 20%+거주 20%) |
| 10년 이상 | 20% | 최대 80% (보유 40%+거주 40%) |
| 15년 이상 | 30% (한도) | 80% (한도) |

일반 부동산은 보유 기간 1년마다 2%씩 쌓여 15년이면 최대 30%까지, 1세대 1주택은 2년 이상 거주를 전제로 보유 연 4%와 거주 연 4%를 더해 최대 80%까지 공제받습니다. 똑같이 10년을 보유했더라도 실제 살던 1주택이면 공제율이 20%에서 80%로 네 배까지 벌어질 수 있어, 실거주 여부가 세금을 크게 좌우합니다.

한 가지 짚어 둘 점이 있습니다. 2026년 9월 1일 국무회의를 통과한 세법개정 정부안에는 다주택 중과와 1세대 1주택 장기보유공제 구조를 2027~2029년에 걸쳐 단계적으로 손보는 내용이 담겨 있습니다. 다만 아직 국회 심의를 거치지 않은 정부안이므로, 아래 계산은 현행 기준으로 봐 주시고 실제 신고 시점의 확정 법령은 따로 확인하시기 바랍니다.

## 🧮 양도소득세 계산기

양도가액·취득가액·필요경비와 보유·거주 기간을 넣으면 양도차익부터 총부담세액까지 어림해 계산해 줍니다. 주택 기준이며, 다주택 중과세율은 빼고 일반세율로 잡았습니다.

{% raw %}
<div class="cgt-calc" id="cgt-calc">
  <style>
    .cgt-calc { border: 1px solid #e2e2e2; border-radius: 12px; padding: 20px; margin: 8px 0 4px; background: #fafafa; }
    .cgt-calc .cgt-calc__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px 18px; }
    .cgt-calc .cgt-calc__label { display: block; font-size: 13px; color: #555; margin-bottom: 4px; }
    .cgt-calc .cgt-calc__field { width: 100%; box-sizing: border-box; height: 38px; padding: 0 10px; border: 1px solid #ccc; border-radius: 8px; font-size: 15px; background: #fff; }
    .cgt-calc .cgt-calc__hint { font-size: 12px; color: #1b4fa0; margin-top: 4px; min-height: 16px; }
    .cgt-calc .cgt-calc__cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-top: 18px; align-items: start; }
    .cgt-calc .cgt-calc__card { background: #fff; border: 1px solid #ececec; border-radius: 8px; padding: 14px; }
    .cgt-calc .cgt-calc__card-label { font-size: 13px; color: #666; }
    .cgt-calc .cgt-calc__card-value { font-size: 18px; font-weight: 600; margin-top: 4px; }
    .cgt-calc .cgt-calc__card-sub { font-size: 12px; color: #999; margin-top: 2px; }
    .cgt-calc .cgt-calc__final { background: #eef4ff; border: 1px solid #cdddff; border-radius: 12px; padding: 16px 18px; margin-top: 14px; }
    .cgt-calc .cgt-calc__final-label { font-size: 13px; color: #1b4fa0; }
    .cgt-calc .cgt-calc__final-value { font-size: 26px; font-weight: 700; color: #1b4fa0; margin-top: 2px; }
    .cgt-calc .cgt-calc__note { font-size: 12px; color: #888; margin-top: 12px; line-height: 1.5; }
  </style>
  <div class="cgt-calc__grid">
    <div>
      <label class="cgt-calc__label" for="cgt-sale">양도가액 (판 금액, 원)</label>
      <input class="cgt-calc__field" id="cgt-sale" type="number" inputmode="numeric" min="0" step="10000000" value="1500000000">
    </div>
    <div>
      <label class="cgt-calc__label" for="cgt-buy">취득가액 (산 금액, 원)</label>
      <input class="cgt-calc__field" id="cgt-buy" type="number" inputmode="numeric" min="0" step="10000000" value="900000000">
    </div>
    <div>
      <label class="cgt-calc__label" for="cgt-cost">필요경비 (취득세·중개보수 등, 원)</label>
      <input class="cgt-calc__field" id="cgt-cost" type="number" inputmode="numeric" min="0" step="1000000" value="30000000">
    </div>
    <div>
      <label class="cgt-calc__label" for="cgt-type">보유 유형</label>
      <select class="cgt-calc__field" id="cgt-type">
        <option value="general" selected>일반(다주택·비거주 등)</option>
        <option value="one">1세대 1주택(거주 2년 이상 특례)</option>
      </select>
    </div>
    <div>
      <label class="cgt-calc__label" for="cgt-hold">보유 기간 (년)</label>
      <input class="cgt-calc__field" id="cgt-hold" type="number" inputmode="numeric" min="0" step="1" value="10">
    </div>
    <div>
      <label class="cgt-calc__label" for="cgt-live">거주 기간 (년, 1주택 특례만)</label>
      <input class="cgt-calc__field" id="cgt-live" type="number" inputmode="numeric" min="0" step="1" value="10">
    </div>
  </div>
  <div class="cgt-calc__cards">
    <div class="cgt-calc__card">
      <div class="cgt-calc__card-label">양도차익</div>
      <div class="cgt-calc__card-value" id="cgt-gain">-</div>
    </div>
    <div class="cgt-calc__card">
      <div class="cgt-calc__card-label">장기보유특별공제</div>
      <div class="cgt-calc__card-value" id="cgt-ltd">-</div>
      <div class="cgt-calc__card-sub" id="cgt-ltd-sub">-</div>
    </div>
    <div class="cgt-calc__card">
      <div class="cgt-calc__card-label">과세표준</div>
      <div class="cgt-calc__card-value" id="cgt-base">-</div>
    </div>
    <div class="cgt-calc__card">
      <div class="cgt-calc__card-label">산출세액 (지방소득세 제외)</div>
      <div class="cgt-calc__card-value" id="cgt-tax">-</div>
      <div class="cgt-calc__card-sub" id="cgt-tax-sub">-</div>
    </div>
  </div>
  <div class="cgt-calc__final">
    <div class="cgt-calc__final-label">총부담세액 (지방소득세 10% 포함)</div>
    <div class="cgt-calc__final-value" id="cgt-total">-</div>
  </div>
  <p class="cgt-calc__note">주택 기준의 개략 추정치입니다. 조정대상지역 다주택 중과세율, 감면·비과세 특례는 반영하지 않았습니다. 보유 2년 미만 주택은 단기세율(1년 미만 70%, 2년 미만 60%)을 적용하며 이 경우 장기보유특별공제는 없습니다. 정확한 세액은 홈택스 또는 세무 전문가에게 확인하시기 바랍니다.</p>
  <script>
    (function () {
      var ids = ['cgt-sale', 'cgt-buy', 'cgt-cost', 'cgt-type', 'cgt-hold', 'cgt-live'];
      var won = function (n) { return Math.round(n).toLocaleString('ko-KR') + '원'; };
      var num = function (id) { var v = parseFloat(document.getElementById(id).value); return isNaN(v) ? 0 : v; };
      var brackets = [
        [14000000, 0.06, 0],
        [50000000, 0.15, 1260000],
        [88000000, 0.24, 5760000],
        [150000000, 0.35, 15440000],
        [300000000, 0.38, 19940000],
        [500000000, 0.40, 25940000],
        [1000000000, 0.42, 35940000],
        [Infinity, 0.45, 65940000]
      ];
      function progressive(base) {
        for (var i = 0; i < brackets.length; i++) {
          if (base <= brackets[i][0]) { return base * brackets[i][1] - brackets[i][2]; }
        }
        return 0;
      }
      function calc() {
        var sale = num('cgt-sale');
        var buy = num('cgt-buy');
        var cost = num('cgt-cost');
        var type = document.getElementById('cgt-type').value;
        var hold = num('cgt-hold');
        var live = num('cgt-live');
        var gain = Math.max(0, sale - buy - cost);

        var ltdRate = 0;
        if (hold >= 3) {
          if (type === 'one') {
            var holdRate = Math.min(40, hold * 4);
            var liveRate = live < 2 ? 0 : (live < 3 ? 8 : Math.min(40, live * 4));
            ltdRate = Math.min(80, holdRate + liveRate);
          } else {
            ltdRate = Math.min(30, hold * 2);
          }
        }
        var ltd = gain * ltdRate / 100;
        var incomeAmt = gain - ltd;
        var base = Math.max(0, incomeAmt - 2500000);

        var tax = 0;
        var rateLabel = '';
        if (gain <= 0) {
          tax = 0;
          rateLabel = '양도차익 없음';
          ltd = 0;
          base = 0;
        } else if (hold < 1) {
          tax = base * 0.70;
          rateLabel = '단기세율 70% (1년 미만)';
        } else if (hold < 2) {
          tax = base * 0.60;
          rateLabel = '단기세율 60% (2년 미만)';
        } else {
          tax = Math.max(0, progressive(base));
          rateLabel = '기본세율 6~45% 적용';
        }
        var local = tax * 0.10;
        var total = tax + local;

        document.getElementById('cgt-gain').textContent = won(gain);
        document.getElementById('cgt-ltd').textContent = won(ltd);
        document.getElementById('cgt-ltd-sub').textContent = '공제율 ' + ltdRate + '%';
        document.getElementById('cgt-base').textContent = won(base);
        document.getElementById('cgt-tax').textContent = won(tax);
        document.getElementById('cgt-tax-sub').textContent = rateLabel;
        document.getElementById('cgt-total').textContent = won(total);
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

## ✍️ 계산 예시로 확인하기

9억 원에 사서 15억 원에 판 아파트를 예로 들어 보겠습니다. 취득세·중개보수 같은 필요경비가 3,000만 원 들었다면 양도차익은 '15억 − 9억 − 3,000만 = 5억 7,000만 원'입니다.

이 집을 10년 보유하고 10년 실거주한 1세대 1주택이라면, 장기보유특별공제는 보유 40%에 거주 40%를 더해 최대 80%가 적용됩니다. 공제액은 '5억 7,000만 × 80% = 4억 5,600만 원'이고, 양도소득금액은 1억 1,400만 원으로 줄어듭니다. 기본공제 250만 원을 빼면 과세표준은 1억 1,150만 원, 세율 35% 구간이므로 산출세액은 '1억 1,150만 × 35% − 1,544만 = 2,358만 5,000원', 지방소득세를 더하면 약 2,594만 원입니다.

반대로 같은 집을 다주택 상태로 10년만 보유하고 살지 않았다면 일반 공제율 20%만 적용됩니다. 공제액은 1억 1,400만 원, 양도소득금액은 4억 5,600만 원, 과세표준은 4억 5,350만 원으로 세율 40% 구간에 들어가 산출세액이 '4억 5,350만 × 40% − 2,594만 = 1억 5,546만 원', 지방소득세까지 더하면 약 1억 7,100만 원에 이릅니다. 차익은 같아도 실거주 1주택이냐 아니냐에 따라 세금이 6배 넘게 벌어지는 셈입니다.

## 🧭 총평

양도소득세는 이익을 얼마 냈느냐 못지않게 어떻게, 얼마나 오래 갖고 있었느냐가 세액을 가릅니다. 보유 2년을 넘겨 단기세율을 피하고 실거주로 1세대 1주택 요건과 장기보유특별공제를 챙기는 것만으로도 부담이 확 달라집니다. 매도를 앞두고 있다면 파는 시점의 보유·거주 기간을 먼저 따져 보고, 필요경비 영수증을 미리 모아 두는 것이 절세의 출발점입니다. 위 계산기로 대략의 규모를 가늠한 다음, 감면·비과세 특례나 다주택 중과 여부는 확정 신고 전에 홈택스나 세무 전문가를 통해 꼭 확인하시기 바랍니다.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

**출처**

- [국세청 양도소득세 세액계산 흐름도](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2310&cntntsId=7709)
- [국세청 양도소득세 장기보유특별공제율](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2311&cntntsId=7710)
- [국세청 종합소득세(양도세 기본세율) 세율표](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2227&cntntsId=7667)
- [심플택스 2026 양도소득세율표·세법개정 비교](https://simpletax.kr/taxRate/transferTaxRate)
