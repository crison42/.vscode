str=input("请输入想要使用的算法："+"\n"
          +"1.冒泡排序"+"\n"
    +"2.选择排序"+"\n"
    +"3.插入排序"+"\n"
    +"4.快速排序"+"\n"
    +"5.归并排序"+"\n"
    +"6.希尔排序"+"\n")
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
imported_module.main()

