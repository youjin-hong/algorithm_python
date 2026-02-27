def solution(numbers):
    str_arr = []

    for num in numbers:
        str_arr.append(str(num))

    str_arr.sort(key=lambda item: item * 3, reverse=True)

    return str(int(''.join((str_arr))))