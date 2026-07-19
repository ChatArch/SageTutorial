# 源码和输出

## 可运行脚本

| 文件 | 说明 |
| --- | --- |
| `examples/lie_quantum_smoke.py` | 主 smoke test，验证 Lie theory / crystals / q-number / quantum group 边界。 |
| `examples/b_type_root_weight_lattice.py` | `B_n` 根格、权格、fundamental weights 示例。 |
| `examples/module_scan.py` | 模块 import / namespace 初扫脚本。 |

## 输出文件

| 文件 | 说明 |
| --- | --- |
| `examples/outputs/lie-quantum-smoke-final.txt` | 最终 smoke test 输出。 |
| `examples/outputs/b-type-root-weight-lattice.txt` | `B_3` 根格/权格示例输出。 |
| `examples/outputs/module-scan.txt` | 第一轮模块扫描输出。 |
| `examples/outputs/api-introspection.txt` | WeylCharacterRing / LieAlgebra API 修正记录。 |
| `examples/outputs/quantum-group-introspection.txt` | `QuantumGroup` 依赖检查输出。 |

## 公开边界

此仓库只保留可公开复现的脚本、数学说明和输出片段。输出中若出现本地 Sage 源码路径，一律用 `<SAGE_ROOT>` 形式表示。
