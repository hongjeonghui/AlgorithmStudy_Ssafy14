N = int(input())
floor = 1
floor_min = 1
floor_max = 1

# 다음층 시작범위 = 현재층 시작범위 + 현재층 층수
# 다음층 끝범위 = 현재층 끝범위 + 다음층수
while floor_max < N:
    floor_min += floor
    floor += 1
    floor_max += floor

# 짝수층이면 정순, 홀수층이면 역순
if floor%2 == 0:
    print(f'{N - floor_min + 1}/{floor - (N - floor_min)}')
elif floor%2 == 1:
    print(f'{floor - (N - floor_min)}/{N - floor_min + 1}')
