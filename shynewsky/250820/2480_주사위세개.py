arr = list(map(int, input().split())) # [3, 3, 6]

if arr[0] == arr[1] == arr[2] : # 같은 눈 3개
    print(10000 + (arr[0] * 1000))

elif arr[0] == arr[1] != arr[2] : # 같은 눈 2개
    print(1000 + (arr[0] * 100))
elif arr[1] == arr[2] != arr[0] : # 같은 눈 2개
    print(1000 + (arr[1] * 100))
elif arr[2] == arr[0] != arr[1] : # 같은 눈 2개
    print(1000 + (arr[2] * 100))

elif arr[0] != arr[1] != arr[2] : # 다른 눈 2개
    print(max(arr) * 100)
