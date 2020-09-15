# 숫자 카드 게임

# N * M 행렬
data = list(map(int, input().split(" ")))

# N 행만큼 for문 돌리기
card = []
min_max = []
for i in range(data[0]):
    tmp = list(map(int, input().split(" ")))
    min_max.append(min(tmp))
    card.append(tmp)

print(max(min_max))