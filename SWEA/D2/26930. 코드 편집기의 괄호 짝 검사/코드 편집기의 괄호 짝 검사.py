T = int(input())

pairs = {
    ')': '(',
    '}': '{'
}

for tc in range(1, T + 1):
    stack = []
    ans = 1
    quotation = None

    for s in input():

        # 문자열 안
        if quotation is not None:
            if s == quotation:
                quotation = None
            continue

        # 문자열 시작
        if s in "\"'":
            quotation = s
            continue

        # 닫는 괄호
        if s in pairs:
            if not stack or stack[-1] != pairs[s]:
                ans = 0
                break
            stack.pop()

        # 여는 괄호
        elif s in "({":
            stack.append(s)

    if stack or quotation is not None:
        ans = 0

    print(f'#{tc} {ans}')