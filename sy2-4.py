list1=[3 ,8 ,11 ,26 ,47]
new_element=int(input("请输入一个新的数字:"))
index=0
while index < len(list1) and new_element > list1[index]:
    index += 1
list1.insert(index, new_element)
print(list1)