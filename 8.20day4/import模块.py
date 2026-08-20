import random
while True:
    user=input("按回车投骰子,按q退出")
    if user =='q':
        print("游戏结束")
        break
    else:
        num=random.randint(1,6)
        print(f"你的骰子数是{num}")
import math
try:
    x=float(input("请输入一个数字"))
    if x<0:
        print("负数不能开平方根")
    else:
        print(math.sqrt(x))
except:
    print("请输入数字！")

import datetime
today=datetime.date.today()
print(f"今天的日期是{today}")

