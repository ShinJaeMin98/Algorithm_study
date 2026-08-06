for tc in range(1, 11):
    N, nums = input().split()
    stack = []
    for n in nums:
        if stack and stack[-1] == n:
            stack.pop()
        else:
            stack.append(n)
    print(f'#{tc} {"".join(stack)}')
