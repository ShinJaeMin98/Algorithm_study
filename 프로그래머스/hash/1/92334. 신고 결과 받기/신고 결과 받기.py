from collections import defaultdict

def solution(id_list, report, k):
    
    # 중복 신고를 처음부터 제거하기 위해 set으로 변환
    report = set(report)
    # 신고자 (id_list를 기준으로 value는 set으로 지정)
    reporter = {user: set() for user in id_list}
    # 신고당한 자 (id_list를 기준으로 value는 기본값 0)
    suspect_count = {user: 0 for user in id_list}
    # 메일 받은 횟수
    answer = []
    
    # report를 신고자와 대상으로 나눠 reporter에 저장 및 suspect에 카운트
    for r in report:
        rep, sus = r.split()
        reporter[rep].add(sus)
        suspect_count[sus] += 1       
            
    # id_list별로 신고한 대상을 순회하며 신고당한 횟수가 k 이상인지 확인하고,
    # 충족하는 만큼 카운트해서 answer에 저장
    for user in id_list:
        user_reported = reporter[user]
        
        count = sum(1 for sus in user_reported if suspect_count[sus] >= k)
        answer.append(count)
    
    return answer