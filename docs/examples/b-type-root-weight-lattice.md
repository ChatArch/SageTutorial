# B 型根格与权格

本页记录 `B_n = so(2n+1)` 的根系、根格、权格，以及一个可复现的 SageMath 示例。这里使用标准欧氏空间 `E = R^n` 和标准正交基 `e_1, ..., e_n`。

## 约定和来源

本文采用 Lie theory 中 `B_n` 根系的标准实现：

```text
B_n = so(2n+1),    E = R^n,    basis = e_1, ..., e_n
```

SageMath 里的 `CartanType(["B", n])` 和 `RootSystem(["B", n]).ambient_space()` 也使用这个标准坐标模型。本文代码里的输出 `(1, -1, 0)` 就表示 `e_1 - e_2`，输出 `(1/2, 1/2, 1/2)` 就表示 `1/2(e_1 + e_2 + e_3)`。

相关 SageMath 对象：

| 数学对象 | SageMath 对象 | 含义 |
| --- | --- | --- |
| Cartan type `B_n` | `CartanType(["B", n])` | Dynkin 类型和 Cartan matrix。 |
| 根系 | `RootSystem(cartan)` | 与 Cartan type 关联的 root system。 |
| ambient space | `RootSystem(cartan).ambient_space()` | 把根和权写成 `e_i` 坐标的空间。 |
| simple roots | `ambient.simple_roots()` | 返回 `alpha_i`。 |
| fundamental weights | `ambient.fundamental_weights()` | 返回 `omega_i`。 |

SageMath 文档参考：

- Root systems: <https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/root_system/root_system.html>
- Cartan types: <https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/root_system/cartan_type.html>

## 自然语言解释

可以先把 `B_n` 想成一个在 `n` 维空间里排布的“方向系统”。每个 `e_i` 是一个基本方向。根系告诉我们：这个李代数允许哪些基本对称方向；根格和权格则是在这些方向上允许的“整数步长”和“半整数步长”。

`B_n` 的根有两类：

- 第一类是 `e_i +/- e_j` 这样的组合方向，它们连接两个坐标方向；
- 第二类是单独的 `e_i`，它们只沿着一个坐标方向走一步。

因为 `B_n` 包含单独的短根 `e_i`，所以 simple roots 生成出来的根格最后正好覆盖整个整数格 `Z^n`。直观地说：根格允许你沿每个坐标轴走任意整数步。

权格比根格稍微大一点。除了整数点以外，它还允许整体平移半步：

```text
1/2(e_1 + ... + e_n)
```

所以 `B_n` 的权格由两层组成：

1. 所有整数坐标点；
2. 所有坐标同时变成半整数的点。

这就是为什么可以写成：

```text
P(B_n) = Z^n + Z * 1/2(e_1 + ... + e_n)
```

其中 `omega_n = 1/2(e_1 + ... + e_n)` 代表第二层，也就是 spin representation 对应的那一类半整数最高权。

一句话总结：

```text
根格 Q(B_n)：只能走整数格点。
权格 P(B_n)：可以走整数格点，也可以整体平移到半整数格点。
二者只差一个 Z/2Z 的选择：整数层或半整数层。
```

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

这里最后一个 simple root `alpha_n = e_n` 是短根。这一点是 `B_n` 区别于 `D_n` 的关键之一：`D_n` 只有 `+/- e_i +/- e_j` 型根，而 `B_n` 还包含短根 `+/- e_i`。

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

所以每个标准基向量 `e_i` 都在根格里。反过来，每个 simple root 又都是整数系数的 `e_i` 组合。因此：

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

权格由 fundamental weights 生成：

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

非平凡陪集可以由 spin weight `omega_n` 表示。这也是 `B_n` 的 spin representation 出现半整数最高权的格论来源。

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

## 代码逐段解释

### 1. 选择 Cartan type

```python
n = 3
cartan = CartanType(["B", n])
```

