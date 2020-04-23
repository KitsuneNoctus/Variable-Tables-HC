'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
-
Restating: given a number, return the the difference between the product and sum of its individual didgits
-


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
'''
# convert number passed in as string, go through and add individual characters as ints to a list
# run through list and add numbers togther to get sum
# run through list again and multiply each number by its last
# return the product - sum
def subtractProductAndSum(n):
        
        digits = [int(num) for num in str(n)]
        aProduct = 0
        aSum = 0
        for i in digits:
            aSum += i
            if i != 0 and aProduct == 0:
                aProduct += i
            else:
                aProduct = aProduct * i

        result = aProduct - aSum
        print(f"{n} | Result = {aProduct} - {aSum} = {result}")
        return result

subtractProductAndSum(234)
subtractProductAndSum(4421)
