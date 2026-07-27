T = int(input())

for tc in range(1, T + 1):
    stack = []

    for token in input().split():

        if token.isdigit():
            stack.append(int(token))

        elif token in ['+', '-', '*', '/']:

            if len(stack) < 2:
                print(f'#{tc} error')
                break

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(a // b)

        elif token == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc} error')
            break