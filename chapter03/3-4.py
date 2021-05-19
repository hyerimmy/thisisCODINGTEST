# N, K 입력받기
n, k = map(int, input().split())

result = 0

while(n != 1):
  if(n % k != 0):
    n -= k
    result += 1
  else:
    n = n/k
    result += 1

print(result)