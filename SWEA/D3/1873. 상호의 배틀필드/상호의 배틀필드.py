# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

tank = "^v<>"
commands_dir = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]

    N = int(input())
    commands = input()

    # 전차의 초기 위치와 방향 찾기
    for i in range(H):
        for j in range(W):
            if board[i][j] in tank:
                r, c = i, j
                direction = tank.index(board[i][j])

    for command in commands:
        if command == 'S':
            # 전차 바로 앞 칸부터 포탄 이동
            nr = r + dr[direction]
            nc = c + dc[direction]

            while 0 <= nr < H and 0 <= nc < W:
                # 벽돌 벽: 파괴하고 포탄 소멸
                if board[nr][nc] == '*':
                    board[nr][nc] = '.'
                    break

                # 강철 벽: 포탄만 소멸
                if board[nr][nc] == '#':
                    break

                # 평지와 물은 통과
                nr += dr[direction]
                nc += dc[direction]

        else:
            # 이동할 수 없어도 방향은 변경
            direction = commands_dir[command]
            board[r][c] = tank[direction]

            nr = r + dr[direction]
            nc = c + dc[direction]

            # 맵 안에 있고 평지일 때만 이동
            if 0 <= nr < H and 0 <= nc < W:
                if board[nr][nc] == '.':
                    board[r][c] = '.'
                    r, c = nr, nc
                    board[r][c] = tank[direction]

    # 첫 번째 행 앞에만 테스트 케이스 번호 출력
    print(f'#{tc}', end=' ')
    for row in board:
        print(''.join(row))