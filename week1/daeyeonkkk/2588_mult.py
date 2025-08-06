A = int(input())
B = input()

C = A * int(B[-1])
D = A * int(B[-2])
E = A * int(B[-3])
F = C + (D * 10) + (E * 100)

print(C)
print(D)
print(E)
print(F)