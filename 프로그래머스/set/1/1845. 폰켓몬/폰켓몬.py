def solution(nums):
    
    # 중복제거 후 숫자 확인
    mons = set(nums)
    
    # nums/2와 종류 최대값 중 min값 출력
    return min(len(mons), len(nums)/2)