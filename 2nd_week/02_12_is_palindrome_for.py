input = "abcba"

# 이 풀이들은 재귀를 이용한 풀이가 아님

# 내 풀이
def is_palindrome(string):
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

print(is_palindrome(input))


# 선생님 풀이
def is_palindrome2(string):
    n = len(string)  # 문자열의 길이
    for i in range(n): # 문자열의 길이만큼 반복
        if string[i] != string[n - i - 1]: # i번째 인덱스랑 맨 뒤에 있는 인덱스를 비교하고 싶음
            return False
    return True

print(is_palindrome2(input))

