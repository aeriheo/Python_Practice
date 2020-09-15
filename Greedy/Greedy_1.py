# 큰 수의 법칙
data = input().split(" ")

# 배열 입력
arr = list(map(int, input().split(" ")))

m = data[1]
k = data[2]

# 오름차순으로 정리
arr = sorted(arr)

cnt = 0
sum = 0
for i in range(int(m)):
    if cnt < int(k) :
       sum += arr[-1]
       cnt += 1
    else :
        sum += arr[-2]
        cnt = 0

print(sum)
