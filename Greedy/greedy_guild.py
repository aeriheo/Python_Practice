# 모험가 길드 문제

n = int(input())
human = input().split(" ")
human.sort()
cnt = 0
arr = []
while len(human) >0:
    n = int(human[-1])
    x = len(human) - n
    arr.append(human[x:])
    del human[x:]
cnt = len(arr)
print(cnt)