import sys

sys.setrecursionlimit(2000)

n = int(sys.stdin.readline())

house = []
for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().strip())))

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

result = []

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or house[x][y] == 0:
        return 0

    house[x][y] = 0
    count = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        count += dfs(nx, ny)

    return count

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            result.append(dfs(i, j))

result.sort()
print(len(result))
for m in result:
    print(m)