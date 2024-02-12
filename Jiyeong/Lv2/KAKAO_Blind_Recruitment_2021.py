def solution(cap, n, deliveries, pickups):
    # cap만큼 꽉 채워서 일단 deliver
    # 빈공간 생기면 pickup
    # 꽉차면 다시 돌아가기
    # delivery와 pickups가 0 될 때까지 반복
    answer = 0
    
    total_d = sum(deliveries)
    total_p = sum(pickups)
    
    index_d=-1
    index_p=-1
    start_cap = cap
    #print(start_cap , "ss start_cap")
    while total_d + total_p > 0:

        index_d +=1
        location_d = deliveries[index_d]
        #print("location_D",location_d)
        
        if start_cap >= location_d:
            start_cap -= location_d
            deliveries[index_d] = 0
            total_d -= location_d
            #print(deliveries)
            #print(pickups)
            print(start_cap , "start_cap")
            if start_cap == 0 or index_d == n-1:
                answer += (index_d+1)*2
                print("start")
                print(index_d)
                p_cap = cap
                for index in range(index_d+1):
                    location_p = pickups[(index_d-1)-index]
                    if total_d == 0:
                        index_p+=1          
                    
                    if p_cap >= location_p:
                        p_cap -= location_p
                        pickups[(index_d-1)-index] = 0
                        total_p-=location_p
                    print(p_cap , "p_cap")
                    if total_p == 0:
                        break
                    
                index_d = -1
                start_cap = cap
        total_d = sum(deliveries)
        total_p = sum(pickups)
        
        #print("--------------")
        
    return answer
