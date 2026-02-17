import sys

k, n = map(int, sys.stdin.readline().split())
lans = []

for _ in range(k) :
  lans.append(int(sys.stdin.readline()))

start = 1
end = max(lans)
ans = 0

while start <= end :
  mid = (start + end) // 2
  result = 0
  for lan in lans :
    result += lan // mid
  if result >= n :
    ans = mid
    start = mid + 1
  else :
    end = mid - 1

print(ans)