---
title: Self-RAG Learning to Retrieve Generate and Critique through Self-Reflection
owner: Product Manager
product_area: Literature
status: active
last_reviewed: 2026-07-14
document_type: public_literature_summary
confidentiality: public
source: arXiv
license: metadata-and-summary-only
---

# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

## 适用范围

本文档用于测试文献型知识块的切片、质量审查和 AI 产品设计启发。本文只保存公开论文的元数据、来源链接、主题摘要和产品化解读，不保存论文全文。

该文献适合用于设计带有“是否需要检索、检索结果是否相关、回答是否有依据”判断能力的 AI 产品流程。

## 标准答案

核心观点总结：

- Self-RAG 关注检索增强生成中的自我反思能力。
- 系统不应在所有场景中固定检索相同数量的文档，而应判断是否需要检索。
- 生成过程中可以对检索片段和模型回答进行评价。
- 该思路启发 AI 产品经理设计更可控的 RAG 工作流，包括检索必要性判断、证据相关性判断和回答质量判断。
- 对知识库产品而言，质量测试不应只检查有没有切片，还要检查检索是否命中正确片段、回答是否引用正确依据。

产品化启发：

1. 在回答前增加“是否需要检索”的判断节点。
2. 在检索后增加“证据是否相关”的评价节点。
3. 在输出前增加“回答是否被证据支持”的审查节点。
4. 对低置信度回答提供澄清问题或拒答策略。
5. 用测试集评估 citation accuracy、answer relevance 和 groundedness。

## 关键规则

- 不上传论文全文，只保存自写摘要和来源链接。
- 知识库切片必须支持 evidence_id 或 chunk_id。
- 测试时必须区分“检索正确”和“回答正确”。
- 当检索结果不足时，AI 不应强行编造答案。
- 质量报告应输出命中率、相关性和证据支持度。

## 示例

输入：

```text
如何判断一个知识库问答系统是否真的引用了正确依据？
```

期望输出摘要：

```text
可以把测试拆成三层：第一层检查是否检索到正确知识块；第二层检查回答是否使用了这些知识块；第三层检查回答中的关键结论是否被证据支持。Self-RAG 的启发是让系统具备检索、生成和自我评价的流程，而不是只做单次检索和直接生成。
```

## 相关链接

- arXiv: Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- ICLR 2024 paper page
- docs/knowledge-base/lit-001-rag-lewis-2020.md
