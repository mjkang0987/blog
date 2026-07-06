---
layout: post
title: "🤖 From OpenAI's 'Jalapeño' Onward — Big Tech's Custom AI-Chip Rush: Can It Shake Nvidia's Reign?"
date: 2026-07-06 19:00:00 +0900
lang: en-US
permalink: /2026/07/06/bigtech-custom-ai-silicon-rush/
page_id: 2026-07-06-bigtech-custom-ai-silicon-rush
image: /assets/og/2026-07-06-bigtech-custom-ai-silicon-rush-en.png
summary: "On June 24, OpenAI unveiled 'Jalapeño,' its first in-house inference chip, with Broadcom. From Google's 8th-gen TPUs to Qualcomm's rumored Tenstorrent deal, here's why Big Tech's custom-silicon rush is peaking now and what it means for Korean chipmakers."
description: "On June 24, OpenAI unveiled 'Jalapeño,' its first in-house inference chip, with Broadcom. From Google's 8th-gen TPUs to Qualcomm's rumored Tenstorrent deal, here's why Big Tech's custom-silicon rush is peaking now and what it means for Korean chipmakers."
categories: [IT]
tags: [OpenAI, Jalapeno, Broadcom, AIchips, CustomSilicon, ASIC, GoogleTPU, Qualcomm, Tenstorrent, Nvidia, HBM4, SKHynix, Samsung, AIinference, Semiconductors]
---

Big Tech's move to design its own AI chips is accelerating. On June 24, OpenAI unveiled 'Jalapeño,' its first in-house inference chip, together with Broadcom — and the cracks in an AI-infrastructure order long dependent on Nvidia GPUs are now clearly visible. Google has already shipped two 8th-generation in-house chips (TPUs), and Qualcomm has been swept up in acquisition rumors around an AI-chip startup. Today we look at why this 'custom silicon' contest is bunching up now, and what it means for Korea's chip industry. 🤖

**TL;DR**
- On June 24, OpenAI teamed up with Broadcom to unveil 'Jalapeño,' its first in-house inference chip. It took roughly nine months from design to tape-out — what the company calls the fastest high-performance ASIC development cycle ever.
- Google unveiled its 8th-gen TPUs in April (the 8t for training and 8i for inference), while Qualcomm was reported to be in talks to buy AI-chip startup Tenstorrent ($8–10 billion) — a claim the other side denied.
- The common thread is 'inference' optimization. As AI's demand center shifts from training to inference, more players are designing purpose-built chips of their own instead of relying on general-purpose GPUs.

## 🌶️ What Is OpenAI's 'Jalapeño'?

It is the first AI inference chip OpenAI has designed in-house. OpenAI and Broadcom unveiled 'Jalapeño' on June 24. It is the fruit of a collaboration in which OpenAI drew the blueprint from its experience with its own models and service operations, Broadcom handled silicon implementation, and Celestica handled the system.

There are two main features. First, development speed. It took about nine months from initial design to a manufacturing tape-out, which OpenAI described as being on par with the fastest ASIC development cycle in the history of high-performance semiconductors. Using its own AI models in the design and verification process is cited as a reason the pace was so quick. Second, power efficiency. In early testing, the company said performance-per-watt was substantially ahead of the best current alternatives. That said, these are the company's own announced figures, so real-world deployment performance bears watching.

Deployment begins late in 2026. OpenAI framed Jalapeño as the first step of a multi-generation computing platform and said it plans to begin deployment from year-end through data-center partners including Microsoft.

## 🏗️ Where Do Google and Qualcomm Stand?

Google has already shipped 8th-gen in-house chips, while Qualcomm is moving to secure AI-chip capability. On April 22, at Google Cloud Next, Google unveiled two 8th-gen TPUs. The 'TPU 8t' for training was designed by Broadcom and delivers, at superpod scale, 121 FP4 exaflops of compute from 9,600 chips, the company said. The 'TPU 8i' for inference was designed by MediaTek and is built in pods of 1,152 chips. Both chips are made on TSMC's 2nm process, with supply to customers outside Google targeted for late 2027.

