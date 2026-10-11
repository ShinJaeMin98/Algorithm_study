import heapq

T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))  # 일방통행

    dist = [float('inf')] * (N + 1)
    dist[0] = 0
    pq = [(0, 0)]  # (거리, 정점)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        if current_node == N:
            break

        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight

            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    print(f"#{tc} {dist[N]}")