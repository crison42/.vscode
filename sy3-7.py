import random

def random_number(times):
    a=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]
    b=["01","02","03","04","05","06","07","08","09","10","11","12"]
    while times>0:
        list1=random.sample(a,5)
        list1.sort()
        list2=random.sample(b,2)
        list2.sort()
        list=list1+list2
        sum=""
        times-=1
        for i in range(list.__len__()):
            sum+=str(list[i])
            sum+=" "
        print(sum)

print("软工2213班常洪的大乐透号码生成器")
times=int(input("请输入要生成的大乐透号码注数:"))
random_number(times)