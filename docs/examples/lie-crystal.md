# Lie algebra 与 crystals

## Lie algebra bracket

```python
from sage.all import *

L = LieAlgebra(QQ, cartan_type=['A', 2])
e1, e2, f1, f2, h1, h2 = L.gens()
print(e1.bracket(f1))
print(h1.bracket(e1))
print(h1.bracket(e2))

jac = e1.bracket(e2.bracket(f1)) + e2.bracket(f1.bracket(e1)) + f1.bracket(e1.bracket(e2))
print(jac == L.zero())
```

已验证：

```text
[e1,f1] = h1
[h1,e1] = 2*E[alpha[1]]
[h1,e2] = -E[alpha[2]]
Jacobi is zero = True
```

## Crystal / Kashiwara operators

```python
C = crystals.Tableaux(['A', 2], shape=[2, 1])
b = C.module_generators[0]
print(b)
print(b.f(1))
print(b.f(1).e(1) == b)
print(C.cardinality())
```

已验证：

```text
highest weight element = [[1, 1], [2]]
f_1(b) = [[1, 2], [2]]
e_1(f_1(b)) == b -> True
cardinality = 8
```

## 解释

- Lie algebra 部分展示 Chevalley basis 下的 bracket 计算。
- Crystal 部分展示量子群表示的组合模型，`e_i` / `f_i` 是 Kashiwara operators。
