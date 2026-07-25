T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_cnt= [0]*10
    
    # idx를 카드 번호로 사용
    for num in input():
        num_cnt[int(num)] += 1

    # 가장 많은 카드 장 수 세기
    max_cnt = 0
    for cnt in num_cnt:
        if cnt > max_cnt:
            max_cnt = cnt

    # 가장 많은 카드 숫자 중 가장 큰 것 (idx를 차례대로 순회하기 때문에 가장 큰 것으로 결정됨)
    max_num = 0
    for i in range(10):
        if num_cnt[i] == max_cnt:
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')