nums = [3,1,2,10,1]

for i in range(1,len(nums)):
    # print(i)
    nums[i] = nums[i-1] + nums[i]

print(nums)