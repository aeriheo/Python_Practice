def sum(arr):
    s = arr[0] + arr[1]
    print(s)

arr = list(map(int,input().split()))

while arr[0] != 0:
    sum(arr)
    arr = list(map(int,input().split()))