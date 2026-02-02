import sys
import heapq

n = int(sys.stdin.readline())

abs_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0 :
      heapq.heappush(abs_heap, (abs(x), x))
    else :
      if not abs_heap :
        print(0)
      else :
        result = heapq.heappop(abs_heap)
        print(result[1])