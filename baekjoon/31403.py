nums = []
for _ in range(3):
    nums.append(int(input()))

print(nums[0] + nums[1] - nums[2])
temp = int(str(nums[0])+str(nums[1]))
print(temp-nums[2])