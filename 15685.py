direction = {
    1: 2,
    0: 1,
    2:3,
    3:0
}

def dragon (x,y,d,g):
    result = [(x,y)]
    if d == 0:
        end = (x+1,y)
    elif d == 1:
        end = (x,y-1)
    elif d == 2:
        end = (x-1,y)
    elif d == 3:
        end = (x,y+1)
    result.append(end)
    dir = [d]
    for i in range(g):
        new_dir = dir[:]
        for i in dir[::-1]:
            end = result[-1]
            news = direction[i]
            new_dir.append(news)
            if news == 0:
                result.append((end[0]+1,end[1]))
            if news == 1:
                result.append((end[0],end[1]-1))
            if news == 2:
                result.append((end[0]-1,end[1]))
            if news == 3:
                result.append((end[0],end[1]+1))

        dir = new_dir[:]
    return result

N = int(input())
answer = set()
for j in range(N):
    x,y,d,g = map(int,input().split())
    for jj in dragon(x,y,d,g):

        answer.update([jj])
cnt = 0

for i in range(100):
    for j in range(100):
        if (i,j) in answer:
            if (i+1,j) in answer:
                if (i,j+1) in answer:
                    if (i+1,j+1) in answer:
                        cnt += 1
print(cnt)
