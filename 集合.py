# https://docs.python.org/zh-cn/3/tutorial/datastructures.html#sets
my_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

my_set.add('watermelon') # 添加元素
my_set.remove('apple') # 删除元素

my_set.clear() # 清空集合
print(my_set)

print('apple' in my_set) # 判断元素是否在集合中
print('apple' not in my_set) # 判断元素是否不在集合中

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b) # 差集
print(a | b) # 并集
print(a & b) # 交集
print(a ^ b) # 对称差集