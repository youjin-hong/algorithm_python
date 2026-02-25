numbers = [1, 1, 1, 1, 1]
target_number = 3


# 이 문제는 한 번에 풀기 어려우면 케이스를 좁혀서 풀어나갈 수 있다.
# numbers = [2, 3, 1]
# target_number = 0
# 1. +2 +3 +1 = 6
# 2. +2 +3 -1 = 4

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N-1의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 된다는 소리이다.

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = [] # 모든 경우의 수를 저장할 리스트

    # 플러스 혹은 마이너스로 모든 경우의 수를 구하는 함수를 만들자
    # 함수 안에 함수를 만든 이유는, all_ways를 공짜로 사용할 수 있기 때문(클로저)
    # 그리고 이 함수에서만 쓰이는 함수라는 걸 보여줄 수도 있기 때문
    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array): # 탈출 조건
            all_ways.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    print('all_ways is', all_ways)

    target_count = 0

    for way in all_ways:
        if target == way:
            target_count += 1
    return target_count


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))