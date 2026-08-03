import math
def solution(n,a,b):
    ans = 0
    # 값을 올림하여 계산
    while a != b:
        a, b = math.ceil(a/2), math.ceil(b/2)
        ans += 1
        
    return ans