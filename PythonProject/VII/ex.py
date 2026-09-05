# 记忆化优化
from functools import lru_cache

@lru_cache(maxsize=None)
def fibo_opt(n):
    if n == 1 or n == 2:
        return 1
    return fibo_opt(n - 1) + fibo_opt(n - 2)
# 输出前20项,每行5个
for i in range(1, 21):
    print(f"{fibo_opt(i):>8}", end="  " if i % 5 != 0 else "\n")