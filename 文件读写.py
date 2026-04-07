# 文件读写

# 打开文件
file = open('test.txt', 'r')

# 读取文件
content = file.read()
print(content)

# 关闭文件
file.close()