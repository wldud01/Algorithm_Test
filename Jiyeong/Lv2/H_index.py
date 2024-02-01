# H-index
# Lv2

def solution(citations):
    answer = 0
    count=0   
    box_index=[] 
    citations.sort()
    for i,c in enumerate(citations):
        count=0              
        count=len(citations[i:])
        if c >= count:
            box_index.append(count)
        else:
            box_index.append(c)
            
    return max(box_index)
