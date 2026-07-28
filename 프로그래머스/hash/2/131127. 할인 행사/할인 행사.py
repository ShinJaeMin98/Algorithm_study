def solution(want, number, discount):
    # 원하는 제품을 key, 수량을 value로 저장
    wants = {}
    for i in range(len(want)):
        wants[want[i]] = number[i]
        
    ans = 0
        
    # discount를 첫번째부터 10개씩 순회하며 마찬가지로 제품을 key로 수량을 더해줌
    for i in range(len(discount) - 9):
        discount_10cycle = {}
        for j in range(i, i+10):
            if discount[j] in wants:
                discount_10cycle[discount[j]] = discount_10cycle.get(discount[j], 0) + 1
           
        # 10개를 돌았을 때 원하는 제품과 동일하면 ans + 1 
        if discount_10cycle == wants:
            ans += 1
    return ans
        
             