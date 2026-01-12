# 수의 개수
n = int(input())
# 수열
nums = list(map(int, input().split()))
# 연산자 개수 (+, -, *, / 순서)
ops = list(map(int, input().split()))

# 최댓값, 최솟값 초기화 (문제 범위에 맞춰서)
max_val = -1e9
min_val = 1e9

def dfs(depth, total, plus, minus, multi, divide):
  global max_val, min_val # 함수 밖 변수 수정하기 가능

  if depth == n: #함수 밖 변수를 읽어오기 가능
    max_val=max(total, max_val)
    min_val=min(total, min_val)

    return

  if plus > 0:
    dfs(depth+1, total+nums[depth], plus-1, minus, multi, divide)
  if minus > 0:
    dfs(depth+1, total-nums[depth], plus, minus-1, multi, divide)
  if multi > 0:
    dfs(depth+1, total*nums[depth], plus, minus, multi-1, divide)
  if divide > 0:
    dfs(depth+1, int(total/nums[depth]), plus, minus, multi, divide-1)

result = dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(max_val, min_val)