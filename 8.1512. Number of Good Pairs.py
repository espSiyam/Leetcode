nums = [1,1,1,1]
# output = 0
# dict_number = dict()

# for n in nums:
#     if n in dict_number:
#         output = output + dict_number[n]
#         dict_number[n] = dict_number[n] + 1
        
#     else:
#         dict_number[n] = 1
# print(output)
ans = 0
test = {1:3, 2:1, 3:2}
for num in test:
    val = test[num]
    print(num, val)
    for i in range(val):
        print("range",i)
        print("ans",ans)
        ans += i
        
    

print("Final:",ans)