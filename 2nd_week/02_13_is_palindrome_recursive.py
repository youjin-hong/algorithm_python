input = "abcba"

# 재귀함수는 문제의 범위를 조금씩 좁혀나가는 거예요.

def is_palindrome(string):
    if len(string) <= 1: return True
    if string[0] != string[-1]: return False # 문자열의 맨 앞과 문자열의 맨 뒤

    return is_palindrome(string[1:-1])

print(is_palindrome(input))


# 아니면 파이썬 슬라이싱 문법 [시작:끝:증감폭] 을 이용해서 "처음부터 끝까지 가되, 역순(-1)으로 가져와라"라는 뜻으로 쓸 수 있음
# 즉, 문자열을 뒤집은 것([::-1])이 원본과 같은지 확인하는 것임
# is_palindrome = input_string == input_string[::-1]





























