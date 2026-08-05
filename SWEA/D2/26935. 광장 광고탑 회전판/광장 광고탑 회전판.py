# 단순 list 풀이
# T = int(input())
# for tc in range(1, T+1):
#    N, M = map(int, input().split())
#    nums = list(input().split())
#    print(f'#{tc} {nums[M % N]}')    
    
# deque 풀이
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque(list(input().split()))

    for _ in range(M % N):
        n = queue.popleft()
        queue.append(n)

    print(f'#{tc} {queue.popleft()}')