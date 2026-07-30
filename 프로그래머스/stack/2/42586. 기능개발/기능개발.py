import math

def solution(progresses, speeds):
    ans = []
    n = len(progresses)
    
    # 각 작업의 배포 가능일 (남은 일수에 속도를 나눈 후 올림하여 계산)
    day_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]
    
    # 앞서 배포되어야 하는 배포 기준일을 첫 날로 설정
    std_day = day_left[0]
    
    cnt = 0
    for i in range(n):
        # 배포 기준일 보다 빠르거나 같다면
        if day_left[i] <= std_day:
            cnt += 1 # 같이 배포하기 위해 cnt 누적
            
        # 배포 기준일 보다 느리다면
        else:
            ans.append(cnt) # 기존에 누적된 cnt 저장
            std_day = day_left[i] # 새로운 배포 기준일 지정
            cnt = 1 # cnt 초기화
    
    # 마지막으로 카운트된 작업들 저장
    ans.append(cnt)
    
    return ans