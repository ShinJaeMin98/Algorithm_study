T = int(input())
for tc in range(1, T + 1):
    words = input()
    ans = 0
    for i in range(1, 11):
        if words[:i] == words[i : 2*i]:
            ans = i
            break
            
    print(f'#{tc} {ans}')
