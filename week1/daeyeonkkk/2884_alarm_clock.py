H, M = map(int, input().split())
Time = (H * 60) + M

if Time < 45:
    Time += (24 * 60)
print(f'{(Time - 45) // 60}  {(Time - 45) % 60}')
