dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, cnt):
    global answer

    answer = max(answer, cnt)

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        # 범위를 벗어나면 이동 불가
        if not (0 <= nr < R and 0 <= nc < C):
            continue

        next_alpha = ord(board[nr][nc]) - ord('A')

        # 현재 경로에서 이미 본 알파벳이면 이동 불가
        if used[next_alpha]:
            continue

        used[next_alpha] = True
        dfs(nr, nc, cnt + 1)
        used[next_alpha] = False  # 돌아오면 사용 표시 해제

T = int(input())

for tc in range(1, T + 1):
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]

    used = [False] * 26
    answer = 0

    # 시작 칸의 알파벳 사용 표시
    start_alpha = ord(board[0][0]) - ord('A')
    used[start_alpha] = True

    dfs(0, 0, 1)

    print(f"#{tc} {answer}")