def solution(arr):
    answer = 0
    num = 0
    for i in arr:
        num += i
    answer = num / len(arr)
    return answer

arr = [1,2,3,4]
ans = solution(arr)
print(ans)