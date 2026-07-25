T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = map(int, input().split())
    max_num = 0
    min_num = 1000000
    
    # 숫자 하나씩 확인
    for num in nums:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    print(f'#{tc} {max_num - min_num}')