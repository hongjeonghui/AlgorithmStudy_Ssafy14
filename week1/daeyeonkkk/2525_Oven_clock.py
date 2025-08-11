A, B = map(int, input().split())
C = int(input())

H = (A + ((B + C)//60)) % 24
M = (B + C) % 60

print(f'{H} {M}')
