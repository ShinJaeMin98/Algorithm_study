T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 원소 하나만 고르면 부분 수열의 길이는 1
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            
            # j에서 끝나는 수열 뒤에 i번째 원소를 붙일 수 있는지 확인
            if numbers[j] <= numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"#{tc} {max(dp)}")