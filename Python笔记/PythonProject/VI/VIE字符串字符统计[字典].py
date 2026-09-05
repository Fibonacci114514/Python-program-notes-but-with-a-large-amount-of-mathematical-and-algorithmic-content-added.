sentence =input()
sentence = sentence.lower()  # 将句中字符都统一成小写
  # 上一句非必要
counts = {}
for c in sentence:
    counts[c] = counts.get(c, 0) + 1
print(counts)