这一步告诉 SageMath：我们要处理的是 `B_3`。数学上对应 `so(7)` 的根系。换成 `n = 4` 就是 `B_4 = so(9)`。

### 2. 切到 ambient space

```python
ambient = RootSystem(cartan).ambient_space()
```

`ambient_space()` 的作用是把根和权写到标准正交基 `e_i` 的坐标里。这样输出比较接近数学书上的写法，例如：

```text
alpha_1 = (1, -1, 0) = e_1 - e_2
omega_3 = (1/2, 1/2, 1/2) = 1/2(e_1 + e_2 + e_3)
```

如果只用 abstract root lattice，SageMath 可能会输出 `alpha[1]`、`Lambda[1]` 这样的符号基。这里选择 ambient space，是为了直接看根格和权格在 `e_i` 坐标里的形状。

### 3. 取 simple roots 和 fundamental weights

```python
alpha = ambient.simple_roots()
omega = ambient.fundamental_weights()
```

- `alpha[i]` 是 simple root `alpha_i`；
- `omega[i]` 是 fundamental weight `omega_i`。

对 `B_3`，SageMath 输出：

```text
alpha_1 = (1, -1, 0)
alpha_2 = (0, 1, -1)
alpha_3 = (0, 0, 1)
```

这正是：

```text
alpha_1 = e_1 - e_2
alpha_2 = e_2 - e_3
alpha_3 = e_3
```

### 4. 验证根格等于整数格

```python
for i in range(1, n + 1):
    rhs = sum(alpha[j] for j in range(i, n + 1))
    print(f"e_{i} = {rhs}")
```

这段代码验证：

```text
e_i = alpha_i + alpha_{i+1} + ... + alpha_n
```

对 `B_3`，输出：

```text
e_1 = alpha_1 + alpha_2 + alpha_3 = (1, 0, 0)
e_2 = alpha_2 + alpha_3 = (0, 1, 0)
e_3 = alpha_3 = (0, 0, 1)
```

因此每个 `e_i` 都在 `Q(B_n)` 中，所以 `Z^n` 包含在根格中。另一方面，所有 `alpha_i` 本来就是整数坐标向量，所以根格也包含在 `Z^n` 中。两边合起来得到：

```text
Q(B_n) = Z^n
```

## 输出怎么读

输出文件见 `examples/outputs/b-type-root-weight-lattice.txt`。

```text
Cartan type: ['B', 3]
Rank: 3
Cartan matrix:
[ 2 -1  0]
[-1  2 -1]
[ 0 -2  2]
```

这说明当前 Cartan type 是 `B_3`。Cartan matrix 的最后两项不对称：`a_23 = -1`，`a_32 = -2`，对应 `B_3` Dynkin 图末端的长短根关系。

```text
Simple roots in the standard orthonormal basis e_i:
alpha_1 = (1, -1, 0)
alpha_2 = (0, 1, -1)
alpha_3 = (0, 0, 1)
```

这三行就是 simple roots 的 `e_i` 坐标。

```text
Fundamental weights in the standard orthonormal basis e_i:
omega_1 = (1, 0, 0)
omega_2 = (1, 1, 0)
omega_3 = (1/2, 1/2, 1/2)
```

前两个 fundamental weights 是整数坐标，最后一个 `omega_3` 是半整数坐标。这就是 `B_n` 权格比根格大的地方。

```text
P(B_n) / Q(B_n) ~= Z/2Z
```

这说明权格相对根格只有两个陪集：整数格本身，以及由 spin weight `omega_n` 代表的半整数陪集。

## SageMath 完整输出

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

实际读代码时，可以把 SageMath 当成两件事来用：

1. **表达对象**：用 `CartanType`、`RootSystem`、`ambient_space` 把根系和权系写出来。
2. **验证推导**：用 `simple_roots()` 和 `fundamental_weights()` 检查手写公式是否和计算模型一致。
