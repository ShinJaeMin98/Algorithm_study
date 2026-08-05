# 단순 list 풀이
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(input().split())
    print(f'#{tc} {nums[M % N]}')