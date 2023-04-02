nums = [1,2,1]


# for i in range(len(nums)):
#     nums.append(nums[i])

# print(nums)

n = len(nums)
ans = []
for i in range(2*n):
    num = nums[i%n]
    ans.append(num)

print(ans)