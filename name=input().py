# 1. 获取用户输入
height = float(input("请输入你的身高(米)："))
weight = float(input ("请输入你的身高(米)"))

# 2. 计算BMI
bmi = weight / (height ** 2)

# 3. 输出BMI值，保留2位小数
print(f'你的bmi指数是:{bmi:.2f}')

# 4. 判断体型
if bmi < 18.5:
    print("体型判定：偏瘦")
elif 18.5 <= bmi <= 23.9:
    print("体型判定：正常")
elif 24 <= bmi <= 27.9:
    print("体型判定：超重")
else:
    print("体型判定：肥胖")