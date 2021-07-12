# N, K 입력받기
n, k = map(int, input().split())

result = 0

while(n != 1):
  if(n % k != 0): # n이 k로 나누어 떨어지지 않으면 - 1씩빼기
    n -= k
    result += 1
  else: # n이 k로 나누어 떨어지면 - k로 나누기
    n = n/k
    result += 1

print(result)