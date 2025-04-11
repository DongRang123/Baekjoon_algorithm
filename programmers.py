def solution(tickets):
    from collections import defaultdict
    
    routes = defaultdict(list)
    
    # 목적지를 알파벳 역순으로 정렬하여 stack처럼 pop() 하도록 설정
    for a, b in sorted(tickets, reverse=True):
        routes[a].append(b)
    
    path = []
    
    def dfs(airport):
        while routes[airport]:
            dfs(routes[airport].pop())
        path.append(airport)
    
    dfs("ICN")
    return path[::-1]