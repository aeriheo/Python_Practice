def solution(board, moves):
    answer = 0
    st = []
    for i in moves:
        num = i-1
        e=0
        while board[e][num]==0 :
            e+=1
            if e== len(board[0]):
                break
        if e!=len(board[0]):
            st.append(board[e][num])
            board[e][num]=0
    x = 0
    y = 1
    while len(st) > 0:
        if y == len(st):
            break
        elif st[x] == st[y]:
            st.pop(y)
            st.pop(x)
            answer += 2
            x = 0
            y = 1
        else:
            x += 1
            y += 1
    print(st)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
ans = solution(board,moves)
print(ans)