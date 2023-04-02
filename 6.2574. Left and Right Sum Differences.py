nums = [10,4,8,3]
sol = []
for i in range(len(nums)):
    pre = sum(nums[:i])
    post = sum(nums[i+1:])
    sol.append(abs(pre-post))

print(sol)