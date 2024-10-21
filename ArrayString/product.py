# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].


# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

nums = [1,2,3,4]
n=len(nums)
l_mul = 1
r_mul = 1
l_arr =[0]* n
r_arr =[0]* n


for i in range(n):
    j= -i -1

    l_arr[i]=l_mul
    r_arr[j]=r_mul

    l_mul *= nums[i]
    r_mul*= nums[j]

print(l*r for l,r in zip(l_arr,r_arr))