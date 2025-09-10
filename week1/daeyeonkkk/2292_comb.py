N = int(input())

if N == 1:
    print(1)

else:
    count = 1
    floor_max = 1

    while N > floor_max:
        floor_max += 6 * count
        count += 1

    print(count)
