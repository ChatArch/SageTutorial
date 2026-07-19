# A2 根系与 Weyl 群

这个例子展示 SageMath 如何表达 `A2` 的 Cartan matrix、root lattice、weight lattice 和 Weyl group。

## 代码

```python
from sage.all import *

ct = CartanType(['A', 2])
print(ct.cartan_matrix())

R = RootSystem(ct)
Q = R.root_lattice()
alpha = Q.simple_roots()
print(alpha[1] + alpha[2])

WL = R.weight_lattice()
print(WL.fundamental_weights())

W = WeylGroup(['A', 2], prefix='s')
s = W.simple_reflections()
print(s[1] * s[1])
print(s[1] * s[2] * s[1] == s[2] * s[1] * s[2])
print(W.order())
```

## 已验证输出

```text
cartan_matrix:
[ 2 -1]
[-1  2]
s1^2: 1
s2^2: 1
braid equality: True
order: 6
long_element: s1*s2*s1
```

## 数学含义

这相当于用 SageMath 计算式验证 `A2` Weyl group 的基本 Coxeter 关系：

- `s_1^2 = s_2^2 = 1`；
- `s_1 s_2 s_1 = s_2 s_1 s_2`；
- Weyl group 阶数为 6。
