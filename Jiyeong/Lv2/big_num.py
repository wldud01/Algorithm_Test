# 큰수
# lv2
def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers_str = [str(num) for num in numbers]

    
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    #print(numbers_str)
    # 정렬된 문자열을 합쳐서 결과 생성
    answer = ''.join(numbers_str)
    
    return answer if answer[0] != '0' else '0'
