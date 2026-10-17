from collections import deque

# 상, 하, 좌, 우, 대각선(상좌, 상우, 하좌, 하우)
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    while q:
        r, c = q.popleft()

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]

            # 배열 범위를 벗어나면 continue
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 지뢰이거나 이미 방문한 칸이면 continue
            if board[nr][nc] == '*' or visited[nr][nc]:
                continue

            # 다음 칸 방문 처리
            # 숫자가 1 이상이어도 여기서 공개됨
            visited[nr][nc] = True

            # 다음 칸의 주변 지뢰 수가 0이면 큐에 넣기
            if counts[nr][nc] == 0:
                q.append((nr, nc))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    # 각 칸의 주변 지뢰 수
    counts = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 1. 주변 지뢰 수 계산
    for r in range(N):
        for c in range(N):
            if board[r][c] == '*':
                continue

            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                # 범위 안이고, 해당 이웃이 지뢰라면
                # counts[r][c]를 1 증가
                if (0 <= nr < N and 0 <= nc < N) and board[nr][nc] == '*':
                    counts[r][c] += 1     
    answer = 0

    # 2. 아직 공개되지 않은 0 영역 클릭
    for r in range(N):
        for c in range(N):
            # 지뢰가 아니고, 주변 지뢰 수가 0이며,
            # 아직 방문하지 않았다면
            # 클릭 횟수 증가 후 bfs 호출
            if board[r][c] != '*' and counts[r][c] == 0 and not visited[r][c]:
                answer += 1
                bfs(r, c)

    # 3. 자동으로 공개되지 않은 나머지 빈 칸 클릭
    for r in range(N):
        for c in range(N):
            # 지뢰가 아니고 아직 방문하지 않았다면
            # 클릭 횟수 증가
            if board[r][c] != '*' and not visited[r][c]:
                answer += 1

    print(f"#{tc} {answer}")