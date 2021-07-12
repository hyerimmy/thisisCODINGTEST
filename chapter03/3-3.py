# N, M 입력받기
n, m = map(int, input().split())

result = 1

for i in range(n):
  data = list(map(int, input().split())) # 카드 값 입력받기
  data.sort()
  min = data[0]
  if(result < min):
    result = min

print(result)
