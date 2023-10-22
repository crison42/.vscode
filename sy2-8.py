list1 = ["Python","Java","Php","Java","Python"]
print("原列表=",list1)
new_list = list(set(list1))
new_list.sort(key=list1.index)
print("删除后列表=",new_list)
