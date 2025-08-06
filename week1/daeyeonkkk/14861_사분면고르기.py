loc_x = int(input())
loc_y = int(input())
if loc_x * loc_y > 0:
    if loc_x > 0:
        print(1)
    else:
        print(3)
else:
    if loc_x > 0:
        print(4)
    else:
        print(2)