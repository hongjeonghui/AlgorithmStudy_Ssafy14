A, B = map(int, input().split()) # 현재 시각
C = int(input()) # 필요한 시간

A += (B+C) // 60
B = (B+C) % 60

A %= 24

print(A, B)
