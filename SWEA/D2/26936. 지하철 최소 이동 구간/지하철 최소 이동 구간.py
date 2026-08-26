from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접 리스트 (인덱스가 노드의 번호)
    graph = [[] for _ in range(V+1)]

    # graph에 입력 (역방향도 넣어줘서 관리)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())

    # start에서 각 노드까지의 이동 구간 수
    distance = [-1] * (V+1)

    # 탐색을 위한 큐 생성
    queue = deque([start])

    # 최초 start 자기 자신과의 거리 0로 초기화
    distance[start] = 0

    # 큐 순회
    while queue:
        current = queue.popleft()

        # end에 도달하면 종료
        if current == end:
            break

        # graph에서 현재 노드와 연결된 노드 확인하여 방문 진행
        for next_node in graph[current]:
            # 만약 연결된 노드가 방문한적 없는 노드일때만 진행
            if distance[next_node] == -1:
                # 현재 노드 + 1을 거리로 저장, queue에 연결 노드 추가
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    # end 노드로 이동한 적 없는 경우 '0'
    if distance[end] == -1:
        answer = 0
    else:
        answer = distance[end]

    print(f'#{tc} {answer}')