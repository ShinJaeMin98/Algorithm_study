def find(x):
    # 경로 압축으로 대표 노드 탐색
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # 이미 연결되어 있으면 제외
    if root_a == root_b:
        return False

    # 작은 집합을 큰 집합에 연결
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return True


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    parent = list(range(V + 1))
    size = [1] * (V + 1)
    edges = []

    for _ in range(E):
        a, b, weight = map(int, input().split())
        edges.append((weight, a, b))

    edges.sort()  # 가중치 기준 오름차순 정렬

    total_weight = 0
    selected_count = 0

    for weight, a, b in edges:
        if selected_count == V - 1:
            break

        if union(a, b):
            total_weight += weight
            selected_count += 1

    print(f"#{tc} {total_weight}")