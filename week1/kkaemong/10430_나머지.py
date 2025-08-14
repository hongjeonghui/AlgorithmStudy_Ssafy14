a = list(map(int, input().split()))

sum_a = (a[0] + a[1])% a[2]
sum_b = ((a[0] % a[2]) + (a[1] % a[2])) % a[2]
sum_c = (a[0] * a[1]) % a[2]
sum_d = ((a[0] % a[2] * a[1] % a[2])) % a[2]

print(sum_a)
print(sum_b)
print(sum_c)
print(sum_d)
