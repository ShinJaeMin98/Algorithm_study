T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    visited = [False] * N
    min_cost = [float('inf')] * N
    min_cost[0] = 0

    total = 0

    for _ in range(N):
        # 아직 연결하지 않은 섬 중 연결 비용이 가장 작은 섬
        current = -1

        for i in range(N):
            if not visited[i]:
                if current == -1 or min_cost[i] < min_cost[current]:
                    current = i

        visited[current] = True
        total += min_cost[current]

        # 새로 연결한 섬을 통해 다른 섬의 연결 비용 갱신
        for next_node in range(N):
            if visited[next_node]:
                continue

            dx = xs[current] - xs[next_node]
            dy = ys[current] - ys[next_node]
            cost = dx * dx + dy * dy

            if cost < min_cost[next_node]:
                min_cost[next_node] = cost

    answer = int(total * E + 0.5)
    print(f"#{tc} {answer}")