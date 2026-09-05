---
tags:
  - CSV
  - 文件操作
  - 表格数据
  - 数据交换
  - 编码
---
> **摘要**:CSV(Comma-Separated Values,逗号分隔值)是一种以纯文本形式存储表格数据的文件格式,广泛应用于不同程序之间的数据交换.Python 内置的 `csv` 模块提供了便捷的读写接口.本文系统介绍 CSV 文件的特征,`csv.reader` 和 `csv.writer` 的用法,以及 `newline=''` 参数的必要性,帮助读者高效处理结构化数据.

---

#### 1. CSV 文件简介

##### 1.1 什么是 CSV

CSV(Comma-Separated Values)是一种以纯文本形式存储表格数据的文件格式.每行对应一条记录,字段之间用分隔符(通常是逗号)隔开.

```
姓名,性别,年龄
李明,男,19
杨柳,女,18
张一凡,男,18
```

##### 1.2 CSV 文件的特征

| 特征 | 说明 |
|------|------|
| **纯文本** | 使用 ASCII,UTF-8 等字符集 |
| **记录组成** | 每行一条记录,每行开头不留空格 |
| **分隔符** | 英文半角分隔符(逗号,分号,制表符) |
| **字段一致** | 每条记录有相同数量的字段 |
| **表头可选** | 若有字段名,通常写在第一行 |
| **纯字符串** | 文件中均为字符串,数值需在读取时转换 |

##### 1.3 文件指针在 CSV 操作中的角色

与普通文本文件一样,CSV 文件读写时也依赖文件指针:
- **读取时**:`csv.reader` 从文件指针当前位置开始逐行读取.通常打开时指针在文件开头.
- **写入时**:`csv.writer` 从指针当前位置开始写入.使用 `'a'` 模式时,指针在文件末尾,从而实现追加写入.

理解指针位置,有助于解释为什么追加模式下写入的内容会出现在文件末尾,以及为什么需要使用 `newline=''`(见 §4.1).

---

#### 2. CSV 文件的读取

##### 2.1 基本流程

1. 打开文件(通常用 `'r'` 模式).
2. 创建 `csv.reader` 对象.
3. 遍历 `reader` 对象,逐行获取数据.
4. 每行数据以 **列表** 形式返回,元素为字符串.

```python
import csv

with open("stu.csv", "r", encoding="utf-8") as stucsv:
    reader = csv.reader(stucsv)
    for row in reader:
        print(row)
```

**输出示例**:
```
['姓名', '性别', '年龄']
['李明', '男', '19']
['杨柳', '女', '18']
['张一凡', '男', '18']
```

##### 2.2 读取时的类型处理

CSV 读取的所有字段均为**字符串**,数值需手动转换:

```python
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)   # 跳过表头
    for row in reader:
        name = row[0]
        age = int(row[1])          # 字符串 → 整数
        score = float(row[2])      # 字符串 → 浮点数
```

---

#### 3. CSV 文件的写入

##### 3.1 基本流程

1. 打开文件(`'w'` 覆盖或 `'a'` 追加).
2. 创建 `csv.writer` 对象.
3. 使用 `writerow()` 逐行写入,或 `writerows()` 批量写入.
4. 每行数据以 **列表** 形式传入.

```python
import csv

with open("stu.csv", "a", newline='', encoding="utf-8") as stucsv:
    writer = csv.writer(stucsv)
    writer.writerow(['张芳', '女', '20'])
    writer.writerow(['王虎', '男', '18'])
```

##### 3.2 批量写入:`writerows()`

将多行数据一次性写入,提高效率.

```python
with open("stu.csv", "a", newline='', encoding="utf-8") as stucsv:
    writer = csv.writer(stucsv)
    rows = [
        ['张芳', '女', '20'],
        ['王虎', '男', '18'],
        ['赵丽', '女', '19']
    ]
    writer.writerows(rows)   # 参数为嵌套列表
```

`writerows()` 接受一个**序列**(列表或元组),其中每个元素又是一个序列,代表一行.

---

