def find(x):
    # parent[x] == x가 될 때까지 부모를 따라가서 x의 대표 노드 반환
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # 대표가 같으면 이미 연결된 노드이므로 간선 추가 X
    if root_a == root_b:
        return False

    # 작은 집합을 큰 집합에 합치고 size 갱신
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return True


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    parent = list(range(V + 1))
    size = [1] * (V + 1) # 대표가 x인 집합에 포함된 노드 수
    buckets = [[] for _ in range(11)]

    # 가중치 w에 해당하는 버킷에 간선 저장
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        buckets[w].append((n1, n2))

    total_weight = 0 # 선택한 간선의 가중치 합
    selected_count = 0  # 선택한 간선 수

    # 가중치가 작은 간선부터 확인
    for w in range(1, 11):
        for n1, n2 in buckets[w]:
            # 사이클 없이 연결할 수 있다면 선택
            if union(n1, n2):         
                total_weight += w
                selected_count += 1
			# 노드 V+1개를 연결하려면 간선 V개 필요
            if selected_count == V:  
                break

        if selected_count == V:
            break

    print(f"#{tc} {total_weight}")