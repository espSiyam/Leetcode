nums = [2,5,1,3,4,7]
n = 3
sol = []
for i,j in zip(nums[:n],nums[n:]):
    sol += [i,j]
    # sol.append(i)
    # sol.append(j)
# for i in range(int((len(nums))/2)):
#     fir = nums[i]
#     sec = nums[i+n]
#     sol.append(fir)
#     sol.append(sec)
print(sol)