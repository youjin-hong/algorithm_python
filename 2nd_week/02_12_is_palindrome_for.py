input = "abcba"


# 내 풀이
def is_palindrome(string):
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

print(is_palindrome(input))


# 선생님 풀이
def is_palindrome2(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i - 1]:
            return False
    return True

print(is_palindrome2(input))