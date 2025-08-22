end_test = 1
while end_test:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        end_test = 0
    else:
        print(A+B)
