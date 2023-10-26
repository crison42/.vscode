def is_palindrome(s: str) -> bool:
   return s == s[::-1]

string = input("请输入字符串")
if is_palindrome(string):
    print(string+" 是回文")
else:
    print(string+" 不是回文")