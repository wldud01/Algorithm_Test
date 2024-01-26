def solution(friends, gifts):
    # 다음 달에 누가 많이 선물을 받을까요
    answer = 0
    gift_give = dict()
    #gift_rate = 준 선물 - 받은 선물
    # 서로 주고 받아본 경우 
    # 서로 주고 받아보지 않은 경우
    
    for g in gifts:
        a,b = g.split(' ')
        if a in gift_give:
            gift_give[a].append(b)
        else:
            gift_give[a] = [b]
    gift_take = list()
    #print(gift_give)
    for g in gift_give.values():
        gift_take += g
    #print(gift_take)
    gift_rate = dict()
    for f in friends:
        if f in gift_give:
            gift_rate[f] = len(gift_give[f]) - gift_take.count(f)
        else:
            gift_rate[f] = 0 - gift_take.count(f)
    #print(gift_rate)
    next_month = dict()
    for i,a in enumerate(friends):
        next_month[a] = 0
        for j,b in enumerate(friends):
            if i != j and b in gift_give and a in gift_give:
                #print(gift_give[a].count(b), gift_give[b].count(a))
                if gift_give[a].count(b) > gift_give[b].count(a):
                    next_month[a] +=1
                elif gift_give[a].count(b) == gift_give[b].count(a):
                    if gift_rate[a] > gift_rate[b]:
                        next_month[a] +=1
            elif i != j and not b in gift_give or not a in gift_give:
                if gift_rate[a] > gift_rate[b]:
                    next_month[a] +=1
    #print(next_month)
    answer = max(next_month.values())
    return answer
