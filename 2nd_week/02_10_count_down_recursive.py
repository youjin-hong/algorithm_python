def count_down(number):
    # 무한 굴레에 빠지지 않도로 종료 조건 설정 해줘야 함
    if number < 0:
        return

    print(number)  # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!

count_down(60)