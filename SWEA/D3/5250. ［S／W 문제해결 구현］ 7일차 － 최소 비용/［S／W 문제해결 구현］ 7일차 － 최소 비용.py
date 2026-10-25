import heapq


def dijkstra():
    # 전체 구역에 대한 거리 배열
    dist = [[float('inf')] * N for _ in range(N)]

    # 시작은 연료 소비량 0
    dist[0][0] = 0

    # (행, 열, 누적 연료)
    pq = [(0, 0, 0)]

    while pq:
        r, c, fuel = heapq.heappop(pq)

        # 이미 더 적은 연료로 방문한 기록이 있다면 건너뛰기
        if fuel > dist[r][c]:
            continue
        
        # 목적지에 도착하면 최소 연료 반환
        if r == N - 1 and c == N - 1:
            return fuel

        # 방향 전환
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 벗어나면 건너뛰기
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 다음 칸으로 이동하는 데 필요한 연료 계산
            # 다음 칸이 더 높으면 높이 차이만큼 추가
            move_cost = 1
            if heights[nr][nc] > heights[r][c]:
                move_cost += (heights[nr][nc] - heights[r][c])

            # 다음 칸까지의 누적 연료 계산 후 최소 비용 갱신
            # 1. 현재 누적 연료 + 이동 비용 계산
            # 2. dist[nr][nc]보다 작은지 확인
            # 3. 더 작다면 dist 갱신
            # 4. (새 누적 연료, nr, nc)를 힙에 추가
            new_cost = dist[r][c] + move_cost
            if dist[nr][nc] > new_cost:
                dist[nr][nc] = new_cost
                heapq.heappush(pq, (nr, nc, new_cost))
            
    return dist[N - 1][N - 1]


# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]

    answer = dijkstra()

    print(f"#{tc} {answer}")