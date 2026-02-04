# 첫 번째 풀이 (브루트 포스 풀이)
# string에 있는 문자 하나당 한바퀴씩 순회하며 최빈값을 찾는 문제
def find_max_occurred_alphabet_1(string):
    # 이건 보너스로 해두면 좋을 것
    string = string.lower()
    # 모든 알파벳 당 string 길이만큼 순회를 돌 것이기 때문에 알파벳 배열 선언 및 초기화
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # 최빈값 정수 변수 선언 및 초기화
    max_occurrence = 0
    # 최빈값을 갖는 알파벳 선언 및 초기화
    max_alphabet = alphabet_array[0]

    # 우선 26번 순회할 거라 제일 겉에 알파벳 배열 for문 설정
    for alphabet in alphabet_array:
        occurrence = 0  # 현재 빈도 수
        for char in string:  # 알파벳 배열 안에서 각 string 문자를 순회할 것이라서 안쪽 for문 생성
            if char == alphabet:  # 현재 string 문자와 알파벳 배열 안의 알파벳과 같다면
                occurrence += 1   # 현재 빈도수 증가시키기

        if occurrence > max_occurrence:  # 만약 현재 빈도수가 최빈값보다 크면
            max_alphabet = alphabet  # 최빈값 갖는 알파벳으로 교체
            max_occurrence = occurrence  # 최빈값도 교체

    return max_alphabet

print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet_1("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet_1("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet_1("best of best youtube"))


# 두 번째 풀이 (빈도 배열로 카운트 + 최대값 갱신)
def find_max_occurred_alphabet_2(string):
    # 알파벳 인덱스 배열을 만든 거임. 여기에 이제 각 알파벳 순서에 따른 갯수 카운팅이 들어갈 예정
    alphabet_occurrence_array = [0] * 26

    # string 문자열 순회
    for char in string:
        # char가 알파벳이 아닐 경우를 대비
        if not char.isalpha():
            continue  # 만약 아니라면 이 if문을 빠져나와 다음 인덱스의 for문 시작
        # 알파벳이 맞다면 현재 char의 아스키코드를 가져와서 a의 아스키코드(97)과 뺼셈
        # 이렇게 해야 현재 알파벳 배열의 인덱스에 카운트 가능
        arr_index = ord(char) - ord('a')
        # 이제 알파벳 카운팅할 배열에 해당 인덱스 원소 증가시키기
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    # 이제 배열을 다 채웠으면 배열을 순회하면서 최빈값, 최빈값을 띄는 알파벳 찾을 거임
    for index in range(len(alphabet_occurrence_array)):
        # 여기 for문에서만 쓰는 변수 하나 만들어서 현재 알파벳 빈도수 저장
        alphabet_occurrence = alphabet_occurrence_array[index]

        # 만약 현재 빈도수보다 더 큰 빈도수가 있다면 교치
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))

result = find_max_occurred_alphabet_2
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
