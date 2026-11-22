def to_postfix(expression):
    priority = {'+': 1, '*': 2}
    operators = []
    postfix = []

    for token in expression:
        if token.isdigit():
            # 숫자는 후위 표기식에 바로 추가
            postfix.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            # 여는 괄호까지 연산자를 꺼내고 괄호는 제거
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()
        else:
            # 우선순위가 높거나 같은 연산자부터 처리
            while (
                operators
                and operators[-1] != '('
                and priority[operators[-1]] >= priority[token]
            ):
                postfix.append(operators.pop())
            operators.append(token)

    while operators:
        postfix.append(operators.pop())

    return postfix


def calculate(postfix):
    numbers = []

    for token in postfix:
        if token.isdigit():
            numbers.append(int(token))
        else:
            # 나중에 넣은 숫자가 오른쪽 피연산자
            right = numbers.pop()
            left = numbers.pop()

            if token == '+':
                numbers.append(left + right)
            else:
                numbers.append(left * right)

    return numbers.pop()

for tc in range(1, 11):
    length = int(input())
    expression = input().strip()

    postfix = to_postfix(expression)
    print(f"#{tc} {calculate(postfix)}")