# N개의 최소 공배수
# Lv2

def solution(arr):
    answer = 0
    arr.sort()
    mini = arr[-1]
    answer = arr[-1]
    index = 1
    finish = len(arr)-1
    #print(arr)
    while finish >0:
        
        for a in arr[0:-1]:
            #print(a,"a")
            if answer%a == 0:
                #print(a)
                finish-=1
        if finish ==0:
            break
        else:
            index +=1
            answer = mini*index
            finish = len(arr)-1
    return answer
