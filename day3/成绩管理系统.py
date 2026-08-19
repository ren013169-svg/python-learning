scores={"小明":90,"小红":85,"小刚":78}
while True:
    print(1,"查看所有成绩")
    print(2,"添加学生")
    print(3,"查询某个学生成绩")
    print(4,"退出")
    choice=input("选择你的操作：")
    if choice =="1":
        print("所有学生成绩:")
        for name,score in scores.items():
            print(name,score)
        print("_"*20)
    elif choice == "2":
        print("添加学生")
        name=input("请输入学生姓名")
        if name in scores:
            print("该学生已存在！")
        else:
            try:
                score=int(input("请输入学生成绩"))
                scores[name]=score
                print(f"成功添加{name}:{score}分")

            except:
                print("成绩必须是数字！")
        print("_"*20)
    elif choice=="3":
        name=input("请输入要查询的姓名：")
        if name in scores:
            score=scores[name]
            print(name,score)
        else:
            print("查无此人！")
        print("_"*20)
    elif choice=="4":
        print("退出系统，再见！")
        break
    else:
        print("请输入1到4之间的数字")
        print("_"*20)
    