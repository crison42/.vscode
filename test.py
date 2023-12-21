def encrypt_four_digit_number(number):
   number_str = str(number)
   encrypted_digits = []
   for digit in number_str:
       encrypted_digit = (int(digit) + 5) % 10
       encrypted_digits.append(str(encrypted_digit))

   encrypted_digits[0], encrypted_digits[3] = encrypted_digits[3], encrypted_digits[0]
   encrypted_digits[1], encrypted_digits[2] = encrypted_digits[2], encrypted_digits[1]

   encrypted_number = str("".join(encrypted_digits))

   return encrypted_number

data1 = eval(input("请输入一个四位整数:"))
data2 = encrypt_four_digit_number(data1)
print("加密后的数字为:",data2,sep = '')
