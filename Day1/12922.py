def solution(n):
    answer = ''
    for i in range(n):
        num = (i+1)%2
        if num == 0:
            answer += '박'
        else :
            answer += '수'
    return answer

n = 5
ans = solution(n)
print(ans)