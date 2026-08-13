# i가 속한 집합의 루트 노드 찾기
def find(parent, i):
    if i == parent[i]:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

# 서로 다른 루트 노드 집합 합치기
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    # 랭크가 작은 트리를 큰 랭크의 트리 아래로 연결
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[yroot] < rank[xroot]:
        parent[yroot] = xroot
    # 동일한 경우, xroot를 최상위로 설정
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def solution(n, costs):
    # 비용을 기준으로 오름차순 정렬
    costs.sort(key=lambda x : x[2])
    
    # 각 노드의 부모를 추적하는 배열 생성 (초기값은 자기 자신)
    parent = [i for i in range(n)]
    
    # 각 노드의 트리의 랭크(뻗어갈 수 있는 노드 수)를 추적하는 배열
    rank = [0] * n
    
    # 최소 비용 / 최소 간선 수
    min_cost, edges = 0, 0
    
    for edge in costs:
        # 최대 간선 수만큼 포함된 경우 중단
        if edges == n-1:
            break
        # 현재 간선의 두 노드가 속한 집합의 루트 찾기
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        # 만약 두 노드의 루트 노드가 다른 경우 => 집합 합치기
        if x != y:
            union(parent, rank, x, y)
            min_cost += edge[2]
            edges += 1
            
    return min_cost
        
    