# 백준 알람 시계

H, M = map(int, input().split())

if M < 45:
    if H < 1:
        H = H -1 + 24
    else:
        H = H-1
    M = M - 45 + 60
else:
    H = H
    M = M -45

print(H, M)
