import heapq


def solution(board):
    N = len(board)

    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # dist[r][c][d]:
    # d 방향으로 이동해서 (r, c)에 도착했을 때의 최소 비용
    dist = [
        [[float('inf')] * 4 for _ in range(N)]
        for _ in range(N)
    ]

    for d in range(4):
        dist[0][0][d] = 0

    # (누적 비용, 행, 열, 이전 이동 방향)
    # -1은 시작점으로, 이전 이동 방향이 없다는 뜻
    pq = [(0, 0, 0, -1)]

    while pq:
        cost, r, c, direction = heapq.heappop(pq)

        # 이미 더 적은 비용으로 도착한 기록이 있다면 건너뛰기
        # 시작점(direction == -1)은 비교에서 제외
        if direction != -1 and cost > dist[r][c][direction]:
            continue

        # 최소 비용 상태부터 꺼내므로 목적지에서 바로 반환
        if r == N - 1 and c == N - 1:
            return cost

        for nd in range(4):
            nr = r + dr[nd]
            nc = c + dc[nd]

            # 범위를 벗어나면 건너뛰기
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 벽이면 건너뛰기
            if board[nr][nc] == 1:
                continue

            # 이동 비용 계산
            # 기본 비용은 100
            # 이전 방향이 존재하고, 다음 방향과 다르면 500 추가
            move_cost = 100
            if direction != -1 and direction != nd:
                move_cost += 500

            # 누적 비용 계산 및 방향별 최소 비용 갱신
            # cost + move_cost 계산
            # dist[nr][nc][nd]보다 작으면 갱신
            # (새 비용, nr, nc, nd)를 힙에 추가
            new_cost = cost + move_cost
            if new_cost < dist[nr][nc][nd]:
                dist[nr][nc][nd] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc, nd))

    return min(dist[N - 1][N - 1])