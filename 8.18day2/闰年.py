print("判断是否是闰年")
year = int(input("要查询的年份是:"))
if (year% 4 == 0 and year % 100 != 0 ) or year % 400 == 0 :
    print("%d是闰年" % (year)) 
else :
    print("%d不是闰年" % (year))