'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 - My interpretation:
 In an array of constant even size, there is one element among the list that repeats (and can repeat any
 number of times). Return this element
 -


Example 1:

Input: [1,2,3,3]
Output: 3

Example 2:

Input: [2,1,2,5,3,2]
Output: 2

Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

'''
#Create a dictionary that counts the number of times a number appears
#add numbers to the dictionary
## If not in dictionary, add with count of 1
## else add to the count

#go through dictionary
# check if dictionary key has value greater than 1
# return that item

def repeatedNTimes(list):
        counter = {}
        for i in list:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1

        for j in counter:
            if counter[j] > 1:
                return j

#Using example info as test case
list = [2,1,2,5,3,2]
print(repeatedNTimes(list))
