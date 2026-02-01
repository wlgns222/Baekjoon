import sys
import heapq

n = int(sys.stdin.readline())

max_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if not max_heap:
            print(0)
        else:
            result = heapq.heappop(max_heap) * -1
            print(result)
    else:
      heapq.heappush(max_heap, -x)