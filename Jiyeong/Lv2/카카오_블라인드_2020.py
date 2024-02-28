# 문자열 압축
# Lv2

def solution(s):
    answer = 0
    # 모든 경우 시도하기
    # buf dict에 하나씩 시도해서 넣고
    # 넣어진 길이만큼 붙여서 최종 list에 넣기
    buf_dict = []
    short_length = 100000
    result =[]
    window = 1
    index = 0
    count = 0
    if len(s) ==1:
        answer =1
    while window < len(s) :
        start, end = index,index+window
       # print(start,end)
        if end > len(s):
            buf_dict.append([s[start:],1])
            index = 0
            window +=1
            #print(buf_dict)
            text = ''
            for buf in buf_dict:
                char,num = buf
                if num != 1:
                    text += str(num) + char
                else:
                    text += char
            #print(text)
            answer = min(len(text),short_length)
            short_length = answer
            result.append(text)
            #print(result)
            buf_dict = []
            start, end = index,index+window
            
        
        # 범위 표시
        alp = s[start:end]
        #print("char",alp)
        if start == 0:
            buf_dict.append([alp,1])
        else:
            #print(buf_dict[-1][0] )
            if start > 0 and buf_dict[-1][0] == alp:
                 buf_dict[-1][1] +=1
            else:
                buf_dict.append([alp,1])
                
        index+=window
        start+= window
        end+= window
        count+=1
        
    
    return answer
