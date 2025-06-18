from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for key in graph:
        graph[key].sort(reverse=True)  # 사전순을 위해 reverse

    route = []
    def dfs(airport):
        while graph[airport]:
            next = graph[airport].pop()
            dfs(next)
        route.append(airport)

    dfs("ICN")
    return route[::-1]
        

if __name__ == '__main__':
    cases = [
        [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    ]

    for case in cases:
        output = solution(case)
        print(output)