def username_test(username,list):
    for letter in range(0,list.__len__()):
        if list[letter] == username:   
            return letter
    return -1

def password_test(password,list,letter):
    if list[letter] == password:
        return True
    else:
        return False
# 该函数可不使用，但需要mian函数内注释行

def main():
    userName = ("zhangsan","lisi","wangwu","zhaoliu","xiaolin","xiaohua")
    pwList=['123','456','789','246','abc','abc1234']
    flag = 0
    while True:
        username = input("请输入用户名:")
        letter=username_test(username,userName)
        if letter==-1:
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
        # if pwList[letter] != password:
        if password_test(password,pwList,letter)==False:
            print("密码不正确")
            flag += 1
            if flag == 3:
                print("密码输入超过3次")
                break
        else:
            print("登录成功")
            break

main()