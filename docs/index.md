# SageTutorial 文档

SageTutorial 是 ChatArch 的 SageMath 教程与探索文档。它把 SageMath 在 Lie theory / quantum groups 周边的可计算能力整理成可复用的 Markdown / MkDocs 站点。

站点入口：<https://arch.gh.wzhecnu.cn/SageTutorial/>

## 按场景选择文档

| 场景 | 文档 |
| --- | --- |
| 快速运行 SageMath 示例 | [快速开始](getting-started.md) |
| 理解 Lie theory 概念和 SageMath API 映射 | [概念与 SageMath 映射](lie-theory-map.md) |
| 查看当前能力边界和验证结果 | [能力边界](capability-report.md) |
| 跑 `A2` 根系、权格、Weyl 群关系 | [A2 根系与 Weyl 群](examples/a2-root-weyl.md) |
| 写出并验证 `B_n` 的根格、权格表达式 | [B 型根格与权格](examples/b-type-root-weight-lattice.md) |
| 跑 Lie algebra bracket、Jacobi identity、crystals | [Lie algebra 与 crystals](examples/lie-crystal.md) |
| 探索 q-number 和量子群依赖边界 | [q-number 与量子群边界](examples/q-numbers.md) |
| 查看源码和输出文件 | [源码和输出](reference.md) |

## 当前主题

第一版主题是：**以 Lie theory / quantum groups 为目标，探索 SageMath 能做哪些计算**。

目前已验证 SageMath 可以直接支持：

- Cartan type / Cartan matrix；
- root system / root lattice / weight lattice；
- fundamental weights；
- Weyl group / Coxeter relations / braid relations；
- Lie algebra Chevalley basis、bracket、Jacobi identity；
- Weyl character ring 和 tensor product decomposition；
- crystals / tableaux crystals / Kashiwara operators；
- q-integers / q-factorials / q-binomials。

当前边界：

- SageMath 存在 `quantum_group_gap` 模块；
- 但完整 `algebras.QuantumGroup(['A', 2])` 需要 GAP 可选包 `QuaGroup`；
- 如果 SageMath 环境未安装 `gap_package_QuaGroup`，完整 Drinfeld-Jimbo quantum group 乘法不可直接运行。

## 公开文档边界

本文档只放可公开的数学和技术内容，不记录账号、绝对路径、内部基础设施、任务目录或凭据。
