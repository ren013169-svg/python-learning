scores={"小明":90,"小红":85,"小刚":78}
def show_all(scores):
    for name,score in scores.items():
        print(name,score)    
    print("_"*20)

def add_student(scores,name,score):
    if name in scores:
        print("该姓名已经存在")
    else:
        try:
            score_num=float(score)
            if score_num<0 or score_num>100:
                print("请输入合理成绩！")
            else:
                scores[name]=score_num
                print(f"成功添加{name}:{score}分！")
        except:
            print("请输入学生成绩")
    print("_"*20)
def query_student(scores, name):
    if name in scores:
        return f"{scores[name]}分"
    else:
        return("该生不存在。请确认学生姓名")
def delete_student(scores, name):
    if name in scores:
        scores.pop(name)
        print("删除成功！")
    else:
        print("该生不存在。请确认学生姓名")
def show_average(scores):
    sum_score=0
    for name,score in scores.items():
        sum_score = sum_score +score
    avg =round(sum_score /len(scores),2)
    return avg
while True:
    print(1,"查看所有成绩")
    print(2,"添加学生")
    print(3,"查询某个学生成绩")
    print(4,"删除学生")
    print(5,"算平均分")
    print(6,"退出")
    choice=input("选择你的操作：")
    if choice =="1":
        print("展示学生成绩") 
        show_all(scores)
    elif choice == "2":
        name=input("请输入学生姓名")
        score=input("请输入学生成绩")
        add_student(scores, name, score)
    elif choice == "3":
        name = input("请输入学生姓名")
        print(query_student(scores, name))
    elif choice == "4":
        name = input("请输入学生姓名")
        delete_student(scores, name)
    elif choice == "5":
        print("平均分是",show_average(scores))
        
    elif choice=="6":
        print("退出系统，再见！")
        break
    else:
        print("请输入1到6之间的数字")
        print("_"*20)
        


    
