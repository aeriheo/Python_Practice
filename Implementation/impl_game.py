# map 크기
size = input().split(" ")
n = int(size[0])
m = int(size[1])

# 캐릭터 위치
loc = input().split(" ")
a = int(loc[0])
b = int(loc[1])
d = int(loc[2])

# 맵 설정
arr = []
for i in range(n):
    g_map = input().split(" ")
    arr.append(g_map)

now = 0
cnt = 1
while now == 0 :
    if a-1>=0 and arr[a-1][b] == '0': # 육지인지 확인
        a -= 1
        cnt += 1
        arr[a][b] = '-'  # 방문표시
    elif a+1<n and arr[a+1][b] == '0':
        a += 1
        cnt += 1
        arr[a][b] = '-'
    elif b-1>=0 and arr[a][b-1] == '0' :
        b -= 1
        cnt += 1
        arr[a][b] = '-'
    elif b+1<m and arr[a][b+1] == '0' :
        b += 1
        cnt += 1
        arr[a][b] = '-'
    else:
        now = 1

print(cnt)