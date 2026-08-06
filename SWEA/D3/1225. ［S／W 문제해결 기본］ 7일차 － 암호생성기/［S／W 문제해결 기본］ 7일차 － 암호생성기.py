from collections import deque

for _ in range(10):
    T = int(input())
    queue = deque(map(int, input().split()))
    cnt = [1, 2, 3, 4, 5]  
    
    i = 0 
    while True:
        num = queue.popleft() - cnt[i % 5]
        if num <= 0:
            queue.append(0)
            break
        queue.append(num)
        i += 1

    print(f'#{T}', *queue)