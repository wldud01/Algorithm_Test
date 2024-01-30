# 2019 카카오 개발자 겨울 인턴십
# 튜플
# Lv2

import re
from collections import Counter
def solution(s):
    answer = []
    # 집합 정렬
    s_re = re.sub(r"[^0-9]", " ",s)
    
    #s.sort(key = lambda x: len(x))
    s_split = s_re.split()
    s_count =dict(Counter(s_split))
    
    count = 0
    result = [0]*max(s_count.values())
    for idx,(k,v)in enumerate(s_count.items()):
        result[v-1] = int(k)
    return result[::-1]
