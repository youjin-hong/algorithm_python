input = 20

def decimal_sort(number):
    prime_list = []  # 찾은 소수들을 저장할 빈 리스트 생성

    # 2부터 입력받은 숫자(20)까지 1씩 증가시키며 반복
    # 즉, num은 2, 3, 4, ..., 20이 됨. 이 숫자가 소수인지 검사할 주인공임
    for num in range(2, number+1):
        # 일단 이 숫자가 "소수"다라고 가정하고 시작하는 거임
        # 밑에서 검사하다가 나누어 떨어지는 수가 발견되면 그때 False로 바꿈
        is_prime = True   # 소수인지 판별하기 위한 flag 변수

        for i in prime_list:
            # 제곱근까지만 검사 (최적화)
            if i*i > num:
                break
            if num % i == 0:
                is_prime = False
                break

        # 내부 반복문이 끝난 후, 소수라고 판별되었을 때만 추가
        if is_prime:
            prime_list.append(num)

    return prime_list

def find_prime_list_under_number(number):

    return decimal_sort(number)


result = find_prime_list_under_number(input)
print(result)