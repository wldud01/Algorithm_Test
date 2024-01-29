# 뒤에 있는 큰 수 찾기
# Lv2


def solution(numbers):
    answer = [-1] * len(numbers)  # 모든 요소에 대해 초기값을 -1로 설정
    stack = []  # 이전 요소들의 인덱스를 저장할 스택

    for idx, num in enumerate(numbers):
        # 스택이 비어있지 않고 현재 요소가 스택의 맨 위에 있는 요소보다 크면
        while stack and numbers[stack[-1]] < num:
            last_idx = stack.pop()  # 스택에서 인덱스를 꺼내고
            answer[last_idx] = num  # 해당 인덱스의 '다음으로 큰 요소'를 현재 요소로 설정
        stack.append(idx)  # 현재 요소의 인덱스를 스택에 추가

    return answer
