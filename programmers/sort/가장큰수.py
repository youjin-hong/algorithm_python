def solution(numbers):
    str_arr = []

    for num in numbers:
        str_arr.append(str(num))

    str_arr.sort(key=lambda item: item * 3, reverse=True)

    return str(int(''.join((str_arr))))

# 문자열 더 쉽게 만들기
def solution(numbers):
    str_arr = list(map(str, numbers))

    str_arr.sort(key=lambda item: item * 3, reverse=True)

    return str(int(''.join((str_arr))))