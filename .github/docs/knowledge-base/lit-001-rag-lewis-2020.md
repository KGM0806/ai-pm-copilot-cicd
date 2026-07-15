---
title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
owner: Product Manager
product_area: Literature
status: active
last_reviewed: 2026-07-14
document_type: public_literature_summary
confidentiality: public
source: arXiv
license: metadata-and-summary-only
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## 适用范围

本文档用于测试 RAG 知识库切片和文献摘要质量检查。本文只保存公开论文的元数据、来源链接、主题摘要和产品化解读，不保存论文全文。

该文献适合用于 AI 产品经理理解为什么知识库检索可以提高回答的事实性、具体性和可追溯性。

## 标准答案

核心观点总结：

- RAG 把参数化语言模型与非参数化知识检索结合起来。
- 模型生成回答前可以检索外部知识片段。
- 对知识密集型任务，检索增强可以帮助模型生成更具体、更有事实依据的内容。
- RAG 对开放域问答和知识密集型生成任务具有代表性意义。
- 对产品经理而言，RAG 说明了为什么 AI 产品不应只依赖模型自身记忆，而应设计可维护、可更新、可追溯的知识库。

产品化启发：

1. 知识库必须保留来源、标题、章节和更新时间。
2. 切片不能只追求长度均匀，还要保留语义边界。
3. 检索结果应能追溯回原始文档。
4. AI 输出应区分“检索依据”和“模型生成”。
5. 需要评估回答的事实性、相关性和引用准确性。

## 关键规则

- 不上传论文全文，只保存自写摘要和来源链接。
- 切片时必须保留 source、title、section、document_type。
- 文献知识块不得与 PRD 需求块混淆。
- 生成回答时应优先引用与问题直接相关的文献块。
- 如果知识块没有直接证据，AI 应提示依据不足。

## 示例

输入：

```text
为什么 AI 产品经理需要把 PRD 和知识库做成可追溯的 RAG 数据源？
```

期望输出摘要：

```text
RAG 的核心价值是把模型生成能力与外部知识检索结合，使回答能够基于可维护的外部资料。对于 PRD 和知识库场景，产品经理应保证每个知识块都有来源、章节、更新时间和适用范围，从而支持事实校验、版本管理和上线后追责。
```

## 相关链接

- arXiv: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- NeurIPS 2020 paper page
- docs/knowledge-base/prd-001-ai-requirement-analysis-assistant.md
