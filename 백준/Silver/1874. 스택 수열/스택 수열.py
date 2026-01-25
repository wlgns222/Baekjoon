import sys

n = int(sys.stdin.readline())

# 수열을 만들기 위한 연산 기록 (+, -)
result = []
# 숫자를 쌓아둘 스택
stack = []
# 현재 스택에 넣어야 할 숫자 (1부터 시작)
curr = 1
# 수열 생성 가능 여부 플래그
is_possible = True

for _ in range(n):
    num = int(sys.stdin.readline())
    while curr <= num:
      stack.append(curr)
      result.append('+')
      curr += 1
    if stack and stack[-1] == num :
      stack.pop()
      result.append('-')
    else :
      is_possible = False
      break

if is_possible :
  for op in result:
    print(op)
else :
  print("NO")