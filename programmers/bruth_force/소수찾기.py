from itertools import permutations


def is_prime(num):
    if num < 2: return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    all_numbers = set()

    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            all_numbers.add(num)

    count = 0
    for num in all_numbers:
        if is_prime(num):
            count += 1
    return count


