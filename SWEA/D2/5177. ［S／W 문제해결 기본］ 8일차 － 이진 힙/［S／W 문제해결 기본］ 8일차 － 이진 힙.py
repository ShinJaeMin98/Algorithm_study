# parent = i // 2
# left = i * 2
# right = i * 2 + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    
    # 0번은 비우고 heap 생성
    heap = [0]

    for num in input().split():
        # 숫자 하나씩 추가
        heap.append(int(num))

        # 현재 위치 (idx)
        child = len(heap) - 1

        # 현재 위치가 루트가 아닌 경우
        while child > 1:
            # 부모 위치 찾기
            parent = child // 2

            # 부모가 더 작거나 같으면 최소 힙 완성
            if heap[parent] <= heap[child]:
                break

            # 부모와 자식 교환
            heap[parent], heap[child] = heap[child], heap[parent]

            # 조건을 충족할 때까지 부모 방향으로 올라감
            child = parent

    # 마지막 노드의 위치
    last_idx = len(heap) - 1

    # 마지막 노드이 부모들의 합
    while last_idx > 1:
        last_idx //= 2
        ans += heap[last_idx]

    print(f'#{tc} {ans}')