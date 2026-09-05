str = input("请输入一句英文：")
count_upper = 0
count_lower = 0
count_digit = 0
for s in str:
    if s.isupper():  count_upper = count_upper+1
    if s.islower():  count_lower = count_lower+1
    if s.isdigit():  count_digit = count_digit+1
print("大写字符：", count_upper)
print("小写字符：", count_lower)
print("数字字符：", count_digit)
