x = int(input())
y = int(input())

# 방1
if x > 0 :
    if y > 0 : 
        print(1)
    else :
        print(4)
else :
    if y > 0 : 
        print(2)
    else :
        print(3)

# 방2
print({(True, True): 1, (False, True): 2, (False, False): 3, (True, False): 4}[(x > 0, y > 0)])
