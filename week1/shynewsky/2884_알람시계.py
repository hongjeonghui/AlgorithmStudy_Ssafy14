H, M = map(int, input().split())

# 방1
if M - 45 >= 0 :
    print(H, M-45)
else :
    if H -1 >= 0 :
        print(H-1, M+60-45)
    else :
        print(H+24-1, M+60-45)

# 방2
H = (H - 1) % 24 if M < 45 else H
M = (M - 45) % 60
print(H, M)
