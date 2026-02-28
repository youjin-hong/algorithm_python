def solution(genres, plays):
    total_plays = {}
    genre_songs = {}

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]

        if g not in total_plays:
            total_plays[g] = 0
            genre_songs[g] = []

        total_plays[g] += p
        genre_songs[g].append((p, i))

    sorted_genres = sorted(total_plays.items(), key=lambda item: item[1], reverse=True)
    result = []

    for genre in sorted_genres:
        songs = sorted(genre_songs[genre[0]], key=lambda item: (-item[0], item[1]))

        for song in songs[:2]:
            result.append(song[1])

    return result
