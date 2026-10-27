T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    classes = list(map(int, input().split()))

    # 일주일 동안 수업이 열리는 횟수
    weekly_cnt = sum(classes)
    # 미리 건너뛸 수 있는 주 수
    weeks = (n - 1) // weekly_cnt
    # 건너뛴 주를 제외하고 남은 수업 횟수
    remaining = n - (weeks * weekly_cnt)

    answer = float("inf")
    
    # 수업이 있는 요일을 시작으로 하루씩 추가하며 남은 수업 횟수를 계산
    for start in range(7):
        if classes[start] == 0:
            continue

        days = 0	# 추가로 머문 날짜
        attended = 0	# 추가로 들은 수업 횟수
        day = start	# 현재 요일

        # 추가로 들은 수업 횟수가 남은 수업 횟수와 같아질 때까지
        while attended < remaining:
            days += 1	# 수업 있든 없든 추가
            if classes[day] == 1:
	            attended += 1
            # 다음 요일 이동
            day = (day + 1) % 7

        # 건너뛴 기간 + 남은 수업을 듣는데 걸린 기간
        total_days = weeks * 7 + days
        answer = min(answer, total_days)

    print(f"#{tc} {answer}")       