def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "无效三角形"
    elif a == b == c:
        return "等边三角形"
    elif a == b or b == c or a == c:
        return "等腰三角形"
    elif a + b > c and b + c > a and a + c > b:
        return "一般三角形"
    else:
        return "无效三角形"

a,b,c=eval(input("请输入三角形三边长度(格式为：a,b,c)："))
# a,b,c=3,4,5
# a,b,c=5,5,5
# a,b,c=4,4,6
# a,b,c=0,4,5
# a,b,c=-1,2,3
# a,b,c=7,2,2
print(triangle_type(a,b,c))