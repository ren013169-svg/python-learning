TODO_FILE="todo.txt"
def load_todos():
    try:
        with open(TODO_FILE,"r",encoding="utf-8") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError :
        return []
def save_todo(lines):
    with open(TODO_FILE,"w",encoding="utf-8") as f:
        f.writelines(lines)
def show_all():
    todo_list= load_todos()
    if not todo_list:
        print("暂无待办")
        return
    else:
        for idx,line in enumerate(todo_list,start=1):
            clean = line.strip()
            print(f"{idx}.{clean}")
def add_todo():
    content = input ("请输入待办内容:")
    if not content:
        print("待办不能为空")
        return
    new_line = f"[ ]{content}\n"
    with open (TODO_FILE,"a",encoding="utf-8") as f:
        f.write(new_line)
    print("添加成功!")
def mark_done():
    todo_list=load_todos()
    if not todo_list:
        print("暂无待办!")
        return
    show_all()
    num_str = input("请输入要标记完成的编号").strip()
    if not num_str.isdigit():
        print("无此项，请确认编号!")
        return
    num = int(num_str)
    index = num -1
    if index <0 or index >= len(todo_list):
        print("无此项，请确认编号")
        return
    old_line = todo_list[index]
    new_line=old_line.replace("[ ]","[x]",1)
    todo_list[index]=new_line
    save_todo(todo_list)
    print("标记完成！")
def delete_todo():
    todo_list=load_todos()
    if not todo_list:
        print("暂无待办")
        return
    show_all()
    num_str=input("请输入要删除的编号:")
    if not num_str.isdigit():
        print("无此项，请确认编号")
        return
    num=int(num_str)
    index=num-1
    if index < 0 or index>=len (todo_list):
        print("无此项，请确认编号!")
        return
    todo_list.pop(index)
    save_todo(todo_list)
    print("删除成功")
def menu():
    while True:
        print("待办清单")
        print("1.查看全部待办")
        print("2.添加待办")
        print("3.标记完成")
        print("4.删除待办")
        print("5.退出")
        choice=input("请选择：").strip()
        if choice =="1":
            show_all()
        elif choice =="2":
            add_todo()
        elif choice =="3":
            mark_done()
        elif choice =="4":
            delete_todo()
        elif choice =="5":
            print("程序退出")
            break
        else:
            print("请输入1-5有效数字")


if __name__ =="__main__":
    menu()
