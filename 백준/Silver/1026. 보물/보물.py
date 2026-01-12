n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
a.sort()

for x in a:
    target = max(b)
    s += x * target

    b.remove(target)

print(s)