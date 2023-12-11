import pickle

try:
    a = 100
    b = "I am a student"
    list1 = [1, 2, 3, 4, 5, 6]
    dict1 = {"姓名": "张三", "毕业学校": "河南科技大学"}
    set1 = {3.5, 5, "abc"}
    data = [a, b, list1, dict1, set1]
    with open("bFile.dat", "wb") as f1:
        for item in data:
            pickle.dump(item, f1)
except Exception as e:
    print("写入数据失败%s" % e)
else:
    print("写入数据成功")
with open("bFile.dat", "rb") as f1:
    for item in data:
        print(pickle.load(f1))
