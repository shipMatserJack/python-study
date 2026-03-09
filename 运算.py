# 1. 数字运算
a = 10
b = 20
print("a + b =", a + b) # 加法
print("a - b =", a - b) # 减法
print("a * b =", a * b) # 乘法
print("a / b =", a / b) # 除法
print("a % b =", a % b) # 取余
print("a ** b =", a ** b) # 幂运算 a的b次方
print("a // b =", a // b) # 整除 a除以b的整数部分

# 2. 字符串运算
a = "hello"
b = "world"
print(len(a)) # 字符串长度
print("a + b =", a + b) # 字符串拼接
print("a * 3 =", a * 3) # 字符串重复
print("a[0] =", a[0]) # 字符串索引
print("a[0:3] =", a[0:3]) # 字符串切片 从索引0开始到索引3结束
print("a[0:3:2] =", a[0:3:2]) # 字符串切片 从索引0开始到索引3结束，步长为2

# 3. 布尔运算
a = True
b = False
print("a and b =", a and b) # 布尔与
print("a or b =", a or b) # 布尔或
print("not a =", not a) # 布尔非

# 4. 类型转换
a = 10
b = str(a)
print("b =", b) # 类型转换
print(type(b)) # 类型转换

num_str = "10"
num_int = int(num_str)
num_float = float(num_str)
print("num_int =", num_int) # 类型转换
print("num_float =", num_float) # 类型转换
print(type(num_int)) # 类型转换
print(type(num_float)) # 类型转换


# 练习：写一个计算器，输入两个数字，输出它们的和、差、积、商
calculator = input("请输入两个数字：")
calculator = calculator.split()
a = int(calculator[0])
b = int(calculator[1])
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)