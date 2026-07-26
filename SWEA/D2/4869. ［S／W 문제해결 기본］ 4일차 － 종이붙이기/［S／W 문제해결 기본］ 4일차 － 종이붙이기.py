# 피보나치 활용
"""
import math

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 20 X 10 짜리로 꽉 채우고 시작
    cnt =  1

    # 20 X 20 짜리를 하나씩 늘려 나갈 수 있을 때까지
    # (20짜리 갯수 + 10짜리 갯수)! / (20짜리 갯수)! * (10짜리 갯수)! X (20짜리를 가로로 놓는 경우의 수)
    for i in range(1, (N//20) + 1):
        cnt += (math.factorial(N // 10 - i) // (math.factorial(i) * math.factorial(N // 10 - i*2))) * (2 ** i)

    print(f'#{tc} {cnt}')
 """
    
 # DP 점화식으로 접근
T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10

    # 공간 생성
    dp = [0] * (N + 1)

    # 10 X n 크기의 직사각형을 채우는 방법의 수
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N + 1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    print(f'#{tc} {dp[N]}')

    