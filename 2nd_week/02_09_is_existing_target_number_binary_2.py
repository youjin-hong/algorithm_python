finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 사실 이 문제는 이진 탐색이 안됨
# 왜냐면 배열이 무작위로 정렬된 배열에서는 이진 탐색을 쓸 수가 없음

def is_exist_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_guess != target:
        if current_guess == target:
            return True
        elif current_guess > target:
            current_max = current_guess - 1
        else:
            current_min = current_guess + 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)