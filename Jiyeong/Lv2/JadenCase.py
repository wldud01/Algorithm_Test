# JadenCase 문자열 만들기
# Lv 2



def solution(s):
    answer = ''
    # 첫번째 문자 대문자
    # 그외 소문자
    # s가 주어지면 Jaden case 리턴
    string = s.split(' ')
    result = []
    for word in string:
        if len(word.strip()) < 1:
            result.append(word)
        else:
            sentence = word[0].upper() + word[1:].lower()
            result.append(sentence)
    answer = " ".join(result)
    
    
    return answer
