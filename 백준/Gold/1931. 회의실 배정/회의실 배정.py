import sys

n = int(sys.stdin.readline())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# 종료 시간을 기준으로 먼저 정렬하고, 같다면 시작 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
time = 0

for start, end in meetings :
  if start >= time:
    count += 1
    time = end

print(count)