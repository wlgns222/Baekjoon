import sys

exp = sys.stdin.readline().strip()
parts = exp.split('-')

result = []

for p in parts:
  val = sum(map(int, p.split('+')))
  result.append(val)

final_answer = result[0]
for i in range(1, len(result)):
  final_answer -= result[i]

print(final_answer)
