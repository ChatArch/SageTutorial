# HITK 环境

HITK 上的 SageMath 环境已经检查通过。

| 项目 | 值 |
| --- | --- |
| host | `hitk.cube` |
| user | `zhihong` |
| `sage` | `/home/zhihong/.local/bin/sage` |
| resolved target | `/home/zhihong/sage/sage` |
| SageMath version | `10.5.beta2` |
| `SAGE_ROOT` | `/home/zhihong/sage` |
| `SAGE_VENV` | `/home/zhihong/sage/local/var/lib/sage/venv-python3.12.4` |
| Sage Python | Python 3.12.4 |

## 已验证能力

```text
factor(123456)= 2^6 * 3 * 643
integral= -1/12*pi - 1/3*sqrt(3) + 1
cycle graph order/size= 5 5
cycle graph diameter= 2
```

## Jupyter kernel

可用 kernel：

- `sagemath-dev`，指向 SageMath 10.5.beta2。

不建议使用：

- 系统 `sagemath` kernel，它指向缺失的 `/usr/bin/sage`。

## 来源任务

HITK 环境检查原始任务：

`/home/zhihong/Playground/projects/07-16-hitk-sagemath-exploration/`
