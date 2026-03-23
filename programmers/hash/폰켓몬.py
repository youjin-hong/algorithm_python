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


# 두 번째 내 풀이
def solution(nums):
    hash_dict = dict()

    for num in nums:
        h = hash(num)
        hash_dict[h] = num

    return min(len(hash_dict), len(nums) // 2)

# 효율적인 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))