T = int(input())
INF = float("inf")

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 대각선도 INF로 두어 사이클의 길이를 계산
    dist = [[INF] * N for _ in range(N)]

    for _ in range(M):
        s, e, c = map(int, input().split())
        dist[s - 1][e - 1] = c  # 일방통행 도로

    # k를 경유하는 경로가 더 짧으면 갱신
    for k in range(N):
        via = dist[k]

        for i in range(N):
            row = dist[i]
            to_k = row[k]

            if to_k == INF:
                continue

            for j in range(N):
                new_dist = to_k + via[j]
                if new_dist < row[j]:
                    row[j] = new_dist

    # 각 정점에서 출발해 돌아오는 사이클 중 최솟값
    answer = min(dist[i][i] for i in range(N))

    if answer == INF:
        answer = -1

    print(f"#{tc} {answer}")