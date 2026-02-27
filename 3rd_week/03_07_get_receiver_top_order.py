top_heights = [6, 9, 5, 7, 4]

# stack이 아닌 반복문을 이용한 풀이

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    for i in range(len(heights) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if heights[i] <= heights[j]:
                answer[i] = j + 1
                break # 가장 먼저 만나는 탑이 정답이기 때문에 break 걸어서 멈춰야 함. 아니면 덮어씌우기가 됨

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))
