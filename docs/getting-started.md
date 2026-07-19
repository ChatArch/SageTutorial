# 快速开始

## 运行 smoke test

```bash
git clone https://github.com/ChatArch/SageTutorial.git
cd SageTutorial
sage -python examples/lie_quantum_smoke.py
```

如果只想看输出，可以查看：

```bash
less examples/outputs/lie-quantum-smoke-final.txt
```

## 构建文档

```bash
python -m pip install -e ".[docs]"
mkdocs build --strict
```

本地预览：

```bash
mkdocs serve
```

## 最小 SageMath 示例

```python
from sage.all import *

ct = CartanType(['A', 2])
print(ct.cartan_matrix())

W = WeylGroup(['A', 2], prefix='s')
s = W.simple_reflections()
print(s[1] * s[2] * s[1] == s[2] * s[1] * s[2])

L = LieAlgebra(QQ, cartan_type=['A', 2])
e1, e2, f1, f2, h1, h2 = L.gens()
print(e1.bracket(f1))
```
