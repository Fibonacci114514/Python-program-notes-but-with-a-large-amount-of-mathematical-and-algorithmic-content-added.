---
tags:
  - time库
  - datetime库
  - 时间操作
  - 计时
  - 格式化
---
> **摘要**:Python 的 `time` 和 `datetime` 库提供了时间获取,格式化,延时,计时等核心功能.本文系统梳理两个库的常用函数,并说明它们在算法计时,日志记录,时间计算等场景中的应用.

---
#### 1. `time` 库 —— 底层时间操作

##### 1.1 导入方式

```python
from time import *      # 或 import time
```

##### 1.2 核心函数

| 函数 | 返回值 | 说明 |
|------|--------|------|
| `time()` | 浮点数(秒) | 从 1970-01-01 00:00:00 UTC 到现在的秒数(时间戳) |
| `localtime([secs])` | `struct_time` 对象 | 将时间戳转换为本地时间的结构化数据 |
| `gmtime([secs])` | `struct_time` 对象 | 将时间戳转换为 UTC 时间的结构化数据 |
| `strftime(format[, t])` | 字符串 | 将结构化时间格式化为指定字符串 |
| `sleep(secs)` | 无 | 让程序暂停 secs 秒 |
| `perf_counter()` | 浮点数(秒) | 高精度计时器,适合测量短时间间隔 |

##### 1.3 结构化时间 `struct_time`

包含以下属性(可通过索引或属性名访问):

| 索引 | 属性名 | 含义 | 取值 |
|------|--------|------|------|
| 0 | `tm_year` | 年份 | 四位数 |
| 1 | `tm_mon` | 月份 | 1–12 |
| 2 | `tm_mday` | 日 | 1–31 |
| 3 | `tm_hour` | 小时 | 0–23 |
| 4 | `tm_min` | 分钟 | 0–59 |
| 5 | `tm_sec` | 秒 | 0–61(考虑闰秒) |
| 6 | `tm_wday` | 星期几 | 0(周一)–6(周日) |
| 7 | `tm_yday` | 一年中的第几天 | 1–366 |
| 8 | `tm_isdst` | 夏令时标志 | 0/1/-1 |

##### 1.4 常用示例

```python
from time import *

# 时间戳
ts = time()
print(ts)                      # 1730191844.214...

# 本地时间结构化
local = localtime()
print(local)                   # struct_time(...)
print(local.tm_year, local.tm_mon)

# 格式化时间
formatted = strftime("%Y-%m-%d %H:%M:%S")
print(formatted)               # 2024-10-29 16:48:38

# 程序延时
for i in range(5):
    print(i)
    sleep(1)                   # 暂停1秒
```

---

#### 2. `datetime` 库 —— 高级日期时间处理

##### 2.1 导入方式

```python
from datetime import *
# 或
import datetime
```

##### 2.2 核心类

| 类 | 说明 |
|------|------|
| `datetime` | 包含日期和时间的完整对象 |
| `date` | 仅包含日期(年,月,日) |
| `time` | 仅包含时间(时,分,秒,微秒) |
| `timedelta` | 时间差,用于日期时间运算 |
| `timezone` | 时区信息 |

##### 2.3 常用函数与方法

| 函数/方法 | 返回值 | 说明 |
|-----------|--------|------|
| `datetime.now()` | `datetime` 对象 | 当前本地日期时间 |
| `datetime.today()` | `datetime` 对象 | 同上 |
| `datetime(year, month, day, ...)` | `datetime` 对象 | 手动创建 datetime |
| `datetime.strptime(str, fmt)` | `datetime` 对象 | 将字符串按格式解析为 datetime |
| `datetime.strftime(fmt)` | 字符串 | 将 datetime 格式化为字符串 |
| `.date()` | `date` 对象 | 提取日期部分 |
| `.time()` | `time` 对象 | 提取时间部分 |

##### 2.4 常用示例

```python
from datetime import *

# 当前时间
now = datetime.now()
print(now)                     # 2024-10-29 17:14:09.994734

# 提取日期和时间
today = now.date()             # 2024-10-29
current_time = now.time()      # 17:14:09.994734

# 时间差计算
delta = timedelta(days=7, hours=3)
future = now + delta
print(future)                  # 一周零3小时后的时间

# 字符串解析与格式化
str_date = "2024-10-29 16:48:38"
dt = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")
print(dt.strftime("%A, %B %d, %Y"))   # Tuesday, October 29, 2024
```

---

#### 3. 常用格式化指令(`strftime` / `strptime`)

| 指令 | 含义 | 示例 |
|------|------|------|
| `%Y` | 四位年份 | 2024 |
| `%m` | 两位月份 | 10 |
| `%d` | 两位日 | 29 |
| `%H` | 24小时制小时 | 16 |
| `%I` | 12小时制小时 | 04 |
| `%M` | 分钟 | 48 |
| `%S` | 秒 | 38 |
| `%f` | 微秒(6位) | 994734 |
| `%A` | 星期几完整名称 | Tuesday |
| `%B` | 月份完整名称 | October |
| `%w` | 星期几(数字,0=周日) | 2 |
| `%j` | 一年中的第几天 | 303 |

---

#### 4. 与数学/算法的关联

| 应用场景 | 使用的函数 | 说明 |
|----------|-----------|------|
| 算法性能测试 | `time.perf_counter()` | 测量代码段执行时间 |
| 模拟实验计时 | `time.sleep()` | 控制模拟步长或限流 |
| 日志时间戳 | `datetime.now().strftime(...)` | 记录事件发生时间 |
| 数据分析时间序列 | `datetime` 与 `timedelta` | 处理日期索引和时间差计算 |
| 随机数种子初始化 | `time.time()` | 用当前时间作为随机种子 |

**示例:测量函数执行时间**

```python
from time import perf_counter

start = perf_counter()
# 执行一些计算
total = sum(range(10**7))
end = perf_counter()
print(f"耗时: {end - start:.6f} 秒")
```

---

#### 5. `time` vs `datetime` 选择指南

| 需求 | 推荐库 | 原因 |
|------|--------|------|
| 简单计时/延时 | `time` | `time.sleep()`, `time.perf_counter()` |
| 获取时间戳 | `time` | `time.time()` 直接返回 |
| 日期计算(加/减天数) | `datetime` | `timedelta` 方便 |
| 格式化输出 | `datetime` | `strftime` 更直观,支持更多格式 |
| 解析用户输入日期 | `datetime` | `strptime` 便捷 |
| 跨平台高精度计时 | `time.perf_counter()` | 不受系统时间调整影响 |

---

> **总结**:`time` 适合底层时间获取和性能计时,`datetime` 适合日期时间运算和格式化.两者配合使用,可满足从算法性能测试到数据时间序列处理的各种需求.掌握时间操作,你就能为程序增加“时间维度”的能力,这在数值模拟,日志分析和实际应用开发中都极为重要.

---

**相关笔记**:
- [[综合应用]] — 时间相关综合案例
- [[random库的使用]] — 可用当前时间作为随机种子
