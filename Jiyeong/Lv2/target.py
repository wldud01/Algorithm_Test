# 요격 시스템
# Lv2

def solution(targets):
    # 시작점을 기준으로 정렬
    targets.sort(key=lambda x: x[0])

    count = 0
    end_point = -1

    for start, end in targets:
        if start > end_point:
            count += 1
            end_point = end - 1
        else:
            end_point = min(end_point, end - 1)

    return count
