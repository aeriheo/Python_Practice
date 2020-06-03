def solution(arr):
    answer = []
    be = -1
    for i in range(len(arr)):
        if arr[i]!=be:
            answer.append(arr[i])
            be = arr[i]
        else:
            be = arr[i]
    return answer

arr = [1,1,3,3,0,1,1]
ans = solution(arr)
print(ans)