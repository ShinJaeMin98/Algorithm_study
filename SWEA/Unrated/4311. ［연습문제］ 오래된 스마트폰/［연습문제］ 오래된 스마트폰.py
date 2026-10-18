import heapq

def solve(digits, operators, M, W):
    INF = float('inf')

    # 직접 입력 가능한 숫자와 필요한 터치 횟수
    direct = []

    for number in range(1000):
        text = str(number)

        if all(ch in digits for ch in text):
            direct.append((number, len(text)))

            # 직접 입력은 최대 3회, 연산은 최소 4회 필요
            if number == W:
                return len(text)

    # dist[number]: 마지막 '='를 제외한 최소 터치 횟수
    dist = [INF] * 1000
    pq = []

    for number, touches in direct:
        dist[number] = touches
        heapq.heappush(pq, (touches, number))

    while pq:
        touches, number = heapq.heappop(pq)

        if touches > dist[number]:
            continue

        # W는 직접 입력 불가능하므로 '=' 터치 1회 추가
        if number == W:
            return touches + 1

        for operand, operand_touches in direct:
            # 연산자 1회 + 피연산자 입력 횟수
            new_touches = touches + 1 + operand_touches

            # 마지막 '='를 누를 횟수까지 확보
            if new_touches + 1 > M:
                continue

            for op in operators:
                if op == 1:
                    result = number + operand

                elif op == 2:
                    result = number - operand

                elif op == 3:
                    result = number * operand

                else:
                    if operand == 0:
                        continue
                    result = number // operand

                if not (0 <= result <= 999):
                    continue

                if new_touches < dist[result]:
                    dist[result] = new_touches
                    heapq.heappush(pq, (new_touches, result))

    return -1


T = int(input())

for tc in range(1, T + 1):
    N, O, M = map(int, input().split())
    digits = set(input().split())
    operators = list(map(int, input().split()))
    W = int(input())

    answer = solve(digits, operators, M, W)
    print(f"#{tc} {answer}")