# 멀리뛰기
# lv2

def solution(n):
    MOD = 1234567
    

    def comb(n, r):
        if r > n - r:  
            r = n - r
        answer = 1
        for i in range(1, r + 1):
            answer = answer * (n - r + i) // i
        return answer % MOD
    
    answer = 0
    for i in range(n // 2 + 1):
        # 2의 묶음 i개와 나머지 1로 이루어진 조합
        answer = (answer + comb(n - i, i)) % MOD
    
    return answer
