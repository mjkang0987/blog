---
layout: post
title: "🟢 NVIDIA Just 'Open-Sourced' Its Own AI Models — A Full Guide to Nemotron 3, With Weights, Data and Recipes"
date: 2026-07-03 19:00:00 +0900
lang: en-US
permalink: /2026/07/03/nvidia-nemotron3-open-models/
page_id: 2026-07-03-nvidia-nemotron3-open-models
image: /assets/og/2026-07-03-nvidia-nemotron3-open-models-en.png
summary: "NVIDIA has released its own Nemotron 3 AI models as open models — weights, training data and recipes under a permissive license. Here's the Nano/Super/Ultra lineup and what 'free and open' really means."
description: "NVIDIA has released its own Nemotron 3 AI models as open models — weights, training data and recipes under a permissive license. Here's the Nano/Super/Ultra lineup and what 'free and open' really means."
categories: [IT]
tags: [NVIDIA, Nemotron, Nemotron3, OpenModels, OpenSourceAI, OpenWeights, HuggingFace, AgenticAI, JensenHuang, LLM, Blackwell, MoE, GenerativeAI, AIChips, TechBriefing]
---

NVIDIA has released its in-house AI model family, "Nemotron 3," as open models. It posted not only the model weights but also the training data and training recipes on Hugging Face, under a permissive license that allows commercial use. In this evening briefing, we look at why a company that sells GPUs would open its own AI models this far — and exactly how "free and open" they really are.

## 📌 TL;DR

- NVIDIA Nemotron 3 is an open model family in three sizes — Nano, Super and Ultra. It first debuted on December 15, 2025, and the largest, Ultra, arrived on June 4, 2026.
- The weights, training data and training recipes are all available on Hugging Face, under the permissive open license OpenMDW-1.1, which allows commercial use, fine-tuning and redistribution.
- The stated goal is "transparent, efficient agentic AI." Key traits include a hybrid Mamba-Transformer MoE architecture and a context window of up to 1 million tokens.

## 🧭 What exactly is Nemotron 3?

Nemotron 3 is an open-weight AI model family built in-house by NVIDIA. When NVIDIA first unveiled the family on December 15, 2025, it described them as efficient open models tuned for "multi-agent" work in which several AI agents collaborate. CEO Jensen Huang said "open innovation is the foundation of AI progress," and that with Nemotron the company aims to turn advanced AI into an open platform that gives developers the transparency and efficiency they need.

Structurally, it uses a hybrid Mamba-Transformer MoE (mixture-of-experts) architecture. During inference it activates only some of the "experts" among all parameters, lowering compute cost. It supports long contexts of up to 1 million tokens and lets you adjust the reasoning budget at inference time. The design aims to boost agentic, reasoning and conversational performance together.

## 🔓 How "free and open" is it? — The license is the crux

The heart of "free and open" is that the model weights and training assets are genuinely public, and commercial use is permitted. Along with the weights, Nemotron 3 released the training data (for the portion NVIDIA holds redistribution rights to) and the training recipes. You can download these assets from the "NVIDIA Nemotron v3" collection on Hugging Face and verify them yourself before deploying.

The license is the open OpenMDW-1.1. It allows commercial use and fine-tuning, and you can also redistribute as long as you provide attribution. That said, "open" does not mean "anything goes with no restrictions." The scope of the released data is limited to the parts NVIDIA has redistribution rights to, and you must observe license terms such as attribution. Even so, compared with closed commercial APIs, the gains in transparency and freedom to self-host are clear.

## 📊 How do Nano, Super and Ultra differ?

The three models differ in size and purpose. The idea is to pick one that fits the scale of your task.

- **Nemotron 3 Nano**: A small model with about 30 billion total parameters (30B; 31.6B to be exact) that activates up to 3 billion (3B) at a time. Released first, on December 15, 2025, it's optimized for cost-sensitive tasks like software debugging, content summarization and information retrieval. According to NVIDIA, it delivers up to 4x higher token throughput than the previous-generation Nemotron 2 Nano and cuts reasoning-token generation by up to 60%.
- **Nemotron 3 Super**: A high-accuracy reasoning model with about 100 billion (100B) parameters, activating up to 10 billion (10B) per token. It targets high-volume workloads where many agents collaborate, such as IT ticket automation.
- **Nemotron 3 Ultra**: A large reasoning engine with about 500 billion (~550B) parameters, activating up to 50 billion (~55B) per token. Released on June 4, 2026, it aims at complex workflows that demand deep research and strategic planning. Super and Ultra are trained with NVIDIA's 4-bit NVFP4 format on the Blackwell architecture, cutting memory requirements and speeding up training.

## 🛠️ What changes for developers? — Data and tools are open too

NVIDIA released not just the models but also the data and tools needed to build specialized AI agents. It put out new datasets totaling 3 trillion (3T) tokens for pre-training, post-training and reinforcement learning, and also released a "Nemotron Agentic Safety Dataset" for evaluating and strengthening the safety of complex agent systems. On top of that, it published open-source libraries on GitHub and Hugging Face: NeMo Gym for training environments, NeMo RL for post-training, and NeMo Evaluator for validating model safety and performance.

Several companies are already adopting it. According to NVIDIA, Accenture, CrowdStrike, Cursor, Deloitte, Oracle Cloud Infrastructure, Palantir, Perplexity, ServiceNow, Siemens, Synopsys and Zoom are integrating Nemotron-family models into AI workflows across manufacturing, cybersecurity, software development and more. On the deployment side, major runtimes such as LM Studio, llama.cpp, SGLang and vLLM support Nemotron 3, making it easier to run on your own infrastructure.

## 🌐 What's the broader open-ecosystem trend?

The Nemotron 3 release sits at the center of NVIDIA's broader push to expand the open-model ecosystem. Beyond its own models, NVIDIA is extending optimized, Blackwell-tuned builds of popular open-source models like DeepSeek, Qwen and GLM. For example, on June 26, 2026, it published on Hugging Face a checkpoint of Zhipu AI's GLM-5.2 quantized with its own NVFP4 (4-bit) format, shrinking the roughly 1.5TB FP8 original to around 410GB (about a 70% reduction) while keeping accuracy nearly intact. The strategy is to make open-source models run best on NVIDIA GPUs, raising the value of the hardware in the process.

## 🧩 Bottom line — What to watch

Nemotron 3 is an open model family that goes beyond "weights only" to also open the training data, recipes and development tools. It opened with Nano in December 2025 and filled out the lineup through Ultra in June 2026, and its commercial-use license widens the room for enterprises and developers to verify and operate the models on their own infrastructure. Still, the true scope of "open" must be understood within the license terms and the extent of data disclosure. When adopting the models, keep in mind that the performance and cost benefits can shift depending on the active-parameter size and whether your workload's bottleneck is memory or decoding speed. The big question ahead is how this decision — a GPU company opening its models too — will reshape the competitive landscape of open AI.

※ This article is for informational purposes only and is not investment advice.

## 🔗 Sources

- [NVIDIA Debuts Nemotron 3 Family of Open Models (NVIDIA Newsroom)](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)
- [NVIDIA Nemotron 3 Family of Models (research.nvidia.com)](https://research.nvidia.com/labs/nemotron/Nemotron-3/)
- [NVIDIA Nemotron v3 Collection (Hugging Face)](https://huggingface.co/collections/nvidia/nvidia-nemotron-v3)
- [NVIDIA Nemotron: Advanced Multimodal AI Models (nvidia.com)](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
- [NVIDIA Releases 4-bit Quantized 'GLM-5.2' (AI Times)](https://www.aitimes.com/news/articleView.html?idxno=212178)
