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