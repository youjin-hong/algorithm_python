# 내 풀이
def solution(nums):
    dict = {}
    possible_count = len(nums) // 2
    count = 0

    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return min(len(dict), possible_count)


# 효율적인 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))