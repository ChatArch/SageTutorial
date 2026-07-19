# B 型根格与权格

本页记录 `B_n = so(2n+1)` 的根系、根格、权格，以及一个可复现的 SageMath 示例。这里使用标准欧氏空间 `E = R^n` 和标准正交基 `e_1, ..., e_n`。

## 根系

`B_n` 的根系为：

```text
Phi(B_n) = { +/- e_i +/- e_j | 1 <= i < j <= n } union { +/- e_i | 1 <= i <= n }
```

其中：

- `+/- e_i +/- e_j` 是长根；
- `+/- e_i` 是短根。

一组标准 simple roots 是：

```text
alpha_1     = e_1 - e_2
alpha_2     = e_2 - e_3
...
alpha_{n-1} = e_{n-1} - e_n
alpha_n     = e_n
```

## 根格 root lattice

根格由 simple roots 生成：

```text
Q(B_n) = Z alpha_1 + ... + Z alpha_n
```

因为：

```text
e_n     = alpha_n
e_{n-1} = alpha_{n-1} + alpha_n
...
e_i     = alpha_i + alpha_{i+1} + ... + alpha_n
```

所以：

```text
Q(B_n) = Z e_1 + ... + Z e_n = Z^n
```

也就是说，`B_n` 的根格就是标准整数格。

## 权格 weight lattice

`B_n` 的 fundamental weights 是：

```text
omega_k = e_1 + e_2 + ... + e_k,        1 <= k <= n-1
omega_n = 1/2 * (e_1 + e_2 + ... + e_n)
```

权格为：

```text
P(B_n) = Z omega_1 + ... + Z omega_n
```

等价地：

```text
P(B_n) = Z^n + Z * 1/2(e_1 + ... + e_n)
```

也可以写成坐标条件：

```text
P(B_n) = { (x_1, ..., x_n) in (1/2)Z^n | x_i - x_j in Z for all i,j }
```

也就是说，权格里的向量坐标要么全是整数，要么全是半整数。

根格与权格的商为：

```text
P(B_n) / Q(B_n) ~= Z/2Z
```

非平凡陪集可以由 spin weight `omega_n` 表示。

## B3 例子

对 `B_3 = so(7)`，simple roots 是：

```text
alpha_1 = e_1 - e_2
alpha_2 = e_2 - e_3
alpha_3 = e_3
```

fundamental weights 是：

```text
omega_1 = e_1
omega_2 = e_1 + e_2
omega_3 = 1/2(e_1 + e_2 + e_3)
```

因此：

```text
Q(B_3) = Z e_1 + Z e_2 + Z e_3
P(B_3) = Z^3 + Z * 1/2(e_1 + e_2 + e_3)
```

## SageMath 代码

完整脚本见 `examples/b_type_root_weight_lattice.py`。

```python
from sage.all import CartanType, RootSystem

n = 3
cartan = CartanType(["B", n])
ambient = RootSystem(cartan).ambient_space()
alpha = ambient.simple_roots()
omega = ambient.fundamental_weights()

print(cartan.cartan_matrix())

for i in range(1, n + 1):
    print(f"alpha_{i} = {alpha[i]}")

for i in range(1, n + 1):
    print(f"omega_{i} = {omega[i]}")

for i in range(1, n + 1):
    rhs = sum(alpha[j] for j in range(i, n + 1))
    print(f"e_{i} = {rhs}")
```

运行：

```bash
sage -python examples/b_type_root_weight_lattice.py
```

## SageMath 输出

输出文件见 `examples/outputs/b-type-root-weight-lattice.txt`。

```text
Cartan type: ['B', 3]
Rank: 3
Cartan matrix:
[ 2 -1  0]
[-1  2 -1]
[ 0 -2  2]

Simple roots in the standard orthonormal basis e_i:
alpha_1 = (1, -1, 0)
alpha_2 = (0, 1, -1)
alpha_3 = (0, 0, 1)

Fundamental weights in the standard orthonormal basis e_i:
omega_1 = (1, 0, 0)
omega_2 = (1, 1, 0)
omega_3 = (1/2, 1/2, 1/2)

Root lattice Q(B_n):
Q(B_n) = Z e_1 + ... + Z e_n
Check e_i = alpha_i + ... + alpha_n:
e_1 = (1, 0, 0)
e_2 = (0, 1, 0)
e_3 = (0, 0, 1)

Weight lattice P(B_n):
P(B_n) = Z^n + Z * 1/2(e_1 + ... + e_n)
Equivalently, coordinates are either all integers or all half-integers.
spin weight omega_3 = (1/2, 1/2, 1/2)

Quotient:
P(B_n) / Q(B_n) ~= Z/2Z
The non-trivial coset is represented by omega_n.
```

## 小结

```text
Q(B_n) = Z^n
P(B_n) = Z^n + Z * 1/2(e_1 + ... + e_n)
P(B_n) / Q(B_n) ~= Z/2Z
```

这也是 `B_n` 中 spin representation 出现半整数最高权的格论来源。
