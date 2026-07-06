---
layout: post
title: "🤖 오픈AI '할라피뇨'까지 — 빅테크 '자체 AI 칩' 러시, 엔비디아 독주 흔들까"
date: 2026-07-06 19:00:00 +0900
lang: ko
permalink: /2026/07/06/bigtech-custom-ai-silicon-rush/
page_id: 2026-07-06-bigtech-custom-ai-silicon-rush
image: /assets/og/2026-07-06-bigtech-custom-ai-silicon-rush-ko.png
summary: "오픈AI가 6월 24일 브로드컴과 첫 자체 추론 칩 '할라피뇨'를 공개했습니다. 구글 8세대 TPU, 퀄컴의 텐스토렌트 인수설까지, 빅테크의 '커스텀 실리콘' 러시가 왜 몰려 나오는지와 한국 반도체에 주는 의미를 짚어봅니다."
description: "오픈AI가 6월 24일 브로드컴과 첫 자체 추론 칩 '할라피뇨'를 공개했습니다. 구글 8세대 TPU, 퀄컴의 텐스토렌트 인수설까지, 빅테크의 '커스텀 실리콘' 러시가 왜 몰려 나오는지와 한국 반도체에 주는 의미를 짚어봅니다."
categories: [IT]
tags: [오픈AI, 할라피뇨, 브로드컴, AI반도체, 커스텀실리콘, ASIC, 구글TPU, 퀄컴, 텐스토렌트, 엔비디아, HBM4, SK하이닉스, 삼성전자, AI추론, 반도체]
---

빅테크가 AI 칩을 직접 설계하는 흐름이 빨라지고 있습니다. 오픈AI가 6월 24일 브로드컴과 함께 첫 자체 추론 칩 '할라피뇨(Jalapeño)'를 공개하면서 엔비디아 GPU에 기대던 AI 인프라 구도에도 균열 조짐이 뚜렷해졌습니다. 구글은 이미 8세대 자체 칩(TPU) 두 종을 내놨고, 퀄컴은 AI 칩 스타트업 인수설에 휩싸였습니다. 오늘은 이 '커스텀 실리콘' 경쟁이 왜 지금 몰려 나오는지, 한국 반도체에는 어떤 의미인지 짚어보겠습니다. 🤖

**핵심 요약(TL;DR)**
- 오픈AI가 6월 24일 브로드컴과 손잡고 첫 자체 추론 칩 '할라피뇨'를 공개했습니다. 설계부터 테이프아웃까지 약 9개월이 걸렸는데, 회사 측은 역대 가장 빠른 고성능 ASIC 개발 주기라고 밝혔습니다.
- 구글은 4월 8세대 TPU(훈련용 8t·추론용 8i)를 공개했고, 퀄컴은 AI 칩 스타트업 텐스토렌트 인수설(80억~100억 달러)이 돌았으나 상대 측이 이를 부인했습니다.
- 공통점은 '추론(Inference)' 최적화입니다. AI 수요 축이 학습에서 추론으로 옮겨가면서, 범용 GPU 대신 용도별 맞춤 칩을 직접 설계하려는 움직임이 커지고 있습니다.

## 🌶️ 오픈AI '할라피뇨'는 무엇인가

오픈AI가 처음으로 자체 설계한 AI 추론 전용 칩입니다. 오픈AI와 브로드컴은 6월 24일 '할라피뇨(Jalapeño)'를 공개했습니다. 오픈AI가 자사 모델과 서비스 운영 경험을 바탕으로 밑그림을 그리고, 브로드컴이 반도체 구현을, 셀레스티카가 시스템을 맡은 협업 결과물입니다.

특징은 크게 두 가지입니다. 첫째는 개발 속도입니다. 초기 설계부터 제조용 테이프아웃까지 약 9개월이 걸렸는데, 오픈AI는 이를 고성능 반도체 사상 가장 빠른 ASIC 개발 주기 수준이라고 설명했습니다. 자체 AI 모델을 설계·검증 과정에 활용한 점이 속도를 끌어올린 배경으로 꼽힙니다. 둘째는 전력 효율입니다. 초기 테스트에서 와트당 성능이 현존 최고 수준 대안보다 상당히 앞선다고 밝혔습니다. 다만 이는 회사 측 자체 발표 수치인 만큼 실제 도입 성능은 지켜볼 필요가 있습니다.

배치 시점은 2026년 말부터입니다. 오픈AI는 할라피뇨를 여러 세대에 걸친 컴퓨팅 플랫폼의 첫 단추로 규정했고, 마이크로소프트 등 데이터센터 파트너와 함께 연말부터 배치를 시작할 계획이라고 전했습니다.

## 🏗️ 구글·퀄컴은 어디까지 왔나

구글은 이미 8세대 자체 칩을 내놨고, 퀄컴은 AI 칩 역량 확보에 나선 상황입니다. 구글은 4월 22일 구글 클라우드 넥스트에서 8세대 TPU 두 종을 공개했습니다. 훈련용 'TPU 8t'는 브로드컴이 설계를 맡았고, 슈퍼팟 기준 9,600개 칩으로 121 FP4 엑사플롭스의 연산 성능을 낸다고 밝혔습니다. 추론용 'TPU 8i'는 미디어텍이 설계했으며 1,152개 칩 단위 팟으로 구성됩니다. 두 칩 모두 TSMC 2나노 공정에서 만들어지며, 구글 외 고객 대상 공급은 2027년 말을 목표로 합니다.

