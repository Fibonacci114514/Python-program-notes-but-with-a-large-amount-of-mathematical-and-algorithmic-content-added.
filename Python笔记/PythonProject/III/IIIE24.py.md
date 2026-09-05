# `IIIE24.py` · 异常处理演示

> **摘要**：该程序故意执行 `2 / '0'`（除数为字符串），触发类型异常，并展示了 `try-except` 异常捕获的顺序机制。

---

#### 💻 代码

```python
try:
    print(2 / '0')
except ZeroDivisionError:
    print('ZeroDivisionError')
except Exception:
    print('Exception')
```

---

#### 📖 运行结果

```
Exception
```

---

#### 📐 异常分析

- `2 / '0'` 触发的是 **`TypeError`**（类型错误：字符串不能与整数相除），而非 `ZeroDivisionError`（除数为 0）。
- 异常捕获顺序：
  1. 先匹配 `ZeroDivisionError` → 不匹配
  2. 再匹配 `Exception` → 匹配（因为 `TypeError` 是 `Exception` 的子类）

> **提示**：`Exception` 是所有异常的基类，捕获它时应放在最后，否则会“吞掉”更具体的异常。

---

#### 🔗 关联笔记
- [[异常和异常处理]]
- [[强制转换#处理无效输入]]

#### 🔗 返回上级
- [[III - 数值算法与模拟实验]]
