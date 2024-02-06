# 의상
# lv 2

def solution(clothes):
    answer = 0
    
    wear_dict = dict()
    for idx,cloth in enumerate(clothes):
        clo,tag = cloth
        if tag not in wear_dict:
            wear_dict[tag] = [clo]
        else:
            wear_dict[tag].append(clo)
    #print(wear_dict)
    wear_only = len(wear_dict.values())
    
    wear_num = []
    num = 1
    for i in wear_dict.values():
        wear_num.append(len(i))
    #print(wear_num)
    for w in wear_num:
        num *= (w+1)
    answer = num -1
    
    
    return answer 
