import sys

s = sys.stdin.readline().strip()

n_length = len(s)

count = 0

for n in range(n_length - 1):
    if s[n] != s[n+1]:
        count += 1

print((count + 1) // 2)