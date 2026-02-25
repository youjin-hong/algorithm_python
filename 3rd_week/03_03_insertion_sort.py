input = [4, 6, 2, 9, 1]

# 여기에서 가장 앞에 있는 것을 기준으로 "이미 정렬된 상태"이다라는 것이 삽입 정렬의 가장 큰 특징임
# 선택 정렬이랑 다르게 얘도 O(N^2)이긴 하지만, 빅 오메가 표기법의 경우 O(N)도 가능(전부 다 잘 정렬되어 있는 경우)
def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))