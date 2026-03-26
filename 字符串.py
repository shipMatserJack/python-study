# 文档 https://docs.python.org/zh-cn/3/tutorial/introduction.html#strings
my_string = "Hello, World!"
print(my_string)
print(my_string[0]) # 获取第一个字符
print(my_string[0:5]) # 获取前5个字符
print(my_string[0:5:2]) # 获取前5个字符，步长为2
print(my_string[::-1]) # 获取倒序字符
print(my_string.upper()) # 获取大写字符
print(my_string.lower()) # 获取小写字符
print(my_string.replace("Hello", "Hi")) # 替换字符
print(my_string.split(",")) # 分割字符串
print(my_string.join(["Hello", "World"])) # 拼接字符串
print(my_string.find("World")) # 查找字符串

# 实战：写一个函数，计算字符串中每个字符的个数
def count_characters(string):
  return len(string)

print(count_characters(my_string))
