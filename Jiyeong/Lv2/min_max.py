# 최대값 최소값
# Lv2

def solution(s):
    answer = ''
    # 숫자중 최소값과 최대값
    result = s.split()
    result.sort(key=lambda x: int(x))
    answer = str(result[0]) + ' ' + str(result[-1])

    return answer
