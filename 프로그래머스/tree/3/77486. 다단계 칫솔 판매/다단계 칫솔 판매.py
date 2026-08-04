def solution(enroll, referral, seller, amount):
    
    # enroll별로 초기값을 0으로 설정 
    answer = {name:0 for name in enroll}
    
    # enroll별로 연결된 부모가 누구인지 
    connected = {name:conn for name, conn in zip(enroll, referral)}
    
    # seller별 amount를 순회하며 answer['sell']에 10% 제외(cost_1)하고 저장 (sell -> connected['sell'])
    # 만약 connected['sell']이 "-"가 아닐때까지 cost_1에 10%를 제외(cost_2)하고 저장
    
    for sell, am in zip(seller, amount):
        am *= 100
        while am > 0 and connected[sell] != '-':
            dis_amount = am // 10
            answer[sell] += am - dis_amount
            
            am = dis_amount
            sell = connected[sell]
            
        answer[sell] += am - (am // 10)
        
    
    
    return list(answer.values())