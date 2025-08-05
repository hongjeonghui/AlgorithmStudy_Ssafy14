a = int(input())
b = input()           # 문자열로 받은 후에, 하나씩 분해해서 자리수로 사용
print(a * int(b[2]))  # 일의 자리수
print(a * int(b[1]))  # 십의 자리수
print(a * int(b[0]))  # 백의 자리수
print(a * int(b))
