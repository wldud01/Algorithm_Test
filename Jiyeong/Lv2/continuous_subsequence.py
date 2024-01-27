# 연속된 부분 수열의 합
# Lv2

def solution(sequence,k):
  left = 0
  right = 0
  # 현재 합
  current_sum = sequence[0]

  result = [ 0, float("inf") ] 
  # 끝까지 돌때까지
  while right < len(sequence):
    # 현재까지 더한 값이 k와 같은 경우
    if current_sum  == k:
      # 더 포함되는 수가 적은 값을 넣는다
      if right-left < result[1] - result[0]:
        result = [left,right]
        right +=1
      # 아직 right가 sequence 끝으로 안갔을 때
      if right < len(sequence):
        current_sum += sequence[right]
        # 이동해서 값을 더해준다
    elif current_sum < k:
      right +=1
      if right < len(sequence):
          current_sum += sequence[right]
    else:
      # 값이 k 보다 큰 경우에는 이전에 더한 값을 빼준다
      current_sum -=sequence[left]
      left +=1
      # 왽쪽으로 이동 한 후에 오른쪽 값보다 커진 경우에는
      if left > right and left < len(sequence):
        # 둘다 끝으로 도착한 경우이다
        right = left
        current_sum = sequence[left]

  return result

