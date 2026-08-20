def solution(numbers, target):
    
    def dfs(index, total):

        # 모든 숫자를 사용했을때,
        # total이 target과 동일한 경우 True(1)
        if index == len(numbers):
            return total == target
        
        # + 연산
        plus = dfs(index + 1, total + numbers[index])
        
        # - 연산
        minus = dfs(index + 1, total - numbers[index])
        return plus + minus
        
    return dfs(0, 0)