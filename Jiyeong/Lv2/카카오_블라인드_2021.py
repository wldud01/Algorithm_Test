# 순위 검색
# Lv2

# 효율성을 제외한 코드
def solution(info, query):
    # info 지원자 query가 개발팀이 궁금해하는 조건
    # info 정보를 모두 각 col마다 조건을 넣어준다
    candidate = {}
    # 지원자 info
    for idx, i in enumerate(info):
        person = i.split(' ')
        candidate[idx] = person
    #print(candidate)
    condition = {}
    for idx , q in enumerate(query):
        q = q.replace('and ', '')
        con = q.split(' ')
        condition[idx] = con
    #print(condition)
    final = []
    # 지원자 한명씩 그 query를 모두 비교하는 2중 for문 작성
    for index, per in enumerate(condition):
        # index를 통해 지원자를 한명씩 불러옴
        req = condition[index]
        #print(req)
        PASS = 0
        for idx , q in enumerate(candidate.values()):  
            fail = 0
            for i, can in enumerate(q):
                if i == len(q)-1:
                    # 후보의 점수
                    score = int(can)
                    #print('score', score,req[-1])
                    if int(req[-1]) > score:
                        #print('score fail')
                        fail+=1
                        break
                else:
                    if can not in req:
                        if req[i] == '-':
                            pass
                        else: 
                            #print(can)
                            fail +=1
                            break
            #print(fail)
            if fail <= 0:
                PASS +=1  
        final.append(PASS)
    return final
