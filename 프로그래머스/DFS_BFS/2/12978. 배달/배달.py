import heapq

def solution(N, road, K):
    # 노드 간 관계를 저장하기 위한 graph
    graph = [[] for _ in range(N+1)]
    
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    # 출발점에서 해당 노드까지의 최소 비용을 저장 (출발점 1은 0으로 초기화)
    distances = [float("inf")] * (N+1)
    distances[1] = 0
    
    # 다익스트라 알고리즘 (최소 비용, 노드 순으로 push해야 비용을 기준으로 정렬됨)
    # heapq을 사용하는 이유 : 연산의 '중복 분출'을 막아 최단 시간을 보장
    """
    최단 거리 선점: 거리가 가장 짧은 노드가 항상 먼저 튀어나오므로,
                  특정 노드를 처음 만났을 때 그 거리가 무조건 최단 거리로 확정됩니다.
    불필요한 탐색 원천 차단: 이미 최단 거리로 확정된 노드는 나중에 더 긴 거리로 다시 튀어나와도
                          대기 조건(if distances[node] < dist)에서 단 한 줄만에 버려집니다.
    폭발적인 연산량 방지: 만약 deque를 쓰면 멀리 돌아가는 잘못된 경로를 기준으로 자식 노드들을 먼저 다 계산한 뒤,
                       나중에 지름길이 나올 때마다 이미 검사했던 수많은 자식 노드들을 처음부터 다시 재계산하는 
                       지옥(도미노 현상)에 빠집니다.
    """
    heap = []
    heapq.heappush(heap, (0, 1))
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        # 인접한 노드들의 최단 거리를 갱신하고, 충족하면 heap에 추가
        for next_node, next_cost in graph[node]:
            new_cost = dist + next_cost
            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))
                
    return sum(1 for d in distances if d <= K)
                
            

    return answer