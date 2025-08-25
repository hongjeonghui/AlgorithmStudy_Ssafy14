N = int(input())
nums = map(int, input().split())
first_num = next(nums)
min_num = first_num
max_num = first_num
for num in nums:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num
print(f'{min_num} {max_num}')