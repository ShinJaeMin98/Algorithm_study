def solution(board, moves):
    board_len = len(board[0])
    stacks = [[] for _ in range(board_len)]
    busket = []
    cnt = 0
    
    # board 역순회
    for row in reversed(board):
        # 0이 아닌 doll이면 각 stack에 쌓음
        for j, doll in enumerate(row):
            if doll != 0:
                stacks[j].append(doll)
                
    # moves 순회하며 작업 진행
    for i in moves:
        if stacks[i-1]:
            doll = stacks[i-1].pop()
            
            if busket and busket[-1] == doll:
                busket.pop()
                cnt += 2
            else:
                busket.append(doll)
    return cnt