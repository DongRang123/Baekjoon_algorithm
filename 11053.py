N = int(input())

matrix = list(map(int,input().split()))

dp = [0]*len(matrix)

dp[0] = 1
for i in range(1,N):
    max1 = 0
    for z in range(i):
        if matrix[i] > matrix[z]:
            max1 = max(max1,dp[z])

    dp[i] = max1+1

print(max(dp))