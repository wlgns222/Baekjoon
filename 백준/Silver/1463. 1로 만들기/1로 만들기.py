import sys

n = int(sys.stdin.readline())
toOne = [0] * (n+1)

for i in range(2, n+1) :
  toOne[i] = toOne[i-1] + 1
  if i % 2 == 0 :
    toOne[i] = min(toOne[i], toOne[i//2] + 1)
  if i % 3 == 0 :
    toOne[i] = min(toOne[i], toOne[i//3] + 1)

print(toOne[n])