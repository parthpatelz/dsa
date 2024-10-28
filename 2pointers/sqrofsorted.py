# 977. Squares of a Sorted Array
# Easy

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sortedSquares():
    nums = [-4,-1,0,3,10]
    n=len(nums)
    l=0
    r=n-1
    a=[]

    while l<=r:
        if abs(nums[l])>abs(nums[r]):
            a.append(nums[l]**2)
            l+=1
        else:
            a.append(nums[r]**2)
            r-=1
    a.reverse()
    return a

print(sortedSquares())