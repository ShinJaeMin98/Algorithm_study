def solution(nums):
    answer = 0
    mons = {}
    for num in nums:
        mons[num] = mons.get(num, 0) + 1
        
    if len(nums)/2 >= len(mons):
        answer = len(mons)
    else:
        answer = len(nums)/2
    
    
    return answer