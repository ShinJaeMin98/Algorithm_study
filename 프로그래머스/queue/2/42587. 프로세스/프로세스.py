from collections import deque

def solution(priorities, location):
    # (우선순위, 원래 위치) 형태로 큐 생성
    queue = deque(
        (priority, idx)
        for idx, priority in enumerate(priorities)
    )

    answer = 0

    while queue:
        priority, idx = queue.popleft()
        
        # 현재 프로세스보다 우선순위가 높은 프로세스가 있는 경우
        if queue and priority < max(p for p, _ in queue):
            queue.append((priority, idx))
            
        # 현재 프로세스를 실행하는 경우
        else:
            answer += 1
            
            # 내가 찾던 프로세스라면 실행 순서 반환
            if idx == location:
                return answer