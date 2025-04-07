import sys
sys.stdin = open('input.txt','r')

dx = [0,1,0,-1]
dy = [1,0,-1,0]
N = int(input())
K = int(input())
apple = []
for i in range(K):
    A,B = map(int,input().split())
    apple.append([A,B])

L = int(input())
move = []
for i in range(L):
    X,C = input().split()
    move.append((int(X),C))

snake = [[1,1]]
direction = 0
time = 0
i = 0
visited = []
while True:
    time += 1
    #머리 위치 이동:
    head = snake[-1]
    head = [head[0]+dx[direction],head[1]+dy[direction]]

    if head[0] < 1 or head[0] >= N+1 or head[1] < 1 or head[1]>=N+1:
        break

    if head in apple: #사과 있는지 화긴
        if head  not in visited: #사과 한번만 방문해야함
            snake.append(head)
            visited.append(head)
        else:
            snake.append(head)
            if head in snake[:len(snake) - 1]:
                break
            else:
                snake.pop(0)
    else:

        snake.append(head)

        if head in snake[:len(snake)-1]:
            break
        else:
            snake.pop(0)


    if i != L:
        if time >= move[i][0]:
            if move[i][1] == 'D':
                direction += 1
                if direction == 4:
                    direction = 0
            elif move[i][1] == 'L':
                direction -= 1
                if direction == -1:
                    direction = 3
            i += 1

print(time)
