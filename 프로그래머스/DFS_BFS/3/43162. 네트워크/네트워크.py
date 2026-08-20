def dfs(computers, visited, node):
    # 노드 방문 처리
    visited[node] = True
    
    # 해당 노드의 연결 정보를 idx와 연결 여부(1 or 0)으로 순회
    for idx, connected in enumerate(computers[node]):
        # 만약 연결되어 있고, 방문하지 않은 노드라면
        if connected and not visited[idx]:
            # 이어서 해당 노드의 연결 확인
            dfs(computers, visited, idx)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        # 방문하지 않은 노드라면 (연결되지 않은 노드라면)
        if not visited[i]:
            dfs(computers, visited, i)
            # 해당 노드와 연결된 노드를 모두 방문했다는 것이므로 answer +1
            answer += 1
            
    return answer