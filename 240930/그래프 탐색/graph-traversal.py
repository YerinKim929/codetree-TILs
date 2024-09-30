import sys

def dfs(v, num_nodes):
    for cur_v in range(N):
        if graph[v][cur_v] and not visited[cur_v]:
            num_nodes += 1
            visited[cur_v] = True
            return dfs(cur_v, num_nodes)

    return num_nodes

N, M = map(int, sys.stdin.readline().split())

graph = [[0]*N for _ in range(N)]
visited = [False]*N

for m in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

visited[0] = True
num_nodes = dfs(0, 0)

print(num_nodes)