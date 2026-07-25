T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 최초 M개 더한 값
    nums_sum = sum(num for num in nums[:M+1])
    max_sum, min_sum = nums_sum, nums_sum
    
    for i in range(1, N - M + 1):
        nums_sum += (nums[i+(M-1)] - nums[i-1])
        if nums_sum > max_sum:
            max_sum = nums_sum
        elif nums_sum < min_sum:
            min_sum = nums_sum
    print(f'#{tc} {max_sum - min_sum}')