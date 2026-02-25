input = "abcba"

# 재귀함수는 문제의 범위를 조금씩 좁혀나가는 거예요.

def is_palindrome(string):
    if len(string) <= 1: return True
    if string[0] != string[-1]: return False # 문자열의 맨 앞과 문자열의 맨 뒤

    return is_palindrome(string[1:-1])

print(is_palindrome(input))