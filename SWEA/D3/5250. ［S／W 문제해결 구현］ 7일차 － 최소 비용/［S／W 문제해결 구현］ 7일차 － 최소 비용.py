import heapq

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    
    fuels = [[float('inf')] * N for _ in range(N)]
    fuels[0][0] = 0
    
    # 연료, 행, 열
    pq = [(0, 0, 0)]
    
    while pq:
        fuel, r, c = heapq.heappop(pq)
        
        # 꺼내온 연료가 최신 최소 연료보다 크면 패스
        if fuel > fuels[r][c]:
            continue
            
        # 목적지 도착하면 종료
        if r == N-1 and c == N-1:
            break
            
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            
            # 범위 벗어나면 패스
            if not (0 <= nr < N and 0 <= nc < N):
                continue
                
            # 연료량 계산(기본 1, 이동한 칸이 더 크면 그만큼 추가)
            used_fuel = 1
            if maps[nr][nc] > maps[r][c]:
                used_fuel += (maps[nr][nc] - maps[r][c])
                
            new_fuel = fuel + used_fuel
            if fuels[nr][nc] > new_fuel:
                fuels[nr][nc] = new_fuel
                heapq.heappush(pq, (new_fuel, nr, nc))
                
    print(f'#{tc} {fuels[N-1][N-1]}')        