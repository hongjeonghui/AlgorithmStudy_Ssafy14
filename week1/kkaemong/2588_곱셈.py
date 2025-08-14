a = list(map(int, input()))
b = list(map(int, input()))
c = b[-1]
d = b[-2]
e = b[0]

a_num = int(''.join(map(str, a)))    # join 함수 지피티한테 물어봄 ㅋ
b_num = int(''.join(map(str, b)))



print(a_num * c)
print(a_num * d)
print(a_num * e)
print(a_num * b_num)
