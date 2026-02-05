input = "abadabac"

# 내 풀이
def find_not_repeating_first_character_1(string):
    # 맵? 딕셔너리에 넣어서 카운트 하고, 1이면 바로 반환
    # for문을 돌았는데도 없으면 '_' 반환
    result = {}

    for str in string:
        result[str] = result.get(str, 0) + 1

    for char in string:
        if result[char] == 1:
            return char

    return '_'

result = find_not_repeating_first_character_1
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))


# 쌤 풀이
def find_not_repeating_first_character_2(string):
    # string에서 알파벳의 빈도수를 저장할 배열 만들어서 초기값 0으로 초기화
    alphabet_occurrence_array = [0] * 26

    # 문자열 돌면서
    for char in string:
        if not char.isalpha():  # 우선 char가 알파벳인지 확인 (공백이거나 숫자일 수도 있으므로)
            continue # 알파벳이 아니면 if문 빠져나와서 다음 인덱스 순회
        arr_index = ord(char) - ord('a')  # 알파벳이면 char를 아스키코드로 바꿔서 97이랑 빼기
        alphabet_occurrence_array[arr_index] += 1 # 해당 알파벳 빈도수에 1 더해주기

    # 반복되지 않는 배열 요소 담는 배열 만들기
    not_repeating_character_array=[]
    # 알파벳 빈도수의 길이만큼 순회해서 이번엔 아이템이 아니라 인덱스로 접근할 것임
    for index in range(len(alphabet_occurrence_array)):
        # 현재 빈도수 저장할 변수 추가
        alphabet_occurrence = alphabet_occurrence_array[index]

        # 현재 순회하는 배열의 원소가 1이면
        if alphabet_occurrence == 1:
            # 반복되지 않는 요소 저장하는 배열에 추가 (원래 알파벳으로 변환해서)
            not_repeating_character_array.append(chr(index + ord('a')))

    # 문자열 다시 순회
    for char in string:
        # 반복하지 않는 요소 배열에 string 요소 char가 있으면
        if char in not_repeating_character_array:
            # 그 char 반환
            return char

    return '_'

result = find_not_repeating_first_character_2
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))