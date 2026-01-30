import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))

dq = deque([i for i in range(1, n + 1)])

total_moves = 0

for target in targets:
    target_idx = dq.index(target)
    mid_idx = len(dq) / 2 

    if target_idx <= mid_idx:
        while dq[0] != target:
            dq.rotate(-1)
            total_moves += 1
    else:
        while dq[0] != target:
            dq.rotate(1)
            total_moves += 1
    dq.popleft()

print(total_moves)