T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0] * 10 for _ in range(10)]
    cnt = 0
    
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                # board의 색이 0인 경우 색칠
                if board[i][j] == 0:
                    board[i][j] = color   
                    
                # board의 색이 0이 아니고 자신의 색도 아닌 경우 cnt +1
                elif board[i][j] != color:
                    cnt += 1
    print(f'#{tc} {cnt}')