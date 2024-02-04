# 행렬의 곱셈
# lv2

def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr2[0])
    arr2_copy = []
    buf = []
    # 전치
    for i in range(len(arr2[0])):
        for j in range(len(arr2)):
            buf +=[0]
        arr2_copy.append(buf)
        buf =[]
    # 초기화
    for i in range(row):
        for j in range(col):
            buf +=[0]
        answer.append(buf)
        buf =[]
    #print(answer)
    #print(arr2_copy)
    for j, r in enumerate(arr2):
        for i, c in enumerate(r):

            #print(i,j)
            arr2_copy[i][j] = c
    
    mul  =0
    for i,a1 in enumerate(arr2_copy):
        for j,a2 in enumerate(arr1):
            for idx,x in enumerate(a2):
                mul += a1[idx]*a2[idx]
            answer[j][i] =  mul
            mul = 0


    return answer
