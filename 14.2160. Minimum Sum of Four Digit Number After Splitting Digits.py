num = 2932

# Intitution:
"""
The idea is that first we have to convert this number to digits and sort them. Ideally the
smallest number can be found from 2 digits and 2 digits as 3 digit is huge.

Suppose, we want to form a small number of 2 digits from 2 digits. The fist digit must be the smallest.
So for this number, after sorting, we kept the first 2 number as first number for num1 and num2.

link: https://www.youtube.com/watch?v=9dP_mSJ3Djw&ab_channel=BroCoders
"""

# Strategy 1:
sorted_num_list = sorted(list(str(num)))

num1 = sorted_num_list[0] + sorted_num_list[2]
num2 = sorted_num_list[1] + sorted_num_list[3]

sum = int(num1) + int(num2)

print(sorted_num_list)
print(sum)

# Strategy 2:
data_list = []

while num>0:
    data = int(num % 10)
    data_list.append(data)
    num = int(num / 10 )

sorted_num_list = sorted(data_list)

num1 = sorted_num_list[0]*10 + sorted_num_list[2]
num2 = sorted_num_list[1]*10 + sorted_num_list[3]

sum = int(num1) + int(num2)

print(sorted_num_list)
print(sum)