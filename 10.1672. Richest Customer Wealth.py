accounts = [[2,8,7],[7,1,3],[1,9,5]]

# result = {}

# for i in range(len(accounts)):
#     result[i] = sum(accounts[i])

# print((result))
# print(max(result.values()))


# val = 0

# for i in range(len(accounts)):
#     result = sum(accounts[i])

#     if result > val:
#         val = result

# print((val))

print(max(map(sum, accounts)))