from collections import deque

# 상 우 하 좌
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def BFS(start, map):
    visited = [[False] * 16 for _ in range(16)]
    queue = deque([start])

    # 시작위치 방문 처리
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + moves[i][0]
            ny = y + moves[i][1]

            # 패스 - 벗어난 경우 not 0 <= nx, ny < 16 / 벽 (1) / 방문한 경우
            if not(0 <= nx < 16 or 0 <= ny < 16) or map[nx][ny] == '1' or visited[nx][ny]:
                continue
            # 목표인 '3'을 만난경우 성공(1) 반환
            elif map[nx][ny] == '3':
                return 1
            else:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return 0

for tc in range(10):
    T = int(input())
    
    # map 생성
    map = list(input() for _ in range(16))
    
    # 시작점, 도착점 찾기
    for i in range(16):
        for j in range(16):
            if map[i][j] == '2':
                start = (i, j)
                break
    
    # BFS 시작
    result = BFS(start, map)

    print(f"#{T} {result}")
