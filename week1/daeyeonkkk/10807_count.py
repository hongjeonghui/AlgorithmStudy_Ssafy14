N = int(input())
nums = input().split()
target = input()
count = 0
for char in nums:
    if char == target:
        count += 1
print(count)
