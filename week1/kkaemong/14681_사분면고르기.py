a = int(input())
b = int(input())
if 0 < a and 0 < b:
    print(1)
elif 0 < a and b < 0:
    print(4)
elif a < 0 and b > 0:
    print(2)
else:
    print(3)
