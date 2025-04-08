N = int(input())

Time = [0]
Pay = [0]
for _ in range(N):
    T, P = map(int, input().split())
    Time.append(T)
    Pay.append(P)

dp = [0] * (N + 2)  # N+1일까지 접근 가능하게 설정

for i in range(1, N + 1):
    # i일까지 얻을 수 있는 최대 수익 유지
    dp[i] = max(dp[i], dp[i - 1])

    # i일부터 상담 시작 가능하면
    end_day = i + Time[i]
    if end_day <= N + 1:
        dp[end_day] = max(dp[end_day], dp[i] + Pay[i])

# 마지막 날까지 최대 수익
print(max(dp))
