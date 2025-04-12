N, K = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(N)]

min_answer = float('inf')
visited = [False] * N

def dfs(depth, start, selected):
    global min_answer

    if depth == K:
        max_dist = 0
        # 각 집에 대해 가장 가까운 대피소 거리 측정
        for i in range(N):
            hx, hy = houses[i]
            min_dist = float('inf')
            for idx in selected:
                sx, sy = houses[idx]
                dist = abs(hx - sx) + abs(hy - sy)
                min_dist = min(min_dist, dist)
            max_dist = max(max_dist, min_dist)
        min_answer = min(min_answer, max_dist)
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1, selected + [i])
            visited[i] = False

dfs(0, 0, [])
print(min_answer)