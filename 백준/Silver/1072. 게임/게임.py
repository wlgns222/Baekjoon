import sys

x, y = map(int, sys.stdin.readline().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    start = 1
    end = 1000000000
    ans = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        new_x = x + mid
        new_y = y + mid
        new_z = (new_y * 100) // new_x
        
        if new_z > z:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    print(ans)