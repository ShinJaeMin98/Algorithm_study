from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # course의 숫자만큼 combinations(조합) 진행
    for c in course:
        
        # 각 갯수 별 menu
        menu = []
        
        # orders를 순회하며 조합 진행
        for order in orders:
            # order을 정렬해줘야 순서가 변경되는 것을 막을 수 있음
            comb = combinations(sorted(order), c) 
            menu.extend(comb)
        
        # menu에서 동일한 메뉴 count
        counter = Counter(menu)
        
        # 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합만 포함
        if counter and max(counter.values()) > 1:
            for me, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(me))
                    
    return sorted(answer)