퀄컴 쪽은 아직 '설(說)' 단계입니다. 6월 16일 로이터 등은 퀄컴이 AI 칩 스타트업 텐스토렌트를 80억~100억 달러에 인수하는 협상을 벌이고 있다고 보도했습니다. 텐스토렌트는 반도체 설계자 짐 켈러가 이끄는 회사로, 개방형 RISC-V 표준 기반 AI 칩을 만듭니다. 다만 6월 30일 짐 켈러 최고경영자가 퀄컴과의 인수 협상 사실을 부인하면서, 이 사안은 아직 확정되지 않은 미확인 단계로 남아 있습니다.

## ⚡ 왜 지금 '자체 칩'인가 — 학습에서 추론으로

AI 연산의 무게중심이 학습에서 추론으로 옮겨가고 있다는 것이 핵심 배경입니다. 그동안 AI 칩 수요는 거대 모델을 '학습(Training)'시키는 데 집중됐습니다. 그러나 서비스가 실사용 단계로 넘어오면서, 이용자 질문에 답하는 '추론(Inference)' 연산이 전체 부하에서 차지하는 비중이 빠르게 커지고 있습니다. 추론은 연산 성능 못지않게 전력 효율과 비용이 중요합니다. 대규모로 반복되는 작업이라 와트당 성능을 조금만 개선해도 운영비 절감 효과가 크기 때문입니다.

여기서 '용도별 맞춤 칩(ASIC)'의 매력이 커집니다. 범용 GPU는 다양한 작업을 두루 처리하는 대신 특정 추론 작업에서는 낭비가 생기기도 합니다. 반면 자사 모델에 맞춰 직접 설계한 칩은 필요한 연산만 골라 최적화하므로 전력·비용 측면에서 유리합니다. 오픈AI와 구글이 나란히 '추론' 최적화를 앞세운 이유입니다. 여기에 특정 공급사 의존도를 낮추려는 전략적 계산도 깔려 있습니다.

## 🇰🇷 한국 반도체에는 위기인가 기회인가

당장은 위기보다 기회 요인이 더 큰 것으로 평가됩니다. 자체 칩 러시가 엔비디아 중심 구도를 흔드는 것은 맞지만, 이들 맞춤 칩도 결국 고대역폭 메모리(HBM)와 첨단 패키징, 파운드리 위탁생산이 있어야 완성됩니다. 오픈AI·구글의 칩 설계 파트너로 브로드컴·미디어텍이 부상하고 실제 생산은 TSMC가 맡는 구조도 이런 흐름을 보여줍니다.

한국 기업에는 메모리·후공정 수요가 유지된다는 의미가 있습니다. AI 칩이 GPU든 맞춤형 ASIC이든, 고성능 연산에는 HBM이 필수적이기 때문입니다. 실제로 HBM4 세대 경쟁이 본격화되고 있으며, 일부 시장 전망은 2026년 HBM4 점유율을 SK하이닉스 54~55%, 삼성전자 28~29%, 마이크론 17~18% 안팎으로 봅니다. 다만 이는 전망치라 출처마다 차이가 있어 확정된 수치로 보기는 어렵습니다. 동시에 미국 반도체산업협회 등은 2026년 세계 반도체 시장 매출이 사상 처음 1조 달러를 넘어설 가능성을 제기하고 있습니다.

## 🧭 총평 — 'GPU 독점 시대'의 분기점

정리하면, 빅테크의 자체 AI 칩 러시는 AI 인프라의 무게중심이 학습에서 추론으로, 범용에서 맞춤형으로 이동하고 있음을 보여주는 신호입니다. 오픈AI 할라피뇨는 이 흐름을 상징하는 최신 사례이고, 구글 TPU는 이미 한 세대 앞서 있으며, 퀄컴의 행보는 아직 확인이 필요합니다.

짚어볼 포인트는 세 가지입니다. 첫째, 자체 칩이 실제 배치 뒤 공언한 성능을 낼지입니다. 발표 수치와 현장 성능은 다를 수 있습니다. 둘째, 엔비디아가 여전히 압도적 생태계를 가진 상황에서 맞춤 칩이 어느 정도 대체·보완 역할을 할지입니다. 셋째, 한국 메모리·파운드리 업계가 이 변화 속에서 공급망 내 위치를 어떻게 지켜갈지입니다. 어느 쪽이든, 'GPU 하나로 통하던' AI 하드웨어 시장이 여러 갈래로 나뉘는 분기점에 서 있다는 점만은 분명해 보입니다.

※ 본 글은 정보 제공 목적이며 투자 조언이 아닙니다.

**출처**
- [OpenAI and Broadcom unveil LLM-optimized inference chip (OpenAI)](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
- [OpenAI and Broadcom Unveil LLM-Optimized Intelligence Processor (Broadcom)](https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor)
- [OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership (CNBC)](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
- [OpenAI unveils its first custom chip, built by Broadcom (TechCrunch)](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
- [Our eighth generation TPUs: two chips for the agentic era (Google)](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
- [Qualcomm in Talks to Acquire AI Chip Startup Tenstorrent for Up to $10 Billion (Reuters via Yahoo)](https://finance.yahoo.com/technology/ai/articles/qualcomm-talks-acquire-ai-chip-230401789.html)
- [Tenstorrent CEO Denies Qualcomm Acquisition Talks (GuruFocus)](https://www.gurufocus.com/news/8938157/tenstorrent-ceo-denies-qualcomm-acquisition-talks-amid-focus-on-ai-development)
