input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0 # 문자열을 모두 '0'으로 만들기 위해 뒤집어야 하는 횟수를 세는 변수
    count_to_all_one = 0 # 문자열을 모두 '1'로 만들기 위해 뒤집어야 하는 횟수를 세는 변수

    # 만약 첫 숫자가 '0'이라면? -> 언젠가 '0' 덩어리를 뒤집어서 '1'로 만들어야 하므로,
    # '모두 1 만들기' 카운트를 1 올림
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    # 여기서는 달라지는 순간(환승역)만 체크하기 때문에
    # 맨 처음 출발하는 기차(첫 번째 숫자 덩어리)는 "달라지는 순간"이 없기 때문에
    # for문이 카운트를 못 해줌
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i+1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_zero, count_to_all_one)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)