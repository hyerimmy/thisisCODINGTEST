# N, M, K 입력받기
n, m, k = map(int, input().split())

# N개의 수 입력받기
data = list(map(int, input().split()))

# 가장 큰 값과 그 다음으로 큰 값 구하기
data.sort()
first = data[n-1] # 가장 큰 값
second = data[n-2] # 두번째로 큰 값

# 반복한계 기준
full = 0
result = 0

for i in range(m) :
  if(full==k):
    full=0
    result += second
  else:
    full += 1
    result += first

print(result)
