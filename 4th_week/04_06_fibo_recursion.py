input = 20

# 재귀를 이용한 피보나치 수열은 input이 100 정도로 커지면 연산량이 너무 많아져서 에러남
# => 동적 계획법을 사용해야 함
def fibo_recursion(n):
    if n == 1 or n == 2: return 1

    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765