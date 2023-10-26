def is_palindrome(s: str) -> bool:
   return s == s[::-1]

# Test cases
print(is_palindrome("121"))  # True
print(is_palindrome("123454321"))  # True
print(is_palindrome("abba"))  # True
print(is_palindrome("hello"))  # False