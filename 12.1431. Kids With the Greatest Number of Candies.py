candies = [4,2,1,1,2]
extraCandies = 1

high = max(candies)
for i in range(len(candies)):
    total = candies[i] + extraCandies
    if  total >= high:
        print(total, max(candies))
        candies[i] = True
    else:
        candies[i] = False
print(candies)