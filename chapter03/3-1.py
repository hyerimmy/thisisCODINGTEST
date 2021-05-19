n = 1260
count = 0

# 큰 단위 화폐부터 차례대로 배열로 생성
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count = count + n // coin
  n = n % coin

print(count)