### 4-1.py ###

# 공간의 크기 N 입력받기
n = int(input())

# A가 이동할 계획 리스트로 입력받기
move = list(map(str, input().split()))

# x좌표와 y좌표
x = 1
y = 1

for i in range(len(move)):
  if (move[i] == "L"):
    if(y>1):
      y -= 1
  elif (move[i] == "R"):
    if(y<n):
      y += 1
  elif (move[i] == "U"):
    if(x>1):
      x -= 1
  elif (move[i] == "D"):
    if(x<n):
      x += 1

print(x , y)