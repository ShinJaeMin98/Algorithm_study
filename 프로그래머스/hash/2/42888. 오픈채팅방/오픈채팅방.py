def solution(record):
    users_log = {}
    result_log = []

    for log in record:
        cmd = log.split()

        # Enter, Change인 경우 users_log에 id(key)랑 이름 저장 또는 변경
        if cmd[0] != 'Leave':
            users_log[cmd[1]] = cmd[2]

    for log in record:
        cmd = log.split()

        # EL에 따른 result_log 등록
        if cmd[0] == "Enter":
            result_log.append("%s님이 들어왔습니다." % users_log[cmd[1]])
        elif cmd[0] == "Change":
            pass
        else:
            result_log.append("%s님이 나갔습니다." % users_log[cmd[1]])

    return result_log
        
        