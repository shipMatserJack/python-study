# 文档 https://docs.python.org/zh-cn/3/tutorial/datastructures.html#more-on-lists 
list = [1, 2, 3, 4, 8, 5]
list.append(6) # 添加元素
list.remove(1) # 删除元素
list.pop() # 删除最后一个元素
list.pop(0) # 删除第一个元素

list.sort() # 排序
list.reverse() # 反转
# list.clear() # 清空
list.copy() # 复制
list_count = list.count(1) # 统计元素个数
list_index = list.index(8) # 查找元素索引
list.insert(0, 0) # 插入元素

print(list)
print(list_count)
print(list_index)