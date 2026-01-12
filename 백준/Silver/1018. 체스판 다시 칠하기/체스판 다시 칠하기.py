import sys

n, m = map(int, sys.stdin.readline().split())

# N줄만큼 문자열을 입력받아 리스트에 저장
# 예: ["WWBW...", "BBWW...", ...] 형태가 됨
board = [sys.stdin.readline().strip() for _ in range(n)]
count = 64

for i in range(n-7) :
  for j in range(m-7) :
    w = 0
    b = 0

    for x in range(i, i+8) :
      for y in range (j, j+8) :
        if((x+y)%2 == 0) :
          if board[x][y] != 'W' : w += 1
          if board[x][y] != 'B' : b += 1
        else :
          if board[x][y] != 'B' : w += 1
          if board[x][y] != 'W' : b += 1
    
    count = min(count, w, b)

print(count)
