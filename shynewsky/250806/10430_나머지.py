a, b, c = map(int, input().split()) # 변수명 A, B, C 쓰기
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A×B)%C)            # 곱셈은 × 가 아니라 *
print(((A%C) × (B%C))%C)  # 곱셈은 × 가 아니라 *
