def reg(n, m):
    if m == 1:
        return n
    return n * reg(n, m-1)

for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    ans = reg(n, m)
    print(f'#{tc} {ans}')