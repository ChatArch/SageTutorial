# q-number 与量子群边界

## q-number

```python
from sage.all import *
from sage.algebras.quantum_groups.q_numbers import q_int, q_factorial, q_binomial

q = polygen(ZZ, 'q')
print(q_int(3, q))
print(q_factorial(4, q))
print(q_binomial(5, 2, q))
```

已验证：

```text
q_int(3): (q^4 + q^2 + 1)/q^2
q_factorial(4): (q^12 + 3*q^10 + 5*q^8 + 6*q^6 + 5*q^4 + 3*q^2 + 1)/q^6
q_binomial(5,2): (q^12 + q^10 + 2*q^8 + 2*q^6 + 2*q^4 + q^2 + 1)/q^6
```

## 直接构造 QuantumGroup

SageMath 包含 `sage.algebras.quantum_groups.quantum_group_gap`，但完整构造依赖 GAP 可选包 `QuaGroup`。

```python
from sage.all import algebras
Q = algebras.QuantumGroup(['A', 2])
```

当前输出：

```text
FeatureNotPresentError: gap_package_QuaGroup is not available.
LoadPackage("QuaGroup") evaluated to fail in GAP.
```

后续如需完整量子群乘法和 quantum Serre relation，可以单独评估：

```bash
sage -i gap_package_quagroup
```
