import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
ans = 0

while start <= end :
  mid = (start+end) // 2
  result = 0
  for tree in trees :
    if tree > mid :
      result += tree - mid
  if result >= m :
    ans = mid
    start = mid + 1
  else :
    end = mid - 1

print(ans)