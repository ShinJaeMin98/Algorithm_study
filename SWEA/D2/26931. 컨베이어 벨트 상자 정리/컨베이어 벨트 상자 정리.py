T = int(input())

for tc in range(1, T + 1):
    stack = []

    for ch in input().strip():
        if stack and (stack[-1] == ch):
            stack.pop()
        else:
            stack.append(ch)

    print(f'#{tc} {len(stack)}')