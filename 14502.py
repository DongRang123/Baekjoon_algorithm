from collections import deque

N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(matrix_a):
    #2를 찾아라
    matrix_a_copy = [arr[:] for arr in matrix_a]
    two = deque()
    for i in range(N):
        for j in range(M):
            if matrix_a_copy[i][j] == 2:
                two.append((i,j))

    while two:
        ab = two.popleft()
        for i in range(4):
            nx = ab[0] + dx[i]
            ny = ab[1] + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if matrix_a_copy[nx][ny] == 0:
                    matrix_a_copy[nx][ny] = 2
                    two.append((nx,ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix_a_copy[i][j] == 0:
                cnt += 1

    return cnt

def dfs(idx,list_a,prev):
    global result

    if idx == 3:
        matrix_copy =[row[:] for row in matrix]
        for abc in list_a:
            matrix_copy[abc[0]][abc[1]] = 1
        soo = bfs(matrix_copy)
        result = max(result,soo)

        return

    for i in range(prev+1,N*M):
        if matrix[i//M][i%M] == 0:
            dfs(idx+1,list_a + [[int(i//M),int(i%M)]],i)


result = 0
dfs(0,[],-1)

print(result)