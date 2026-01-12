n = int(input())
p = list(map(int, input().split()))

p.sort()
sum = 0
wait = 0

for x in p:
  wait += x
  sum += wait

print(sum)