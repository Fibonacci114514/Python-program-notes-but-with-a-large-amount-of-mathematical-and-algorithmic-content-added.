# `IVE字符类型统计.py` · 字符类型统计

> **摘要**：遍历用户输入的字符串，分别统计大写字母、小写字母和数字字符的个数。演示了字符串遍历与字符类型判断方法。

---

#### 💻 代码

```python
str = input("请输入一句英文：")
count_upper = 0
count_lower = 0
count_digit = 0
for s in str:
    if s.isupper():
        count_upper = count_upper + 1
    if s.islower():
        count_lower = count_lower + 1
    if s.isdigit():
        count_digit = count_digit + 1
print("大写字符：", count_upper)
print("小写字符：", count_lower)
print("数字字符：", count_digit)
```

---

#### 📖 运行示例

**输入**：`Hello World 2024`

**输出**：
```
大写字符： 2
小写字符： 8
数字字符： 4
```

---

#### 🔗 关联笔记
- [[字符串#内置的字符串处理方法]]
- [[循环结构#for 语句中的迭代]]
- [[条件表达式]]

#### 🔗 返回上级
- [[IV - 字符串与随机生成实验]]
