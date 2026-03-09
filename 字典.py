# https://docs.python.org/zh-cn/3/tutorial/datastructures.html#dictionaries
my_dict = {'name': '张三', 'age': 18}
print(my_dict)
print(my_dict['name1']) # 获取元素，键不存在时报错
print(my_dict.get('name1')) # 获取元素，键不存在时返回None

my_dict['name'] = '李四' # 修改元素
my_dict['gender'] = '男' # 添加元素
my_dict.pop('age') # 删除元素
my_dict.clear() # 清空字典
print(my_dict)

print(my_dict.keys()) # 获取字典的键
print(my_dict.values()) # 获取字典的值
print(my_dict.items()) # 获取字典的键值对