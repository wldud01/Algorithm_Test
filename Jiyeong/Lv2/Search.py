# 완전 탐색
# Lv 2

def solution(brown, yellow):
    # 레오가 본것이 브라운 테두리
    # 노란색이 주어짐 안에
    # 가로세로 크기 순서대로 배열에 담아
    
    # 일단 brown - 4를 빼 6 
    # 6 - yellow * 2 
    # w 4 4 * 2   
    # h 6 6 * 2
    # 최종 + 4
    # brown
    if yellow == 1:
        w , h =1,1
        return [w+2, h +2]
    for w in range(1,yellow):
        if yellow % w == 0:
            h = yellow // w
        if w * 2 + h * 2 + 4 == brown:
            #print(w,h)
            return [h+2,w+2]
        
