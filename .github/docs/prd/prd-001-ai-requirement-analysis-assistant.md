---
title: AI Requirement Analysis Assistant PRD
owner: Product Manager
product_area: PRD
status: active
last_reviewed: 2026-07-14
document_type: simulated_prd
confidentiality: public-demo
source: self-created
license: portfolio-demo
---

# AI Requirement Analysis Assistant PRD

## 适用范围

本文档用于测试 AI Product Manager Copilot 的知识库切片、PRD 结构审查和质量评估能力。该模拟 PRD 描述一个面向产品经理的需求分析助手，帮助用户把模糊业务需求转化为结构化需求分析草稿。

## 标准答案

系统应支持用户输入一段原始需求，并输出结构化分析结果，包括：

- 业务背景
- 目标用户
- 用户故事
- 功能范围
- 用户流程
- 验收标准
- 成功指标
- 风险与约束
- 下一步澄清问题

核心功能包括：

1. 需求理解：识别用户输入中的业务目标、对象、场景和约束。
2. PRD 草稿生成：按固定模板生成初版 PRD。
3. 验收标准生成：把模糊描述转化为可验证的 Given / When / Then。
4. 风险识别：输出产品、技术、数据和运营风险。
5. 追问建议：当输入信息不足时，给出澄清问题。

## 关键规则

- 不允许把 AI 输出直接视为最终 PRD。
- 需求过于模糊时，必须先生成澄清问题。
- 验收标准必须尽量可测试、可判断、可复现。
- 输出必须保留假设说明，不能伪造业务事实。
- 风险必须至少覆盖产品风险、技术风险和运营风险。
- 用户可以修改 AI 生成结果后再进入人工评审流程。

## 示例

输入：

```text
我们想做一个能帮产品经理快速分析需求的 AI 助手。
```

期望输出摘要：

```text
业务背景：产品经理经常收到模糊需求，需要快速拆解业务目标、用户场景和验收标准。
目标用户：B端产品经理、AI产品经理、解决方案产品经理。
核心功能：需求理解、PRD草稿生成、验收标准生成、风险识别、澄清问题生成。
验收标准：当用户输入原始需求时，系统必须输出业务背景、用户故事、功能范围、验收标准、风险与下一步问题。
风险：AI可能误解业务上下文，需要人工确认。
```

## 相关链接

- docs/prd/001-requirement-analysis.md
- docs/uat/001-requirement-analysis-uat.md
- prompts/requirement-analysis.prompt.md
