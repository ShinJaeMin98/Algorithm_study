from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, maze):
    visited = [[False] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = True
    
    q = deque([start])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < 16 and 0 <= ny < 16):
                continue
            elif maze[nx][ny] == 1 or visited[nx][ny]:
                continue
            elif maze[nx][ny] == 3:
                return 1
            else:
                visited[nx][ny] = True
                q.append((nx, ny))
            
    return 0


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_idx = (i, j)
                break
                         
    result = bfs(start_idx, maze)
                         
    print(f'#{tc} {result}')
                
    