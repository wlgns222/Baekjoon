import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

max_pos = 100000
dist = [0] * (max_pos + 1)
dist[n] = 1

queue = deque([n])
while queue :
  curr = queue.popleft()

  if curr == m : 
    print(dist[m]-1)
    break
  
  for next in [curr-1, curr+1, curr*2] :
    if 0 <= next <= max_pos:
      if dist[next] == 0:
        dist[next] = dist[curr] + 1
        queue.append(next)    