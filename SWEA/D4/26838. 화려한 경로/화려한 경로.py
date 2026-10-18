TC = int(input())

for tc in range(1, TC + 1):
    N, M, K = map(int, input().split())
    colors = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 각 정점의 색을 비트로 표현
    color_bit = [0] * (N + 1)

    for v in range(1, N + 1):
        color_bit[v] = 1 << (colors[v] - 1)

    mask_count = 1 << K

    # dp[mask][v]: 사용한 색이 mask이고 v에서 끝나는 경로 수
    dp = [[0] * (N + 1) for _ in range(mask_count)]

    # 정점 하나짜리 경로로 시작
    for v in range(1, N + 1):
        dp[color_bit[v]][v] = 1

    answer = 0

    for mask in range(1, mask_count):
        color_count = bin(mask).count('1')

        for v in range(1, N + 1):
            count = dp[mask][v]

            if count == 0:
                continue

            # 정점이 2개 이상인 경로만 정답에 포함
            if color_count >= 2:
                answer += count

            for next_v in graph[v]:
                bit = color_bit[next_v]

                # 이미 사용한 색이면 이동 불가
                if mask & bit:
                    continue

                # 새 색을 추가하고 경로 수 누적
                new_mask = mask | bit
                dp[new_mask][next_v] += count

    print(answer)