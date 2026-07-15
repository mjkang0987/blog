---
layout: post
title: "🔐 Over 500 GitHub Access Tokens Leaked — Korean Police Issue Urgent Advisory: Revoke and Reissue Your PAT Now"
date: 2026-07-15 10:00:00 +0900
lang: en-US
permalink: /2026/07/15/github-pat-token-leak/
page_id: 2026-07-15-github-pat-token-leak
image: /assets/og/2026-07-15-github-pat-token-leak-en.png
summary: "Korea's National Office of Investigation confirmed a leak of over 500 GitHub personal access tokens (PATs) and issued an urgent security advisory. Private repos can be breached without an ID or password, so an immediate check is needed."
description: "Korea's National Office of Investigation confirmed a leak of over 500 GitHub personal access tokens (PATs) and issued an urgent security advisory. Private repos can be breached without an ID or password, so an immediate check is needed."
categories: [IT]
tags: [GitHub, PersonalAccessToken, PAT, TokenLeak, NationalOfficeOfInvestigation, SecurityAdvisory, DeveloperSecurity, MFA, MultiFactorAuth, SourceCodeLeak, SupplyChainSecurity, InfoSec, ITBriefing]
---

On July 14, Korea's National Office of Investigation (NOI), part of the Korean National Police Agency, confirmed that over 500 personal access tokens (PATs) used to sign in to GitHub had been leaked, and issued an urgent security advisory. Once such a token is handed over, an attacker can reach private repositories without knowing the ID or password — putting source code, corporate secrets, and personal data at risk together. If you are a developer or a company, the safe move is to check your access logs right now and reissue your tokens. Today we lay out what happened and how to respond. 🔐

**TL;DR**

- The NOI confirmed a leak of over 500 GitHub personal access tokens (PATs) and distributed a security advisory on July 14.
- A PAT grants access to private repositories without an ID or password, so a leak can lead to theft of source code and corporate information.
- The core guidance: review access logs from the past 1–3 months, and if you see signs of compromise, immediately revoke and reissue the affected tokens.

## 🚨 What Happened?

Access credentials for GitHub accounts leaked in bulk. On July 14, Korea's National Office of Investigation said it had confirmed that a large number of personal access tokens (PATs) used to sign in to GitHub were leaked, and that it is investigating. So far, about 500 accounts are known to have had their access credentials exposed; of those, 370-plus accounts across 54 countries have had their nationality identified, including roughly 30 domestic (Korean) accounts. The nationality of the remaining accounts is not yet confirmed.

The trail began with a separate cybercrime case. Police discovered that a suspect in an unrelated investigation was holding another person's GitHub token, which surfaced the leak; they identified it on July 9.

## 🔑 What Exactly Is a Personal Access Token (PAT)?

A personal access token is an authentication method used to reach private repositories or to sign in to GitHub from the command line and automation tools. It effectively acts as a key that stands in for an ID and password — and that is precisely what makes this leak dangerous.

Once a single line of token reaches an attacker's hands, they can access repositories without knowing the account's ID or password. The attacker can obtain not only the source code stored in the repository but also any other system access details written inside that code, widening the intrusion into a company's core systems. In other words, a single leaked token can lead straight to theft of source code, corporate secrets, and personal data.

## 🛡️ How Did GitHub and the Police Respond?

After confirming the leak, police promptly notified Microsoft, which operates GitHub, and shared information with Interpol. GitHub told police it had completed the necessary security measures, including revoking the leaked tokens and warning the affected users.

To prevent further damage, police distributed a security advisory to domestic companies and developers. Even with the operator's measures done, an individual user's own check is a separate matter — so you still need to verify your access logs and token status yourself.

## ✅ What Should You Do Now?

The most urgent steps are checking access logs and reissuing tokens. Here is the police guidance, in order.

First, check whether there has been any abnormal access over the past 1–3 months, and if you see signs of compromise, immediately revoke the existing personal access token and issue a new one. On top of that, apply multi-factor authentication (MFA) to access privileges, and narrow each account's permissions to the minimum. Not writing key system access details (passwords, keys, tokens, and the like) directly into source code is another basic rule. Finally, regularly check the security state of developer PCs to prevent the device holding the token from being breached first.

## 📝 Wrap-Up

This incident lays bare a trait of development environments where a single "token," not an ID and password, becomes the key to an entire account. With the leak spanning over 500 accounts — roughly 30 of them domestic — and the source code inside repositories along with the access details written into it potentially exposed, this is not something to take lightly. Even with steps taken by the operator and the police, checking individual accounts ultimately falls to the user, so it is best not to put off reviewing access logs, reissuing tokens, and applying multi-factor authentication.

※ This article is a security notice written for informational purposes.

**Sources**

- [Police: "Access credentials for 500-plus GitHub accounts leaked"… urgent security advisory (SBS, Korean)](https://news.sbs.co.kr/news/endPage.do?news_id=N1008656994)
- [Police confirm leak of numerous GitHub access tokens… urgent advisory (Asia Today, Korean)](https://www.asiatoday.co.kr/kn/view.php?key=20260714010005066)
- [Many GitHub personal access tokens leaked… police advise revoke/reissue of PATs (Digital Daily, Korean)](https://www.ddaily.co.kr/page/view/2026071414184235701)
- [MS GitHub "access credentials" leaked en masse… police open investigation (Money Today, Korean)](https://www.mt.co.kr/society/2026/07/14/2026071410063885156)
- [Police investigate mass leak of GitHub access tokens (The Korea Herald)](https://www.koreaherald.com/article/10808572)
- [South Korean Police Uncover Major GitHub Token Leak (Open Source For You)](https://www.opensourceforu.com/2026/07/south-korean-police-uncover-major-github-token-leak/)
