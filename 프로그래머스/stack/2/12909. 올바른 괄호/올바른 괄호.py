def solution(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return not stack

# 그냥 count로 계산
# def solution(s):
#     count = 0

#     for ch in s:
#         if ch == '(':
#             count += 1
#         else:
#             count -= 1

#         if count < 0:
#             return False

#     return count == 0