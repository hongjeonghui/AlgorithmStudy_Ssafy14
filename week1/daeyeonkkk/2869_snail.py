A, B, V = map(int, input().split())

# night = 1
#
# height = A
#
# gain = A-B
#
# day = (V-A)//gain
#
# while V > height:
#     night += 1
#     height += gain
#
# print(night + day)

if A == V:
    day = 1
else:
    gain = A - B
    goal = V - A
    if goal % gain == 0:
        day = (goal//gain) + 1
    else:
        day = (goal//gain) + 2

print(day)
