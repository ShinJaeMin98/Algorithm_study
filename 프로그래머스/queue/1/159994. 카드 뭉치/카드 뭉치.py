from collections import deque

def solution(cards1, cards2, goal):
    queue = deque
    
    # 큐로 만들어주기
    cards1 = queue(cards1)
    cards2 = queue(cards2)
    goal = queue(goal)
    
    # goal이 없어질때까지 순회
    while goal:
        # cards1이 있고, 첫번째 요소가 goal의 첫번째 요소인 경우
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft()
            goal.popleft()
        # cards2이 있고, 첫번째 요소가 goal의 첫번째 요소인 경우
        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft()
            goal.popleft()
        # 두 곳 모두에서 찾지 못한 경우
        else:
            break
    
    # goal이 빈 경우 Yes / 아니면 No
    return "Yes" if not goal else "No"