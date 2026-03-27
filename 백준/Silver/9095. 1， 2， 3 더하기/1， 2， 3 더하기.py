import sys

total = [0] * 12
total[1] = 1
total[2] = 2
total[3] = 4

for i in range(4, 12) :
  total[i] = total[i-1] + total[i-2] + total[i-3]

T = int(sys.stdin.readline())

for _ in range(T) :
  n = int(sys.stdin.readline())
  print(total[n])