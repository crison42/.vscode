import re


def is_valid_phone_number(phone_number):
    pattern = re.compile(r"^1[0-9]\d{9}$")
    return bool(pattern.match(phone_number))


if __name__ == "__main__":
    while True:
        phone_number = input("请输入手机号，输入-1程序结束:")
        if phone_number == "-1":
            break
        elif is_valid_phone_number(phone_number):
            print("您输入的手机号格式正确")
        else:
            print("您输入的手机号格式不正确")
