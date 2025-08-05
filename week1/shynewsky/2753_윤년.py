y = int(input())

# 윤년 계산식 (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
    print(1)
else :
    print(0)
