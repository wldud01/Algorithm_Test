# 두 큐의 합

def solution(queue1, queue2):
    answer = 0
    from collections import deque
    # 한개의 pop 한번의 insert
    # 크면 다른쪽에 넣고 작으면 채우고
    # 어떤 경우도 같은 수ㄹ가 될 없는 경우 return -1
    # 뒤에 두 수를 비교
    # q1_sum q2_sum 큰쪽에 수 빼기
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    #print(q1_sum,q2_sum)
    
    if (q1_sum + q2_sum)%2 !=0:
        return -1
    else: 
        target = (q1_sum + q2_sum)//2
    
    # 나머지 값의 조합이 큐 안에 존재하면 된다
    maximum = 0
    if q1_sum == target and q1_sum == q2_sum:
        return 0
    # q1이 더 큰경우
    else:
        while maximum != len(queue1)*2+len(queue2):
            if q1_sum == q2_sum:
                break
            elif q1_sum > q2_sum:
                back = q1.popleft()
                maximum +=1
                answer +=1
                q2.append(back)
                q1_sum -= back
                q2_sum += back
                #print("q1_sum", q1, q2)

            # q2가 더 큰경우
            elif q2_sum > q1_sum:
                back = q2.popleft()
                maximum +=1
                answer+=1
                q1.append(back)
                q1_sum += back
                q2_sum -= back
                #print("q2_sum", q1, q2)
        #print(maximum)
    if q1_sum !=q2_sum:
        return -1
    return answer
