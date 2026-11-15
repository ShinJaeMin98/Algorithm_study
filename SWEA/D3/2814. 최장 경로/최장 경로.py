def dfs(node, length):
    global answer
    answer = max(answer, length)

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, length + 1)
            visited[next_node] = False  # 다른 경로에서도 방문할 수 있도록 복구


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [set() for _ in range(N + 1)]

    # 무방향 그래프 구성, 중복 간선 제거
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].add(y)
        graph[y].add(x)

    visited = [False] * (N + 1)
    answer = 1

    # 모든 정점을 시작점으로 탐색
    for start in range(1, N + 1):
        visited[start] = True
        dfs(start, 1)  # 경로의 길이는 정점 개수
        visited[start] = False

    print(f"#{tc} {answer}")