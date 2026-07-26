from collections import Counter

T = int(input())
for tc in range(1, T+1):
    check = set(input())
    list_cnt = Counter(input())
    ans = 0

    for ch in check:
        ans = max(ans, list_cnt[ch])

    print(f'#{tc} {ans}')