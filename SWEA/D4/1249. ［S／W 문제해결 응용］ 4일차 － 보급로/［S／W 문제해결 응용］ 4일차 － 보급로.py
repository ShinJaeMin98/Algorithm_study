import heapq

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    
    times = [[float('inf')] * N for _ in range(N)]
    times[0][0] = 0
    
    # (누적 복구 시간, 행, 열)
    pq = [(0, 0, 0)]
    
    while pq:
        time, r, c = heapq.heappop(pq)
        
        # 만약 누적 복구 시간이 해당 위치의 최신 최단 복구 시간보다 크다면 건너뛰기
        if time > times[r][c]:
            continue
            
        # 종료 조건
        if r == N - 1 and c == N - 1:
            break
        
        # 방향 이동
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            
            # 범위 벗어나면 건너뛰기
            if not (0 <= nr < N and 0 <= nc < N):
                continue
                
            new_time = times[r][c] + maps[nr][nc]
            if times[nr][nc] > new_time:
                times[nr][nc] = new_time
                heapq.heappush(pq, (new_time, nr, nc))
                
    print(f'#{tc} {times[N-1][N-1]}')
    