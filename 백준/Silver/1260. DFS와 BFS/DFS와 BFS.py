import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

dfsVisit = [False] * (n+1)
bfsVisit = [False] * (n+1)

def dfs(v) :
  dfsVisit[v] = True
  print(v, end = ' ')
  
  for next in graph[v] :
    if not dfsVisit[next] :
      dfs(next)

def bfs(v) :
  queue = deque([v])
  bfsVisit[v] = True

  while queue :
    curr = queue.popleft()
    print(curr, end =' ')

    for next in graph[curr] :
      if not bfsVisit[next]:
        bfsVisit[next] = True
        queue.append(next)

dfs(v)
print()
bfs(v)