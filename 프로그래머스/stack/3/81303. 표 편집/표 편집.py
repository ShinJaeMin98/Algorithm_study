def solution(n, k, cmd):
    # 삭제된 행 저장
    deleted = []
    
    # 각 행의 위, 아래를 인덱스로 표현
    # 맨 앞과 맨 끝에 가상 공간을 확보하여 생성
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 2)]
    
    # 현재 위치를 나타내는 인덱스 (up, down에서 움직일)
    # 가상 공간에 의해 초기 위치에 1을 더해줘야 함
    k += 1
    
    for cmd_i in cmd:
        if cmd_i.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if down[k] > n else down[k]
            
        elif cmd_i.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
            
        else:
            act, num = cmd_i.split()
            if act == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
                    
    ans = ["O"] * n
    for i in deleted:
        ans[i - 1] = "X"
    return "".join(ans)
