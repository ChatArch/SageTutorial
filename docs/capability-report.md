# SageMath Lie Theory / Quantum Groups Capability Report

## Environment

- Tested SageMath version: `10.5.beta2`
- Smoke script: `examples/lie_quantum_smoke.py`
- Final output: `examples/outputs/lie-quantum-smoke-final.txt`
- Sage version: `SageMath 10.5.beta2`

## Summary

SageMath 对 Lie theory 的基础计算支持很好，包括：

- Cartan types / Cartan matrices；
- root systems / root lattices / weight lattices；
- Weyl groups and Coxeter relations；
- Lie algebras in Chevalley basis；
- Weyl character rings and representation decompositions；
- crystals and Kashiwara operators；
- q-integers / q-factorials / q-binomials。

对完整 Drinfeld-Jimbo quantum group 的直接计算支持处于“模块存在但依赖缺失”的状态：`quantum_group_gap` 存在，但当前没有安装 GAP `QuaGroup` 可选包，因此 `algebras.QuantumGroup(['A',2])` 不能直接构造。

## Capability Matrix

| Area | Status | What worked | Notes |
|---|---|---|---|
| Cartan type | OK | `CartanType(['A',2])`, Cartan matrix | 成熟可用 |
| Root system | OK | `RootSystem(['A',2]).root_lattice()` | 成熟可用 |
| Weight lattice | OK | fundamental weights, simple roots in weight basis | 成熟可用 |
| Weyl group | OK | simple reflections, braid relation, group order | 成熟可用 |
| Weyl character ring | OK | fundamental reps, tensor product decompositions | A2 uses length-3 partition notation |
| Lie algebra | OK | Chevalley basis, bracket, Jacobi identity | `h_i` from `L.gens()` / generators, not `L.h(i)` |
| Crystals | OK | tableaux crystal, Kashiwara `e_i`, `f_i` | Good for quantum group representation combinatorics |
| q-numbers | OK | `q_int`, `q_factorial`, `q_binomial` | Useful for quantum Serre formulas |
| Quantum group direct construction | Blocked | module imports, class exists | Missing GAP package `QuaGroup` |

## Verified Examples

### 1. Cartan matrix and root/weight lattices

Constructed type `A2` and got:

```text
cartan_matrix:
[ 2 -1]
[-1  2]
simple_roots: {1: alpha[1], 2: alpha[2]}
fundamental_weights: {1: Lambda[1], 2: Lambda[2]}
alpha1 in fundamental weights basis: 2*Lambda[1] - Lambda[2]
```

### 2. Weyl group Coxeter relations

Constructed `WeylGroup(['A',2])` and verified:

```text
s1^2 = 1
s2^2 = 1
s1*s2*s1 == s2*s1*s2 -> True
order = 6
long_element = s1*s2*s1
```

This is a computational check of the basic Coxeter presentation for `A2`.

### 3. Representation decompositions

Constructed `WeylCharacterRing('A2')` and computed:

```text
V = A2(1,0,0)
W = A2(1,1,0)
V*W = A2(1,1,1) + A2(2,1,0)
V^2 = A2(1,1,0) + A2(2,0,0)
V dimension = 3
```

This supports small-scale representation-theoretic exploration.

### 4. Lie algebra brackets and Jacobi identity

Constructed `LieAlgebra(QQ, cartan_type=['A',2])` and verified:

```text
gens = (E[alpha[1]], E[alpha[2]], E[-alpha[1]], E[-alpha[2]], h1, h2)
[e1,f1] = h1
[h1,e1] = 2*E[alpha[1]]
[h1,e2] = -E[alpha[2]]
Jacobi(e1,e2,f1) = 0
Jacobi is zero = True
```

This covers basic Chevalley relation checks and the Jacobi identity.

### 5. Crystals and Kashiwara operators

Constructed a tableaux crystal:

```python
C = crystals.Tableaux(['A', 2], shape=[2, 1])
b = C.module_generators[0]
```

Verified:

```text
highest weight element = [[1, 1], [2]]
f_1(b) = [[1, 2], [2]]
f_2(b) = [[1, 1], [3]]
e_1(f_1(b)) == b -> True
cardinality = 8
```

This is a concrete entry point to the quantum group representation side.

### 6. q-number calculations

Verified:

```text
q_int(3) = (q^4 + q^2 + 1)/q^2
q_factorial(4) = (q^12 + 3*q^10 + 5*q^8 + 6*q^6 + 5*q^4 + 3*q^2 + 1)/q^6
q_binomial(5,2) = (q^12 + q^10 + 2*q^8 + 2*q^6 + 2*q^4 + q^2 + 1)/q^6
```

These functions can be used to formulate q-Serre relation checks once full quantum group multiplication is available.

## Quantum Group Boundary

The module exists:

```text
sage.algebras.quantum_groups.quantum_group_gap
```

with classes like:

```text
QuantumGroup
LowerHalfQuantumGroup
QuantumGroupModule
QuantumGroupMorphism
```

But direct construction fails:

```text
FeatureNotPresentError: gap_package_QuaGroup is not available.
LoadPackage("QuaGroup") evaluated to fail in GAP.
Try: sage -i gap_package_quagroup
```

Therefore the current recommended approach is:

1. Use root systems, Weyl groups, Lie algebras, Weyl character rings, crystals, and q-number utilities now.
2. Treat full quantum group algebra multiplication as blocked until `gap_package_quagroup` is installed and verified.
3. Use crystals as the main currently available computational proxy for quantum group representations.

## Files

- `scripts/lie_quantum_smoke.py`: runnable capability test.
- `reports/lie-quantum-smoke-final.txt`: final run output.
- `reports/module-scan.txt`: initial module scan.
- `reports/api-introspection.txt`: API corrections for WeylCharacterRing and LieAlgebra.
- `reports/quantum-group-introspection.txt`: QuantumGroup dependency check.
- `reports/concepts-map.md`: concept/API mapping.
