def username_test(username,list):
    for letter in range(0,list.__len__()):
        if list[letter] == username:   
            return letter
        else:
            return False

def main():
    userName = ("zhangsan","lisi","wangwu","zhaoliu","xiaolin","xiaohua")
    pwList=['123','456','789','246','abc','abc1234']
    flag = 0
    while True:
        username = input("请输入用户名:")
        letter=username_test(username,userName)
        if letter==False:
            print("用户不存在")
            flag += 1
            if flag == 3:
                print("用户名输入超过3次")
                exit()
        else:
            break

    flag=0
    while True:
        password = input("请输入密码:")
        if pwList[letter] == password:
            print("密码错误")
            flag += 1
            if flag == 3:
                print("密码输入超过3次")
                break
        else:
            print("登录成功")

main()