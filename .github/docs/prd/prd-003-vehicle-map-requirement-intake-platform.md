---
title: Vehicle Map Requirement Intake Platform PRD
owner: Product Manager
product_area: PRD
status: active
last_reviewed: 2026-07-14
document_type: simulated_prd
confidentiality: public-demo
source: self-created
license: portfolio-demo
---

# Vehicle Map Requirement Intake Platform PRD

## 适用范围

本文档用于测试车机地图 B2B 需求管理场景。该模拟 PRD 描述一个面向车企、地图供应商和内部产品团队的需求准入与评审平台。

## 标准答案

平台目标是把来自车企客户、地图服务商、测试团队和内部产品团队的地图相关需求统一收口，形成可追踪、可评审、可验收的需求闭环。

主要角色包括：

- 车企产品经理
- 地图供应商产品经理
- 后端开发
- 车机端开发
- 测试工程师
- 项目经理

核心模块包括：

1. 需求提交：支持按车型、版本、地图模块、优先级提交需求。
2. 需求澄清：支持补充场景、影响范围、验收标准和依赖方。
3. 评审流程：支持 PM、研发、测试、地图供应商联合评审。
4. 版本关联：把需求绑定到车机系统版本和地图数据版本。
5. UAT 验收：支持测试用例、验收结果和遗留问题记录。
6. 发布追踪：支持上线状态、回滚方案和客户确认记录。

## 关键规则

- 每个需求必须绑定车型、软件版本、地图模块和验收标准。
- 需求未通过评审前不能进入开发状态。
- 涉及导航、安全提醒和驾驶辅助的信息必须标记风险等级。
- 地图数据变更必须记录数据版本和生效区域。
- 客户口头需求必须转化为书面记录后才能排期。
- 上线前必须完成 UAT 记录和回滚方案确认。

## 示例

输入：

```text
某车型希望在车机地图中增加新能源充电站筛选和路线偏好。
```

期望输出摘要：

```text
业务背景：新能源车主需要在导航过程中快速找到可用充电站。
功能范围：充电站筛选、路线偏好、充电站详情、距离与可用状态展示。
验收标准：用户可以筛选快充/慢充；路线规划可以优先经过充电站；地图数据版本必须可追踪。
风险：充电站状态数据可能延迟；地图数据覆盖不完整会影响体验。
```

## 相关链接

- docs/prd/003-vehicle-map-requirement-intake.md
- docs/uat/003-vehicle-map-requirement-intake-uat.md
- api/openapi.yaml
