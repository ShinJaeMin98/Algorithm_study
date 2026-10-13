import heapq

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        
    dist = [float('inf')] * (N+1)
    dist[0] = 0
    
    pq = []
    heapq.heappush(pq, (0, 0))
    
    while pq:
        min_dist, min_idx = heapq.heappop(pq)
        if min_dist > dist[min_idx]:
            continue
            
        for target_idx, target_dist in graph[min_idx]:
            new_dist = target_dist + dist[min_idx]
            if new_dist < dist[target_idx]:
                dist[target_idx] = new_dist
                heapq.heappush(pq, (new_dist, target_idx))
                
    print(f'#{tc} {dist[N]}')
    