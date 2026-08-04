T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    num = [1]      # 현재 넣을 숫자

    def inorder(node):
        # 1. 종료 조건
        if node > N:
            return

        # 2. 왼쪽 서브트리 방문
        inorder(node * 2)

        # 3. 현재 노드에 값 저장
        tree[node] = num[0]

        # 4. 다음 숫자로 증가
        num[0] += 1

        # 5. 오른쪽 서브트리 방문
        inorder(node * 2 + 1)

    # 루트부터 시작
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')