T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = nums[M%N]
    print(f'#{tc} {ans}')