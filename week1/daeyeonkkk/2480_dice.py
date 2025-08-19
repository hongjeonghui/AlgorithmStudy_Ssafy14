nums = list(map(int, input().split()))
prize = 0
if nums[0] == nums[1] == nums[2]:
    prize = nums[0] * 1000 + 10000

elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
    prize = max(nums) * 100

else:
    for i in range(3):
        if nums[i-1] - nums[i] == 0:
            prize = nums[i] * 100 + 1000
            break

print(prize)
