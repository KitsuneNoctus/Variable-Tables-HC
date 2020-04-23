'''
Given an integer n, return any array containing n unique integers such that they add up to 0.


Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:

Input: n = 3
Output: [-1,0,1]

Example 3:

Input: n = 1
Output: [0]

'''
# Create a list
# if n = 1, then simply return 0
#-?-
# if number is even
## for i in range of n
### num is equal to i and its negative
# else if number is odd
## for i in range of n - but only up to an even
### num is equal to i and its negative
### then add zero
# return the list
def sumZero(n):
        """
        :type n: int
        :rtype: List[int]
        """
        list = []
        if n == 1:
            list.append(0)
            return list

        runs = n // 2
        if n % 2 ==0:
            for i in range(0,runs):
                num = i
                # num = i - (n/2)
                list.append(num)
                num = num * -1
                list.append(num)
        else:
            for i in range(0,runs):
                # num = i - ((n/2)-1)
                num = i
                list.append(num)
                num = num * -1
                list.append(num)
            list.append(0)

        print(n)
        return list

print(sumZero(6))
print("-----------")
print(sumZero(5))
