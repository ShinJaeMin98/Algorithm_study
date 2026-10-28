# 8방향 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    # 가운데 돌 4개 배치
    mid = N // 2
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1
    board[mid][mid] = 2

    for _ in range(M):
        x, y, color = map(int, input().split())

        # 입력 방향 주의!!
        r = y - 1
        c = x - 1
        board[r][c] = color

        # 흑돌 : 1 <-> 백돌 : 2
        opponent = 3 - color

        # 방향 순회
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]

            # 이 방향에서 뒤집을 후보 좌표 (같은 방향으로 계속 갔을때 나의 색과 같은지 확인 후 처리)
            candidates = []

            while 0 <= nr < N and 0 <= nc < N:
                # 빈칸이면 이 방향의 탐색 종료
                if board[nr][nc] == 0:
                    break

                # 상대 돌을 만난 경우
                elif board[nr][nc] == opponent:
                    candidates.append((nr, nc))

                # 내 돌을 만난 경우
                else:
                    # candidates에 저장한 돌들을 모두 color로 바꾼 뒤 이 방향의 탐색 종료
                    for c_r, c_c in candidates:
                        board[c_r][c_c] = color
                    break

                # 같은 방향으로 한 칸 더 이동
                nr += dr[d]
                nc += dc[d]

    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f"#{tc} {black} {white}")