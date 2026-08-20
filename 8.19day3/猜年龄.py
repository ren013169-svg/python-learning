import random
answer=random.randint(1,100)
match answer:
    case x if x<=10:
        print("small")
    case 11|12|13|14|15|16|17|18:
        print("teenager")
    case x if x>=18 and x<=99:
        print("easy")
    case 100:
        print(666)
print(answer)