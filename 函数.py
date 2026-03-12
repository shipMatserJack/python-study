# 1. 定义函数
def add(a, b):
  return a + b

# 2. 调用函数
print(add(1, 2))

# 实战：写一个函数，计算列表中的最大值
def max_value(list):
  max_value = list[0]
  for i in list:
    if i > max_value:
      max_value = i
  print(max_value)

max_value([1, 2, 3, 4, 5])


# 实战：写一个函数， 计算列表中所有数字的平均值
def average(list):
  if len(list) == 0:
    return 0
  sum = 0
  for i in list:
    sum += i
  return sum / len(list)

print(average([1, 2, 3, 4, 5]))