from collections import deque

def solution(maps):
    # 상, 우, 하, 좌
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    # 맵의 크기 저장 (상대방 진영은 각각 -1)
    n, m = len(maps), len(maps[0])
    
    # 각 구간 별 거리 저장 배열 초기화
    dist = [[-1] * m for _ in range(n)]
    
    def bfs(start): # start : [0,0]
        # 시작 위치를 queue에 추가, 거리 갱신
        queue = deque([start])
        dist[start[0]][start[1]] = 1
        
        while queue:
            current = queue.popleft()
            
            # 현재 위치에서 이동할 수 있는 모든 방향 탐색
            for move in moves:
                row, col = current[0] + move[0], current[1] + move[1]
                
                # 이동한 위치가 범위를 벗어나거나 벽(0)이 있는 경우 continue
                if row < 0 or row >= n or col < 0 or col >= m or maps[row][col] == 0:
                    continue
                
                # 이동한 위치가 처음 방문하는 경우, queue에 추가하고 거리 갱신
                if dist[row][col] == -1:
                    queue.append([row, col])
                    dist[row][col] = dist[current[0]][current[1]] + 1
                    
        return dist
    
    bfs([0,0])
    

    return dist[n-1][m-1]