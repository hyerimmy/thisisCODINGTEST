### 4-3.py ###

# 현재 나이트 위치 입력받기
input = input()
row = int(input[1])
col = int(ord(input[0])) - int(ord('a')) + 1

print(row, col)

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]

result = 0

for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]

  # 범위를 벗어나지 않았으면 결과값에 1 더하기
  if(1<=next_row<=8 and 1<=next_col<=8):
    result += 1

print(result)