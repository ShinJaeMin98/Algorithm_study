# x가 속한 조의 대표 찾기
def find(x):
    # x가 대표가 아니면 부모 따라가기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# a와 b가 속한 조 합치기
def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # 대표가 다르면 동일하게 변경
    if root_a != root_b:
        parent[root_b] = root_a

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    parent = list(range(N + 1))

    # numbers에서 2개씩 꺼내서 union 실핼
    for i in range(0, M * 2, 2):
        union(numbers[i], numbers[i + 1])

    groups = set(find(i) for i in range(1, N + 1))

    print(f"#{tc} {len(groups)}")