from collections import deque

def solution(info, edges):
    # 트리 구축 함수 (idx가 부모, 값들이 자식)
    def build_tree(info, edges):
        tree = [[] for _ in range(len(info))]
        for edge in edges:
            tree[edge[0]].append(edge[1])
        return tree
    
    # 트리 생성
    tree = build_tree(info, edges)
    max_sheep = 0
    
    # BFS를 위한 큐 생성 및 초기 상태 설정
    # BFS : 너비 우선 탐색 - 루트 노드부터 시작하여 각 레벨의 노드를 모두 방문하고
    #                       다음 레벨의 노드 방문
    # (현재 위치, 양의 수, 늑대 수, 방문한 노드 집합)
    queue = deque([(0, 1, 0, set())])
    
    # BFS 시작
    while queue:
        # 상태 가져오기
        current, sheep_cnt, wolf_cnt, visited = queue.popleft()
        # visited에 현재 노드의 이웃 노드 추가
        visited.update(tree[current])
        
        # 인접한 노드들에 대해 탐색
        for near_node in visited:
            # 만약 늑대(1, True)인 경우
            if info[near_node]:
                # 늑대를 추가해도 양의 수와 일치하지 않는 경우에는 새롭게 queue에 추가
                # 양과 늑대 수가 같아지는 상태는 더 이상 탐색하지 않는다. (queue에 추가하지 않음)
                if sheep_cnt != wolf_cnt + 1:
                    queue.append(
                        (near_node, sheep_cnt, wolf_cnt + 1, visited - {near_node})
                    )
                    
            # 만약 양(0)인 경우
            else:
                # 새롭게 queue에 추가
                queue.append(
                    (near_node, sheep_cnt + 1, wolf_cnt, visited - {near_node})
                )
        max_sheep = max(max_sheep, sheep_cnt)
        
    return max_sheep