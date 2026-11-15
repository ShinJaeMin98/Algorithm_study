T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]

num = 1234567891

# 가장 큰 N까지 팩토리얼 전처리
max_n = max(n for n, r in cases)
factorial = [1] * (max_n + 1)

for i in range(1, max_n + 1):
    factorial[i] = factorial[i - 1] * i % num

for tc, (n, r) in enumerate(cases, start=1):
    # 조합 공식의 분모 : R! × (N-R)!
    denominator = factorial[r] * factorial[n - r] % num
    # 페르마의 소정리로 분모의 모듈러 역원 계산
    inverse = pow(denominator, num - 2, num)
    # N!에 분모의 역원을 곱해 조합 계산
    answer = factorial[n] * inverse % num

    print(f"#{tc} {answer}")