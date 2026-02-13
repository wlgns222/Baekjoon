import sys

n = int(sys.stdin.readline())
m = int (sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (n+1)
count = 0

def dfs(curr) :
  global count
  visited[curr] = True
  for nextNode in graph[curr] :
    if not visited[nextNode] :
      count += 1
      dfs(nextNode)

dfs(1)
print(count)