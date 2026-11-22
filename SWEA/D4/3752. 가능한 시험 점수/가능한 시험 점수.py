T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    total = sum(scores)

    # s점을 만들 수 있는지
    dp = [False] * (total + 1)
    dp[0] = True  # 모든 문제를 틀리면 0점

    for score in scores:
        # 같은 문제의 배점을 두 번 더하지 않도록 큰 점수부터 확인
        for current in range(total - score, -1, -1):
            if dp[current]:
                dp[current + score] = True

    # True의 개수를 세면 중복 점수는 한 번만 집계됨
    print(f"#{tc} {sum(dp)}")