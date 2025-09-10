N = int(input())
floor = 1
floor_max = 1

# 다음 층 끝범위 = 현재층 끝범위 + 6 * (현재층수-1)
# 현재 층수를 갱신하기 전에, 다음 층 끝범위를 구하고, 다음 층으로 갱신한다
while floor_max < N: # 끝범위가 N보다 커질때까지 돌린다
    floor_max += 6 * floor  # 다음 층수의 최고 끝 범위를 구하고
    floor += 1              # 다음 층으로 이동한다

print(floor)
