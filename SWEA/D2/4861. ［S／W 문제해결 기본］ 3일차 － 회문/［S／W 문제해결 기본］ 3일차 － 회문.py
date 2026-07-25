T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 입력 문자열을 굳이 list()로 안 쪼개고 문자열 그대로 두는 게 슬라이싱에 편함
    board = [input().strip() for _ in range(N)]
    
    # 세로 검사를 위해 zip으로 행과 열을 바꾼 뒤, 문자열 리스트로 다시 병합
    T_board = ["".join(col) for col in zip(*board)]

    ans = ""  # 정답을 담을 변수
    
    for i in range(N):
        for j in range(N - M + 1):
            # 1. 가로판에서 i번째 행의 j부터 j+M까지 슬라이싱
            txt = board[i][j : j + M]
            
            # 2. 세로판(T_board)에서 i번째 행의 j부터 j+M까지 슬라이싱
            T_txt = T_board[i][j : j + M]
    
            # 자른 조각(txt)과 뒤집은 조각(txt[::-1])이 같은지 비교
            if txt == txt[::-1]:
                ans = txt
                break
            elif T_txt == T_txt[::-1]:
                ans = T_txt
                break
                
        if ans: # 정답을 찾았다면 안쪽 j 루프에 이어 i 루프도 탈출
            break
            
    print(f'#{tc} {ans}')
