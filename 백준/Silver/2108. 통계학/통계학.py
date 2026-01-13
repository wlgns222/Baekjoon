import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

n = int(input())

# 1. 빈도를 저장할 배열 (범위: -4000 ~ 4000 이므로 총 8001개)
counts = [0] * 8001
total_sum = 0
max_val = -4001
min_val = 4001

for _ in range(n):
    num = int(input())
    counts[num + 4000] += 1  # 인덱스 변환 후 빈도 증가
    total_sum += num
    if num > max_val: max_val = num
    if num < min_val: min_val = num

# --- 1. 산술평균 ---
# Python의 round()는 .5에서 짝수 쪽으로 가므로 직접 구현하는 것이 안전할 수 있음
mean = round(total_sum / n)
print(mean)

# --- 통계 계산을 위한 준비 ---
sorted_list = []  # 정렬된 결과를 담을 리스트
max_freq = 0      # 최빈값을 찾기 위한 최대 빈도수
for i in range(8001):
    if counts[i] > 0:
        # 정렬된 리스트 복원
        for _ in range(counts[i]):
            sorted_list.append(i - 4000)
        
        # 최빈값 후보를 위해 최대 빈도수 확인
        if counts[i] > max_freq:
            max_freq = counts[i]

# --- 2. 중앙값 ---
# 이미 sorted_list가 순서대로 채워졌으므로 중앙 인덱스 접근
print(sorted_list[n // 2])

# --- 3. 최빈값 ---
modes = []
for i in range(8001):
    if counts[i] == max_freq:
        modes.append(i - 4000)

# 최빈값이 여러 개면 두 번째로 작은 값 출력
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

# --- 4. 범위 ---
print(max_val - min_val)