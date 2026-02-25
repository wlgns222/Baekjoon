import sys

n = int(sys.stdin.readline())
requests = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

if sum(requests) <= m :
  print(max(requests))
else :
  start = 0
  end = max(requests)
  ans = 0
  while start <= end :
    mid = (start + end) // 2
    result = 0
    for request in requests :
      if request > mid :
        result += mid
      else :
        result += request
    if result <= m :
      ans = mid
      start = mid + 1
    else :
      end = mid - 1

  print(ans)
