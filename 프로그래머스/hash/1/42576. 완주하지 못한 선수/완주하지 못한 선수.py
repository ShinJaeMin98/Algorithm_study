def solution(participant, completion):
    dic = dict()
    
    # 이름을 key로 1씩 입력
    for part in participant:
        if part in dic:
            dic[part] += 1
        else:
            dic[part] = 1
            
    # completion을 돌면서 -1
    for com in completion:
        dic[com] -= 1
        
    # 이름에 해당하는 key의 value가 0이 아닌경우 return
    for key in dic.keys():
        if dic[key] > 0:
            return key
    