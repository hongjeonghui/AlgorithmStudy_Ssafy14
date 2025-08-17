num = int(input())
pick_list = list(map(int, input().split()))
zol = []
for i in range(num):
    zol.insert(pick_list[i], i+1)
zol = zol[::-1]
print(*zol)
