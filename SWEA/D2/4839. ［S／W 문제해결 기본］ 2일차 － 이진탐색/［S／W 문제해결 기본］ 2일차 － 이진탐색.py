# 이진탐색 함수
def binary_search(P, target):
    l = 1
    r = P
    cnt = 0

    while True:
        C = int((l+r)/2)
        cnt += 1
        
        if target > C:
            l = C
        elif target < C:
            r = C
        else:
            return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    cnt_a = binary_search(P, Pa)
    cnt_b = binary_search(P, Pb)

    if cnt_a > cnt_b:
        print(f'#{tc} B')
    elif cnt_b > cnt_a:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
            