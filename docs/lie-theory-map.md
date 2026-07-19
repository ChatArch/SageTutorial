# Lie Theory / Quantum Groups 基础概念与 SageMath 映射

## 1. 总体路线

本任务分两层：

1. **知识层**：理解 Lie theory / quantum groups 的基础对象和典型性质。
2. **计算层**：看这些对象在 SageMath 中如何表达、计算和做计算式验证。

当前 HITK 上 SageMath 版本为 `10.5.beta2`。对 Lie theory、Weyl groups、root systems、representations、crystals 支持较成熟；对 Drinfeld-Jimbo quantum group 的直接构造模块存在，但依赖 GAP 可选包 `QuaGroup`，当前环境未安装。

## 2. 基础概念图谱

| 概念 | 数学含义 | SageMath 对应 |
|---|---|---|
| Cartan type | Dynkin 图/类型，如 `A2`, `B2`, `G2` | `CartanType(['A',2])` |
| Cartan matrix | 编码 simple roots 夹角与长度的矩阵 | `CartanType(['A',2]).cartan_matrix()` |
| Root system | 根系，包含 simple roots、positive roots 等 | `RootSystem(['A',2])` |
| Root lattice | 由 simple roots 张成的格 | `RootSystem(['A',2]).root_lattice()` |
| Weight lattice | 权格，包含 fundamental weights | `RootSystem(['A',2]).weight_lattice()` |
| Weyl group | 由 simple reflections 生成的 Coxeter 群 | `WeylGroup(['A',2], prefix='s')` |
| Lie algebra | 与根系相关的半单 Lie algebra | `LieAlgebra(QQ, cartan_type=['A',2])` |
| Chevalley basis | `e_i, f_i, h_i` 生成元和根向量 | `L.gens()`, `L.e(i)`, `L.f(i)` |
| Highest weight representation | 由 dominant highest weight 标记的不可约表示 | `WeylCharacterRing('A2')` |
| Character decomposition | tensor product 的不可约分解 | `A2(1,0,0) * A2(1,1,0)` |
| Crystal | 量子群表示在 `q -> 0` 的组合骨架 | `crystals.Tableaux(['A',2], shape=[2,1])` |
| Kashiwara operators | crystal 上的 `e_i`, `f_i` 操作 | `b.e(i)`, `b.f(i)` |
| q-number | 量子群中的 `[n]_q`, q-factorial, q-binomial | `q_int`, `q_factorial`, `q_binomial` |
| Quantum group | Drinfeld-Jimbo `U_q(g)` | `algebras.QuantumGroup(['A',2])`，当前缺 `QuaGroup` |

## 3. SageMath 可以直接做什么？

### 3.1 Cartan / root / weight 数据

SageMath 可直接构造 Cartan type、Cartan matrix、root lattice、weight lattice 和 fundamental weights。

示例：

```python
ct = CartanType(['A', 2])
ct.cartan_matrix()
R = RootSystem(ct)
Q = R.root_lattice()
WL = R.weight_lattice()
```

已验证输出：

```text
cartan_matrix:
[ 2 -1]
[-1  2]
simple_roots: {1: alpha[1], 2: alpha[2]}
fundamental_weights: {1: Lambda[1], 2: Lambda[2]}
alpha1 = 2*Lambda[1] - Lambda[2]
```

### 3.2 Weyl group / Coxeter relations

可构造 Weyl group，并验证基本 Coxeter 关系。

```python
W = WeylGroup(['A', 2], prefix='s')
s = W.simple_reflections()
s[1] * s[1] == W.one()
s[1] * s[2] * s[1] == s[2] * s[1] * s[2]
```

已验证：

```text
s1^2 = 1
s2^2 = 1
s1*s2*s1 == s2*s1*s2 -> True
order = 6
long_element = s1*s2*s1
```

这相当于计算式验证 `A2` 的 Coxeter presentation。

### 3.3 表示论 / Weyl character ring

SageMath 可用 Weyl character ring 表达最高权表示和 tensor product decomposition。

```python
A2 = WeylCharacterRing('A2')
V = A2(1, 0, 0)
W = A2(1, 1, 0)
V * W
V * V
```

已验证：

```text
V*W = A2(1,1,1) + A2(2,1,0)
V^2 = A2(1,1,0) + A2(2,0,0)
V dimension = 3
```

