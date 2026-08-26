from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map = [input() for _ in range(N)]

    # 시작점(2), 도착점(3) 찾기
    for i in range(N):
        for j in range(N):
            if map[i][j] == '2':
                start = (i, j)
            elif map[i][j] == '3':
                goal = (i, j)

    # 상 우 하 좌
    move_xy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    # BFS ([(시작점의 x좌표, 시작점의 y좌표, 이동 거리)])
    queue = deque([(start[0], start[1], 0)])

    # 방문여부
    visited = [[-1] * N for _ in range(N)]
    visited[start[0]][start[1]] = 0

    answer = 0

    while queue:
        x, y, dist = queue.popleft()

        # 만약 도착하면 중단
        if (x, y) == goal:
            answer = dist - 1
            break

        for m in move_xy:
            nx = x + m[0]
            ny = y + m[1]

            # 조건 밖인 상태(창고 밖, 이미 방문, 막힌 칸)의 경우 패스
            if not(0<= nx < N and 0 <= ny < N) or visited[nx][ny] == 0 or map[nx][ny] == '1':
                continue

            visited[nx][ny] = 0
            queue.append((nx, ny, dist + 1))

    print(f'#{tc} {answer}')