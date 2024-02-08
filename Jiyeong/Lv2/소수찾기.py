# 소수찾기
# lv 2

def solution(numbers):
    from itertools import permutations
    prime_set = set()
    
    # 모든 숫자 조합을 검사
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            # 소수 판별
            if num > 1:
                is_prime = True
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_set.add(num)

    return len(prime_set)

