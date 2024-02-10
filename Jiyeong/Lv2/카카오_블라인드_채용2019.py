# 카카오 블라인드 채용
# lv 2
def solution(record):
    answer = []
    # 새로운 닉네임으로 다시 들어가기
    # 채팅방에서 닉네임 변경
    # 변경한 기록이 담긴 문자열 배열 Record가 매개변수로 주어진다
    # 모른 처리기록 후 최종으로 개설할 사람이 보게될 문자열 배열
    # 배열 구성 Enter Change, Leave id , nickname
    # id1234 Muzi Muzi prodo
    # id4567 prodo Ryan
    # 결과 prodo Ryan Prod Prodo
    # Enter , Enter Leave Enter
    # prodo enter/ Ryan enter /prodo leave/ prodo/ Enter
    state_list = []
    id_list = []
    id_dict = dict()
    # 기록 저장
    for idx,r in enumerate(record):
        if len(r.split(' ')) > 2:
            state, Id, name = r.split(' ')
        else:
            state,Id = r.split(' ')
        if Id not in id_dict:
            id_dict[Id] = [name]
            id_list.append(Id)
            state_list.append(state)
        else:
            if state == 'Leave':
                state_list.append(state)
                id_list.append(Id)
                id_dict[Id].append(id_dict[Id][-1])
            else:
                id_dict[Id].append(name)
                state_list.append(state)
                id_list.append(Id)
    #print(state_list)
    #print(id_dict)
    #print(id_list)
    state_index = 0
    for i in id_list:
        state_now = state_list[state_index]
        id_now = id_dict[i][-1]
        # 들어온 경우
        if state_now == 'Enter':
            answer.append(f"{id_now}님이 들어왔습니다.")
        # 나간경우
        elif state_now == 'Leave':
            answer.append(f"{id_now}님이 나갔습니다.")
        else: pass
        state_index+=1
        
    
    return answer