On Qualcomm's side, it is still at the 'rumor' stage. On June 16, Reuters and others reported that Qualcomm was in talks to acquire AI-chip startup Tenstorrent for $8–10 billion. Tenstorrent, led by chip designer Jim Keller, builds AI chips based on the open RISC-V standard. However, on June 30, CEO Jim Keller denied that any acquisition talks with Qualcomm were underway, leaving the matter unconfirmed and not finalized.

## ⚡ Why 'In-House Chips' Now — From Training to Inference

The key backdrop is that AI computing's center of gravity is shifting from training to inference. AI-chip demand had long been concentrated on 'training' huge models. But as services move into real-world use, the 'inference' computation that answers user queries is rapidly taking up a larger share of the total load. For inference, power efficiency and cost matter as much as raw compute — because the work repeats at massive scale, even a small gain in performance-per-watt yields big savings in operating costs.

This is where the appeal of purpose-built chips (ASICs) grows. A general-purpose GPU handles a wide range of tasks but can be wasteful on specific inference workloads. A chip designed to fit one's own models, by contrast, can pick out only the needed computations and optimize for them, giving it an edge on power and cost. That is why OpenAI and Google alike lead with 'inference' optimization. Layered on top is the strategic calculation of reducing dependence on any single supplier.

## 🇰🇷 Crisis or Opportunity for Korean Chips?

For now, the opportunity outweighs the risk. It is true that the in-house-chip rush shakes the Nvidia-centered order, but these custom chips still need high-bandwidth memory (HBM), advanced packaging, and foundry contract manufacturing to be completed. The structure — with Broadcom and MediaTek rising as OpenAI's and Google's chip-design partners and TSMC handling actual production — reflects this very trend.

For Korean firms, it means memory and back-end demand holds up. Whether an AI chip is a GPU or a custom ASIC, high-performance computing requires HBM. Indeed, the HBM4-generation contest is heating up; some market forecasts put 2026 HBM4 share at roughly 54–55% for SK Hynix, 28–29% for Samsung, and 17–18% for Micron. These are forecasts that differ by source, however, so they should not be treated as fixed figures. At the same time, the U.S. Semiconductor Industry Association and others suggest that 2026 global semiconductor market revenue could top $1 trillion for the first time.

## 🧭 The Takeaway — A Turning Point for the 'GPU-Monopoly Era'

In sum, Big Tech's custom AI-chip rush is a signal that the center of gravity of AI infrastructure is shifting from training to inference, and from general-purpose to purpose-built. OpenAI's Jalapeño is the latest emblem of this trend, Google's TPUs are already a generation ahead, and Qualcomm's move still needs confirming.

Three points to watch. First, whether these in-house chips deliver their promised performance once actually deployed — announced numbers and field performance can differ. Second, how far custom chips will substitute for or complement Nvidia, which still commands an overwhelming ecosystem. Third, how Korea's memory and foundry industries will hold their place in the supply chain amid this change. Either way, one thing seems clear: the AI-hardware market, once served by 'one GPU for everything,' is standing at a fork that splits into many branches.

※ This article is for informational purposes only and is not investment advice.

**Sources**
- [OpenAI and Broadcom unveil LLM-optimized inference chip (OpenAI)](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)
- [OpenAI and Broadcom Unveil LLM-Optimized Intelligence Processor (Broadcom)](https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor)
- [OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership (CNBC)](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
- [OpenAI unveils its first custom chip, built by Broadcom (TechCrunch)](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
- [Our eighth generation TPUs: two chips for the agentic era (Google)](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
- [Qualcomm in Talks to Acquire AI Chip Startup Tenstorrent for Up to $10 Billion (Reuters via Yahoo)](https://finance.yahoo.com/technology/ai/articles/qualcomm-talks-acquire-ai-chip-230401789.html)
- [Tenstorrent CEO Denies Qualcomm Acquisition Talks (GuruFocus)](https://www.gurufocus.com/news/8938157/tenstorrent-ceo-denies-qualcomm-acquisition-talks-amid-focus-on-ai-development)
