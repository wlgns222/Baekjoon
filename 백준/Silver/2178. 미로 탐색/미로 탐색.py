import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maze = []
for _ in range(n) :
  maze.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0, 0)])

while queue :
  x, y = queue.popleft()

  if x == (n-1) and y == (m-1) :
    print(maze[x][y])
    break
  
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < n) and (0 <= ny < m) :
      if maze[nx][ny] == 1 and (nx != 0 or ny != 0) :
        maze[nx][ny] = maze[x][y] +1
        queue.append([nx, ny])