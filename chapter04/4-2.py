### 4-2.py ###

# 시간 N 입력받기
n = int(input())

count = 0

for i in range(n+1): #1부터 h까지 (시)
  for j in range(60): #1부터60까지 (분)
    for k in range(60): #1부터 60까지 (초)
      # 만약 3이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)