T = int(input())
for tc in range(1, T+1):
    word = input()
    ans = 0
    if word[::-1] == word:
        ans = 1
    print(f'#{tc} {ans}')