#### 4. 关键参数:`newline=''`

##### 4.1 问题背景

在 Windows 系统上,Python 的 `open()` 默认会将换行符 `\n` 转换为 `\r\n`.若写入 CSV 时使用默认设置,每行末尾会多出一个空行:

```python
# 未设置 newline 时
with open("stu.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(['张芳', '女', '20'])
    # 文件末尾会插入多余空行
```

##### 4.2 解决方案

```python
with open("stu.csv", "a", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['张芳', '女', '20'])
```

**设置 `newline=''` 的作用**:
- 禁用换行符的自动转换.
- CSV 模块自行管理换行,确保每条记录后只有一行换行,不产生多余空行.

---

#### 5. 编码处理

CSV 文件若包含中文,需指定正确的编码(通常为 `utf-8`).

```python
with open("d:\\通信录.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

> 若文件在 Excel 中直接打开出现乱码,可尝试用 `encoding='gbk'`(中文 Windows 系统常见),或将 CSV 文件另存为 UTF-8 with BOM.

---

#### 6. 综合示例:通信录查询

**需求**:由通信录字典生成 `通信录.csv` 文件,然后通过程序查询“大王”的手机号,QQ 号和微信号.

##### 6.1 生成 CSV 文件(假设已有字典数据)

```python
import csv

# 假设通信录以嵌套列表存储
contacts = [
    ['姓名', '手机号', 'QQ号', '微信号'],
    ['大王', '13914000004', '18191230002', 'jack_w'],
    ['小王', '13812345678', '12345678', 'wang_w']
]

with open("d:\\通信录.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(contacts)
```

##### 6.2 查询指定联系人

```python
import csv

with open("d:\\通信录.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "大王":
            print(f"手机号:{row[1]}")
            print(f"QQ号:{row[2]}")
            print(f"微信号:{row[3]}")
            break
```

---

#### 7. 与数学/算法的关联

| 应用场景 | CSV 操作 |
|----------|----------|
| 读取实验数据 | `csv.reader` 导入观测值 |
| 保存计算结果 | `csv.writer` 导出数值结果 |
| 数据预处理 | 读取 CSV → 清洗 → 转换为 NumPy 数组 |
| 机器学习数据集 | 从 CSV 加载特征矩阵和标签 |
| 统计分析 | 读取 CSV 后用 `pandas` 或自建统计函数分析 |

---

#### 8. CSV vs 其他文件格式

| 格式 | 优点 | 缺点 |
|------|------|------|
| CSV | 简单,通用,可读性强 | 无数据类型信息,嵌套结构弱 |
| JSON | 支持嵌套结构,可读性好 | 体积较大 |
| Excel (.xlsx) | 支持样式,公式,多工作表 | 需要第三方库,非纯文本 |
| Pickle | Python 原生,支持任意对象 | 仅 Python 可用,不安全 |

---

#### 9. 快速参考

```python
# 读取 CSV
import csv
with open("file.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)      # row 是列表

# 写入 CSV(单行)
with open("file.csv", "a", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['张三', 20, 85.5])

# 写入 CSV(多行)
with open("file.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows([
        ['姓名', '年龄', '成绩'],
        ['张三', 20, 85.5],
        ['李四', 21, 92.0]
    ])

# 读取并处理数据
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)          # 跳过表头
    for name, age, score in reader:
        score = float(score)       # 类型转换
```

---

> **总结**:CSV 是数据交换的通用格式,Python 内置 `csv` 模块提供了简洁高效的读写接口.使用时注意编码设置(`utf-8`)和空行问题(`newline=''`),读取后根据需要进行类型转换.掌握 CSV 操作,你就能轻松处理各类表格数据,为数据分析与算法应用做好准备.

---

**相关笔记**:
- [[文件及文件基本操作]] — 文件 I/O 基础
- [[字符串]] — `split()` 手动解析 CSV(但推荐使用 `csv` 模块)
- [[列表与列表操作]] — CSV 每行读取为列表
- [[字典与集合]] — 可将 CSV 数据转换为字典列表