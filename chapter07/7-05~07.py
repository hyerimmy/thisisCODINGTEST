### 7-05~07.py ###
### [실전문제] 부품 찾기 ###

# 가게 부품 개수와 부품번호 입력받기
n = int(input())
a = list(map(int, input().split()))
a.sort()

# 손님 부품 개수와 부품번호 입력받기
m = int(input())
b = list(map(int, input().split()))
b.sort


for i in range(0,m):
  result = "no"
  for j in range(0,n):
    if a[j] == b[i]:
      result = "yes"
  print(result, end=' ')