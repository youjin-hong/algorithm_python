# "많이", "가장 많이"가 나온다면 일단 "정렬"을 생각해보자

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# -> genre_array에서 genre별로 재생횟수를 모두 모아서 비교해준다. 그리고 가장 많이 재생된 장르 별로 노래를 2곡씩 넣어줄거다.
# 어떤 값이 올지 모름
# !!!!! 특정 key 값에 대해서 value를 모아서 합쳐주고 싶다.
# !!!!! 특정 key 값은 아직 정해지지 않은 상황 => dictionary 사용하기
def get_melon_best_album(genre_array, play_array):
    # 첫 번째 딕셔너리: dict에 장르별로 얼마나 재생횟수를 가지고 있는가 -> genre_total_play_dict
    # 두 번째 딕셔너리: dict에 장르별로 어느 인덱스에 몇 번 재생횟수를 가지고 있는가

    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    for i in range(n):
        genre = genre_array[i]  # classic
        play = play_array[i]    # 500

        if genre in genre_total_play_dict: # classic 이라는 key값이 있었으면
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else: # key값이 없는 상황이라면
            genre_total_play_dict[genre] = play # 500
            genre_index_play_array_dict[genre] = [[i, play]]

    # 장르별로 가장 재생횟수가 많은 장르들 중, 곡수가 많은 순서대로 2개씩 출력하기
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item:item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item:item[1], reverse=True)

        # 장르별로 제일 잘 나가는 2곡만 넣으라는 조건을 만족해야 함
        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2: break

            result.append(index)
            genre_song_count += 1


    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))