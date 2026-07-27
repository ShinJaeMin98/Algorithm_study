T = int(input())
for tc in range(1, T+1):
    stack = []
    for alp in input():
        if stack and stack[-1] == alp:
            stack.pop()
        else:
            stack.append(alp)
            
    print(f'#{tc} {len(stack)}')