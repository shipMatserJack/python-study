# 基础结构 if elif else
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
else:
    print("不及格")


# 实战：猜数字小游戏
target_num = 66
guess_num = int(input('猜一个1～100的数字'))

if guess_num == target_num:
  print('猜对了')
elif guess_num > target_num:
  print('猜大了')
else:
  print('猜小了')