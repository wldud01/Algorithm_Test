# 기능개발
# lv 2

def solution(progresses, speeds):
    answer = []
    # 각 프로그램 마다 몇개의 기능이 배포되는지
    rest = []
    for p,s in zip(progresses,speeds):
        num = (100 - p)//s
        if num*s + p >= 100:
            rest.append(num)
        elif num*s + p <= 100:
            rest.append(num+1)
    #print(rest)
    buf = []
    count =1
    for idx,n in enumerate(rest):
        if idx == 0:
            buf.append(n)
        else:
            if buf[-1] > n:
                count+=1
                
            elif buf[-1] < n:
                answer.append(count)
                buf.pop()
                buf.append(n)
                count = 1
            elif buf[-1] ==n:
                count+=1
                
    answer.append(count)
    #print(answer)
              
    return answer
