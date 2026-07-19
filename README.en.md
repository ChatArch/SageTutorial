# SageTutorial

SageTutorial is a ChatArch documentation/demo repository for SageMath tutorials and exploratory notes.

The first version focuses on:

- SageMath 10.5.beta2 on HITK;
- Lie theory basics: Cartan types, root systems, weight lattices, Weyl groups;
- Lie algebra computations: Chevalley basis, brackets, Jacobi identity;
- Representation theory: Weyl character rings and tensor product decompositions;
- Quantum-group adjacent tools: crystals, Kashiwara operators, q-numbers, and the current `QuaGroup` dependency boundary.

Documentation: <https://arch.gh.wzhecnu.cn/SageTutorial/>

## Quick Start

```bash
sage -python examples/lie_quantum_smoke.py
```

Build docs locally:

```bash
python -m pip install -e ".[docs]"
mkdocs build --strict
mkdocs serve
```
