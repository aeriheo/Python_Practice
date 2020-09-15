# 1이 될 때까지

data = list(map(int, input().split(" ")))

# n = data[0], k = data[1]
n = data[0]
k = data[1]

cnt = 0
while n > 1:
    n -= 1
    n = n/k
    cnt +=1

print(cnt)