---
layout: post
title: "🤖 AIが「仕事」を代わりにこなす時代 — OpenAI『ChatGPT Work』が開く自律エージェントの幕開け"
date: 2026-07-12 07:00:00 +0900
lang: ja
permalink: /2026/07/12/openai-chatgpt-work-agent-era/
page_id: 2026-07-12-openai-chatgpt-work-agent-era
image: /assets/og/2026-07-12-openai-chatgpt-work-agent-era-ja.png
summary: "OpenAIが7月9日、自律エージェント『ChatGPT Work』を公開。GPT-5.6を基盤に数時間ひとりで作業し、シート・スライド・文書・Webアプリの完成物を返します。料金は定額ではなく従量制です。"
description: "OpenAIが7月9日、自律エージェント『ChatGPT Work』を公開。GPT-5.6を基盤に数時間ひとりで作業し、シート・スライド・文書・Webアプリの完成物を返します。料金は定額ではなく従量制です。"
categories: [IT]
tags: [OpenAI, ChatGPTWork, AIエージェント, 自律エージェント, GPT-5.6, Codex, 生成AI, 人工知能, 業務自動化, Grok4.5, エンタープライズAI, AIニュース, ChatGPT, エージェントAI, AIエージェント戦争]
---

OpenAIが7月9日（現地時間）、『ChatGPT Work』を発表しました。人が任せた仕事を何時間でも自分で処理し、文書やシート、スライドといった完成物として返す自律エージェントです。質問に答えるだけだったチャットボットが、実際の業務を代わりにこなす段階へと進んだことになります。先週のGPT-5.6モデルに続き、それを業務ツールへと変えた後継作である以上、今日はChatGPT Workとは何か、どのように働き料金はどう決まるのか、企業導入や競争構図はどう変わるのかを整理していきます。🤖

**要点（TL;DR）**

- OpenAIが7月9日、『ChatGPT Work』を公開しました。GPT-5.6を基盤に、連携したアプリやファイルから情報を引き出し、数時間かけて自分で作業を分割して進め、その結果をシート・スライド・文書・Webアプリといった完成物として提示します。
- 料金は定額制に含まれる機能ではなく、コーディングツール『Codex』のように使用量に応じて課金される仕組みです。入力・キャッシュされた入力・出力のトークンにそれぞれ異なる料率がかかり、長く動かすほど費用が増えます。
- まずはPro・Enterprise・Eduプランに先行して開放され、その後Plus・Businessへ広がります。管理者向けの支出管理やエージェントの行動制限といった企業向けの安全装置も併せて提供されます。

## 🤖 ChatGPT Workは何が違うのか — 「会話」ではなく「完成物」

ChatGPT Workの核心は、答えではなく仕上がった成果物を出す点にあります。従来のチャットボットは質問にテキストで答えていましたが、ChatGPT Workは目標を受け取ると、ユーザーのアプリやファイルから文脈を引き出し、レポートやスプレッドシート、プレゼンテーションや文書はもちろん、共有可能なWebアプリまで作り上げます。OpenAIはこの成果物を「チャットではなく完成した資料」と表現しました。

動作基盤は、先週正式リリースされたGPT-5.6です。OpenAIはこのモデルを、フラッグシップの「Sol」、バランス型の「Terra」、高速・低価格の「Luna」の3種類として投入しましたが、ChatGPT Workはその性能を実際の業務成果物へとつなぐ役割を担います。Web、モバイル、デスクトップなどChatGPTが動く環境のどこでも利用できます。

## ⏱️ 数時間ひとりで働く — 自律エージェントの動く仕組み

最大の変化は、人がずっと張り付いていなくてもよい点です。ChatGPT Workは複雑なプロジェクトを小さな段階に分け、数時間にわたり自分で進めます。途中で必要な情報は、連携した業務アプリやファイルから直接取得します。ユーザーが望む「結果」だけを示せば、そこに至る過程はエージェントが自分でたどっていく構造です。

このやり方は、コーディング補助ツールCodexの流れに似ています。実際にOpenAIは、ChatGPT Workが「通常のチャット要求より長く複雑な作業を狙って設計された」と説明し、Codexと同じ使用構造に従うと明かしました。複数の海外メディアはこれを、事務職の人でもコーディングツールが備える自動化の力を、難しい学習過程なしに使えるようになったと評価しています。

## 💳 料金が見慣れない — 定額ではなく「使った分だけ」課金

