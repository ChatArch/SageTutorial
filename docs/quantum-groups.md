# 量子群路线

SageMath 对 quantum groups 的支持分两层：

1. **可直接使用的组合/公式层**：crystals、Kashiwara operators、q-number、q-binomial。
2. **完整量子群代数层**：`QuantumGroup` 模块存在，但依赖 GAP 可选包 `QuaGroup`。

## 当前已可用

### Crystals

```python
C = crystals.Tableaux(['A', 2], shape=[2, 1])
b = C.module_generators[0]
print(b.f(1))
print(b.f(1).e(1) == b)
```

输出：

```text
f_1(b) = [[1, 2], [2]]
e_1(f_1(b)) == b -> True
```

### q-number

```python
from sage.algebras.quantum_groups.q_numbers import q_int, q_factorial, q_binomial
q = polygen(ZZ, 'q')
print(q_int(3, q))
print(q_binomial(5, 2, q))
```

## 当前边界

```python
from sage.all import algebras
Q = algebras.QuantumGroup(['A', 2])
```

如果 SageMath 环境未安装 `QuaGroup`，会失败：

```text
gap_package_QuaGroup is not available.
LoadPackage("QuaGroup") evaluated to fail in GAP.
```

SageMath 提示可以尝试：

```bash
sage -i gap_package_quagroup
```

因此，在安装 `QuaGroup` 之前，本仓库先把 quantum groups 的探索重点放在：

- crystals 作为 `q -> 0` 的组合模型；
- q-number / q-binomial 作为 quantum Serre relation 的公式准备；
- Lie theory / representation theory 作为量子群表示的 classical shadow。
