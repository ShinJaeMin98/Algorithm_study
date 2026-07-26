T = int(input())
for tc in range(1, T+1):
    check = input()
    list = input()
    ans = 0

    for i in range(len(list) - len(check) + 1):
        if list[i:i+len(check)] == check:
            ans = 1
            break
    print(f'#{tc} {ans}')
