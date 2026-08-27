from collections import deque

# BFS 함수 생성(시작값, edges)
def BFS(start, edges):
    visited = [False] * 100
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()

        # 추출한 현재 노드가 목표와 같다면 성공(1) 반환
        if node == 99:
            return 1

        for next_nodes in edges[node]:
            # 방문한적 노드의 경우만 진행
            if not visited[next_nodes]:
                visited[next_nodes] = True
                queue.append(next_nodes)

    return 0

for _ in range(10):
    T, N = map(int, input().split())

    # 순서쌍 저장
    edges = [[] for _ in range(100)]
    nums = list(map(int, input().split()))

    for i in range(0, len(nums), 2):
        idx, edge = nums[i], nums[i+1]
        edges[idx].append(edge)

    
    # BFS 시작
    result = BFS(0, edges)

    print(f"#{T} {result}")