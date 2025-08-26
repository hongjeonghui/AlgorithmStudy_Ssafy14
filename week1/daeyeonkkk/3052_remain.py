remain = set()
for _ in range(10):
    num = int(input())
    remain.add(num % 42)
print(len(remain))