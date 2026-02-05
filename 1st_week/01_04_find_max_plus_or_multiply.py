# 내 풀이
# 시간복잡도는 쌤 코드와 같이 O(n)이지만 0이 나왔을 때도 굳이 곱하기 계산을
# 수행하고 버리기 때문에 비효율적임
def find_max_plus_or_multiply_1(array):
    result = array[0]

    for num in array[1:]:
        result = max(result*num, result+num)

    return result

result = find_max_plus_or_multiply_1
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))

# 쌤 풀이
# 이 문제의 핵심은 0과 1일 때는 더하고, 그 외에는 곱하는 것이 유리하다는 greedy 규칙을 찾아내는 것임
# 이 풀이는 조건에 따라 필요한 연산만 골라서 수행하기 때문에 효율성, 가독성, 알고리즘 구현 측면에서 우수
def find_max_plus_or_multiply_2(array):
    plus_or_multiply_sum = 0 # 대입연산
    for number in array: # N의 길이만큼 반복 -> for문이므로 최악의 경우 시간복잡도 O(n)
        if number <= 1 or plus_or_multiply_sum <= 1:
            plus_or_multiply_sum += number
        else:
            plus_or_multiply_sum *= number

    return plus_or_multiply_sum

plus_or_multiply_sum = find_max_plus_or_multiply_2
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))


# 처음 접근 방법
# 1) array를 내림차순으로 정렬하고 (이것부터가 쓸 데가 없는 짓이었음)
# 2) 배열 원소가 0보다 크면 곱하고 0보다 작거나 같으면 더하기로
# -> 그러나, 무조건 곱한다고 다 큰 게 아님.
# eg) 1+2=3 > 1*2=2

# 두 번째 접근 방법
# 결과 변수를 하나 생성한다. 여기엔 배열 원소 첫 번째 값을 넣어줌
# for문은 1번 인덱스부터 끝까지 돌면서 곱한 거랑 더한 것 중에
# 큰 수를 result에 계속 누적
# 반환

# 선생님 접근 방법
# 무작정 곱한다고 큰 수가 아님 (1+2=3 > 1*2=2와 같은)
# 1) 그래서 result 변수를 만들어서 0으로 초기화하고,
# 2) for문을 돌면서 배열 원소가 1보다 작거나 같은 경우 또는 result 변수가 1보다 작거나 같은 경우
# 3) 더하고
# 4) 그 외의 경우는 다 곱해준다