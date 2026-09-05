---
tags:
  - lambda函数
  - 匿名函数
  - 函数式编程
  - 高阶函数
  - lambda演算
---
> **摘要**:`lambda` 函数是 Python 中定义匿名函数的方式,适用于需要简单函数对象且只使用一次的场合.它是函数式编程的基础工具,可与 `filter()`,`map()`,`sorted()` 等高阶函数配合使用.本文系统介绍 `lambda` 的语法,用法及其与计算理论中 **$λ$ 演算** 的渊源,帮助读者理解简洁表达背后的思想.

---

#### 1. `lambda` 函数的基本概念

`lambda` 函数是一种**匿名函数**——即没有显式函数名的函数.它适合逻辑简单,只需使用一次的场合.

**与计算理论的关联**:`lambda` 这一名称源自 **$λ$ 演算(Lambda Calculus)** ,由阿隆佐·邱奇(Alonzo Church)在 1930 年代提出,是形式化计算和函数式编程的理论基础.$λ$ 演算通过函数抽象和应用来表达计算,图灵完备,是计算理论的核心之一.

##### 1.1 语法格式

```python
lambda 参数1, 参数2, ... : 表达式
```

- **参数**:可以是 0 个或多个,逗号分隔.
- **表达式**:只能是单个表达式,不能包含语句(如赋值,循环).
- **返回值**:表达式的计算结果自动作为返回值.

```python
# 求乘积
f = lambda x, y: x * y
print(f(4, 6))   # 24

# 求平方(单参数)
square = lambda x: x ** 2
print(square(5)) # 25
```

##### 1.2 `lambda` 作为“普通函数”使用

`lambda` 表达式本质上是一个函数对象,可以被赋值给变量,像普通函数一样调用.

```python
add = lambda a, b: a + b
print(add(3, 5))   # 8
```

但与 `def` 定义的函数相比,`lambda` 更适合作为**临时使用的函数对象**.

---

#### 2. `lambda` 与高阶函数配合使用

高阶函数是指接收函数作为参数或返回函数作为结果的函数.

##### 2.1 `filter()`:过滤序列

`filter(function, iterable)` 对序列中的每个元素调用 `function`,保留返回 `True` 的元素.

**示例:筛选负数**

```python
nums = [3, 5, -7, 4, -1, 0, -9]

# 传统方式
f = lambda x: x < 0
for i in filter(f, nums):
    print(i)          # -7, -1, -9

# 直接使用 lambda(真正的“匿名”)
for i in filter(lambda x: x < 0, nums):
    print(i)          # -7, -1, -9
```

##### 2.2 `map()`:映射转换

```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)   # [1, 4, 9, 16, 25]
```

##### 2.3 `sorted()` 的 `key` 参数

```python
students = [("张三", 85), ("李四", 92), ("王五", 78)]

# 按分数升序排序
sorted_by_score = sorted(students, key=lambda x: x[1])
print(sorted_by_score)   # [('王五', 78), ('张三', 85), ('李四', 92)]
```

##### 2.4 `reduce()`:累积计算(需导入 `functools`)

```python
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)   # 120
```

---

#### 3. 与计算理论的关联:$λ$ 演算

| 概念 | 数学/计算理论 | Python 对应 |
|------|---------------|-------------|
| 函数抽象 | $λx. 表达式$ | `lambda x: 表达式` |
| 函数应用 | $(λx. x²)(3) = 9$ | `(lambda x: x**2)(3)` → 9 |
| 匿名函数 | 无需命名即可使用 | `lambda` 可直接传入高阶函数 |
| 高阶函数 | 函数可以接受函数作为参数 | `filter(lambda x: x<0, nums)` |

> **$λ$ 演算的图灵完备性**:$λ$ 演算被证明与图灵机等价,任何可计算函数都可以用 $λ$ 演算表达.Python 的 `lambda` 虽然功能有限(仅支持表达式),但结合 `def` 定义的函数,Python 支持完整的函数式编程范式,理论上可以表达任何可计算问题.

---

#### 4. `lambda` 与 `def` 的对比

| 特性 | `def` 定义 | `lambda` 定义 |
|------|-----------|---------------|
| 函数名 | 必须命名 | 匿名(可赋值给变量) |
| 语句支持 | 支持多语句 | 仅支持单表达式 |
| 可读性 | 适合复杂逻辑 | 适合简单逻辑 |
| 返回值 | `return` 显式返回 | 表达式值自动返回 |
| 类型 | `<class 'function'>` | `<class 'function'>` |
| 使用场景 | 通用定义 | 临时,一次性,回调 |

**选择建议**:
- 逻辑复杂 → 用 `def` 定义,保持可读性.
- 逻辑简单且只使用一次 → 用 `lambda`,避免命名冗余.

---

#### 5. 注意事项

- `lambda` 内部不能使用 `print()` 等语句(只有表达式).
- 不能包含赋值操作(如 `x = 10`),但可包含 `:=` 海象运算符(Python 3.8+).
- 过度使用 `lambda` 会影响代码可读性,应适度使用.
- 在需要多行逻辑时,仍应使用 `def` 定义具名函数.

---

#### 6. 综合示例:快速筛选与排序

```python
# 从列表中筛选偶数并排序
nums = [12, 5, 8, 3, 20, 7, 14]
result = sorted(filter(lambda x: x % 2 == 0, nums))
print(result)   # [8, 12, 14, 20]

# 从字典按值排序
data = {"a": 3, "b": 1, "c": 2}
sorted_items = sorted(data.items(), key=lambda x: x[1])
print(sorted_items)   # [('b', 1), ('c', 2), ('a', 3)]
```

---

#### 7. 快速参考

```python
# 基本语法
lambda x: x * 2
lambda x, y: x + y
lambda: "Hello"

# 与高阶函数
filter(lambda x: x > 0, nums)
map(lambda x: x**2, nums)
sorted(data, key=lambda x: x[1])
reduce(lambda x, y: x + y, nums)

# 立即调用
(lambda x: x**2)(5)   # 25
```

---

> **总结**:`lambda` 是 Python 从函数式编程中引入的简洁工具,其根源可追溯至 $λ$ 演算——计算理论的核心模型之一.掌握 `lambda` 的用法,不仅能写出更简洁的代码,也为理解函数式编程,高阶函数和更深入的计算理论奠定基础.当你在 `filter`,`map`,`sorted` 中看到 `lambda` 时,你看到的不仅是语法糖,更是计算理论在编程语言中的具体实践.

---

**相关笔记**:
- [[函数的基本概念]] — 函数的定义与结构
- [[函数的使用]] — 函数参数与调用的完整说明
- [[递归函数]] — 递归与 $λ$ 演算中的不动点