注意して見るべき点は料金の方式です。ChatGPT Workは購読料に単純に乗っている機能ではなく、実行するたびにトークン使用量に応じて費用がかかります。OpenAIは入力トークン、キャッシュされた入力トークン、出力トークンにそれぞれ異なる料率を設定して課金すると説明しました。エージェントが長く働くほど、扱う資料が多いほど費用が大きくなるわけです。

参考までに、ChatGPT Workを動かすGPT-5.6のAPI価格は100万トークン基準で、Solが入力5ドル・出力30ドル、Terraが2.5ドル・15ドル、Lunaが1ドル・6ドルです。定額料金の中で無制限に使っていた感覚とは異なり、自律エージェントは「作業単位」で費用が決まる点を、導入前に見極める必要があります。

## 🏢 企業がまず注目する — 管理者の統制と安全装置

企業導入を念頭に置いた統制の仕組みが併せて入った点も注目に値します。OpenAIはEnterprise・Eduの管理者に支出管理機能を提供します。ワークスペースの既定値やグループ別の上限、個人別の例外設定、クレジット追加の申請・承認の流れなどを管理コンソールで扱えます。

エージェントが各アプリでどんな行動を取れるかを管理者が制限する安全装置も用意されました。自律的に動くエージェントが実際の業務システムにアクセスする以上、費用の統制と権限の管理が導入の前提条件になる点を、OpenAIも認識しているとみられます。利用範囲はまずPro・Enterprise・Eduで開放され、その後Plus・Businessプランへ順次広がります。

## 🥊 OpenAIだけの話ではない — 「AIエージェント戦争」の序幕

ChatGPT Workは、業界全体の「エージェント競争」の流れの真ん中に置かれています。7月9日前後に主要なAI企業が相次いで新モデルやツールを投入し、単純な対話型チャットボットを超えて「仕事を代わりに処理するAI」へと競争の軸が移っていく姿が見えます。イーロン・マスク氏のxAIは同じ日に「Grok 4.5」を公開し、Metaも自社の最新モデルを前面に攻めの価格戦略を予告したと伝えられています。

こうした流れは、AI産業の重心が「モデルの性能」から「モデルが実際にこなす業務」へと移りつつあることを示します。ただし、自律エージェントがどれほど正確かつ安定して仕事を仕上げるのか、実際の業務現場で信頼を得られるのかは、今後の検証が必要な部分です。

## 総評

ChatGPT Workの登場は、AIが「答えるツール」から「働くツール」へ移る分岐点を象徴します。数時間ひとりで作業を続けて完成物を出す点、そしてそれに合わせて料金が定額から従量制へ変わる点が、前世代のチャットボットと最も大きく変わった箇所です。

押さえておきたい点は三つです。第一に、従量制の課金は利便性と同じだけ費用管理の負担も抱えさせます。導入前に想定使用量と上限設定を必ず点検する必要があります。第二に、自律エージェントが業務システムにアクセスする以上、権限とセキュリティの管理が導入の核心的な課題になります。第三に、OpenAIだけでなく複数の企業が同じ方向へ動いている以上、エージェントの性能と安定性を実際の業務で検証する流れが下半期を通じて続く見通しです。

※ 本記事は情報提供を目的としたものであり、投資助言ではありません。

**出典**

- [OpenAI Launches ChatGPT Work Agent to Handle Complex Tasks (Bloomberg)](https://www.bloomberg.com/news/articles/2026-07-09/openai-unveils-chatgpt-work-agent-to-field-tasks-for-hours)
- [OpenAI Debuts ChatGPT Work Workplace AI Agent With GPT-5.6 (Forbes)](https://www.forbes.com/sites/madhulika-pathak/2026/07/09/openai-debuts-chatgpt-work-workplace-ai-agent-with-gpt-56/)
- [OpenAI unveils ChatGPT Work agent, GPT-5.6 models now available (9to5Mac)](https://9to5mac.com/2026/07/09/openai-announcing-the-next-chapter-for-chatgpt-today-watch-here/)
- [OpenAI Debuts ChatGPT Work Agent and New GPT-5.6 Models (MacRumors)](https://www.macrumors.com/2026/07/09/openai-chatgpt-work/)
- [OpenAI Launches ChatGPT Agent That Executes Complex Workflows (PYMNTS)](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-chatgpt-agent-that-executes-complex-workflows/)
