<div align="center">
  <a href="https://github.com/ChatArch/SageTutorial/actions/workflows/ci.yml">
    <img src="https://github.com/ChatArch/SageTutorial/actions/workflows/ci.yml/badge.svg" alt="Docs CI" />
  </a>
  <a href="https://arch.gh.wzhecnu.cn/SageTutorial/">
    <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
  </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# SageTutorial

SageTutorial 是 ChatArch 的 SageMath 教程与探索仓库。当前第一版聚焦：

- Lie theory 基础对象：Cartan type、root system、weight lattice、Weyl group；
- Lie algebra 计算：Chevalley basis、bracket、Jacobi identity；
- 表示论：Weyl character ring、tensor product decomposition；
- quantum groups 相关入口：crystals、Kashiwara operators、q-numbers，以及 `QuaGroup` 可选依赖边界。

文档入口：<https://arch.gh.wzhecnu.cn/SageTutorial/>

## 快速开始

```bash
git clone https://github.com/ChatArch/SageTutorial.git
cd SageTutorial
sage -python examples/lie_quantum_smoke.py
```

本地构建文档：

```bash
python -m pip install -e ".[docs]"
mkdocs build --strict
mkdocs serve
```

## 当前内容

| 场景 | 文档 |
| --- | --- |
| 了解仓库结构 | `docs/index.md` |
| Lie theory 概念映射 | `docs/lie-theory-map.md` |
| 能力边界报告 | `docs/capability-report.md` |
| A2 根系与 Weyl 群 | `docs/examples/a2-root-weyl.md` |
| B 型根格与权格 | `docs/examples/b-type-root-weight-lattice.md` |
| Lie algebra 与 crystals | `docs/examples/lie-crystal.md` |
| q-number 与 quantum group 边界 | `docs/examples/q-numbers.md` |

## 状态

这是 demo 仓库第一版，目标是把 SageMath 的可计算数学能力整理成纯技术教程，不包含账号、绝对路径、内部基础设施或环境细节。
