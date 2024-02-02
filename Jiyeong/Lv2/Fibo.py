# 피보나치 수열
# Lv 2
# 재귀는 겹치는 연산이 많기 때문에 check해서 찾아쓰기

def solution(n):
    answer = 0
    count = 0
    check = [0] * (n+1)
    while n >= count:
        if count == 1 or count ==2:
            check[count] =1
            answer +=1
        elif count == 0:
            answer +=0
        else:
            answer = check[count-1] + check[count-2]
            check[count] = answer  
        count+=1
    
    answer = answer % 1234567
    return answer
        
