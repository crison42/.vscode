str=input("请输入想要使用的检索策略："+"\n"
          +"1.基于顺序表的顺序查找"+"\n"
    +"2.基于链表的顺序查找"+"\n"
    +"3.基于顺序表的折半查找"+"\n"
    +"4.基于二叉排序树的查找"+"\n"
    +"5.基于开放地址法的散列查找"+"\n"
    +"6.基于链地址法的散列查找"+"\n")
imported_module = ""
if str=="1":
    imported_module=__import__("6-1")
elif str=="2":
    imported_module=__import__("6-2")
elif str=="3":
    imported_module=__import__("6-3")
elif str=="4":
    imported_module=__import__("6-4")
elif str=="5":
    imported_module=__import__("6-5")
elif str=="6":
    imported_module=__import__("6-6")
else:
    print("输入错误")