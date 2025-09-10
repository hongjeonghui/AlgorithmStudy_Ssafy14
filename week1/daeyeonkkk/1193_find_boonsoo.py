X = int(input())

stacked_num = 0
floor = 0
while stacked_num < X:
    floor += 1
    stacked_num += floor

if floor % 2 == 0:
    print(f'{floor - (stacked_num - X)}/{stacked_num-X+1}')

else:
    print(f'{stacked_num-X+1}/{floor-(stacked_num-X)}')
