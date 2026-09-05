def prime_factors_optimized(n):
   factors = []
   # 处理偶数因子
   while n % 2 == 0:
       factors.append(2)
       n //= 2
   # 检查奇数因子
   divisor = 3
   while divisor * divisor <= n:
       while n % divisor == 0:
           factors.append(divisor)
           n //= divisor
       divisor += 2
   # 如果剩余的是质数
   if n > 2:
       factors.append(n)
   return factors
n=int(input())
f=prime_factors_optimized(n)
w=sorted(list(set(f)))
a=['({}^{})'.format(i,f.count(i)) for i in w]
print('{}={}'.format(n,'×'.join(a)))