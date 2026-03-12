# 1. for循环
for i in range(5): # range(5) 生成一个从0到4的整数序列
    print(i)
for i in range(1, 5): # range(1, 5) 生成一个从1到4的整数序列
    print(i)
for i in range(1, 5, 2): # range(1, 5, 2) 生成一个从1到4的整数序列，步长为2
    print(i)


# 2. while循环
i = 0
while i < 5:
    print(i)
    i += 1

# 3. 嵌套循环
for i in range(5):
    for j in range(5):
        print(f"i = {i}, j = {j}")

# 4. 循环控制 break continue
for i in range(5):
    if i == 1:
      continue
    if i == 3:
      break
    print(i)

# 实战：计算1到100的和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 实战：用 while 循环写一个程序，让用户反复输入单词，直到输入 "exit" 为止，然后统计用户输入的单词个数
word_count = 0
while True:
  word = input("请输入单词：")
  if word == "exit":
    break
  word_count += 1
print(f"用户输入的单词个数为：{word_count}")