这可以用于探索：

- fundamental representations；
- tensor product decomposition；
- character-level representation computations；
- 小型 branching / decomposition 问题。

### 3.4 Lie algebra bracket / Jacobi identity

SageMath 可构造 Chevalley basis 下的 Lie algebra，并计算 bracket。

```python
L = LieAlgebra(QQ, cartan_type=['A', 2])
e1, e2, f1, f2, h1, h2 = L.gens()
e1.bracket(f1)
h1.bracket(e1)
h1.bracket(e2)
```

已验证：

```text
[e1,f1] = h1
[h1,e1] = 2*E[alpha[1]]
[h1,e2] = -E[alpha[2]]
Jacobi(e1,e2,f1) = 0
Jacobi is zero = True
```

这可以用来验证最基础的 Chevalley relations 和 Jacobi identity。

### 3.5 Crystals / Kashiwara operators

SageMath 对 crystals 有较成熟的组合模型支持，尤其是 type A tableaux crystals。

```python
C = crystals.Tableaux(['A', 2], shape=[2, 1])
b = C.module_generators[0]
b.f(1)
b.f(2)
b.f(1).e(1) == b
```

已验证：

```text
highest weight element = [[1, 1], [2]]
f_1(b) = [[1, 2], [2]]
f_2(b) = [[1, 1], [3]]
e_1(f_1(b)) == b -> True
cardinality = 8
```

这对量子群表示很重要，因为 crystals 是 `U_q(g)` 表示在 `q -> 0` 极限下的组合模型。

### 3.6 q-numbers / q-binomial

SageMath 内置量子群相关的 q-number 工具。

```python
from sage.algebras.quantum_groups.q_numbers import q_int, q_factorial, q_binomial
q = polygen(ZZ, 'q')
q_int(3, q)
q_factorial(4, q)
q_binomial(5, 2, q)
```

已验证：

```text
q_int(3) = (q^4 + q^2 + 1)/q^2
q_factorial(4) = (q^12 + 3*q^10 + 5*q^8 + 6*q^6 + 5*q^4 + 3*q^2 + 1)/q^6
q_binomial(5,2) = (q^12 + q^10 + 2*q^8 + 2*q^6 + 2*q^4 + q^2 + 1)/q^6
```

## 4. 当前不能直接做什么？

### 4.1 直接构造 Drinfeld-Jimbo quantum group

SageMath 有 `sage.algebras.quantum_groups.quantum_group_gap` 模块，里面有：

- `QuantumGroup`
- `LowerHalfQuantumGroup`
- `QuantumGroupModule`
- `QuantumGroupMorphism`

但当前 HITK 环境中直接构造失败：

```python
from sage.all import algebras
Q = algebras.QuantumGroup(['A', 2])
```

失败原因：

```text
gap_package_QuaGroup is not available.
LoadPackage("QuaGroup") evaluated to fail in GAP.
To install gap_package_QuaGroup using the Sage package manager, try:
  sage -i gap_package_quagroup
```

所以当前可做：

- root system / Weyl group / Lie algebra / representation / crystal / q-number；
- 间接探索量子群表示的组合模型；
- q-Serre 公式层面的准备。

当前不能直接做：

- 构造完整 `U_q(g)` 元素；
- 在 Sage 内直接乘量子群生成元并验证 quantum Serre relations；
- 使用 `QuantumGroupModule` 等 QuaGroup-backed 功能。

如果后续需要，可以单独评估是否安装 `gap_package_quagroup`。

## 5. 下一步数学任务设计建议

可以围绕以下小任务继续：

1. **A2 root system 小任务**：输出 Cartan matrix、simple roots、fundamental weights，并验证 simple roots 与 fundamental weights 的 Cartan pairing。
2. **Weyl group 小任务**：验证 `A2` 的 Coxeter relations 和 braid relation。
3. **Lie algebra 小任务**：验证 Chevalley relations 与 Jacobi identity。
4. **Representation 小任务**：计算 `sl_3` 基本表示 tensor product 分解。
5. **Crystal 小任务**：画/枚举 tableaux crystal，验证 `e_i` / `f_i` 局部逆关系。
6. **q-number 小任务**：计算 q-binomial，并准备 quantum Serre relation 公式。
7. **Quantum group 环境任务**：如需完整 `U_q(g)`，安装/验证 GAP `QuaGroup`。
