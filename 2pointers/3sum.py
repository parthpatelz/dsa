# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input:
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def threeSum():
    nums = [-1,0,1,2,-1,-4]
    nums.sort()
    n=len(nums)
    ans=[]

    for i in range(n):

        if nums[i]>0:
                break
        elif i>  0 and nums[i] == nums[i-1]:
                continue

        l=i+1
        h=n-1

        while l<h:
            sum=nums[i]+nums[l]+nums[h]
            if sum==0:
                ans.append([nums[i],nums[l],nums[h]])
                l+=1
                h-=1
                while nums[l]==nums[l-1]:
                    l+=1
                while  nums[h]==nums[h+1]:
                    h-=1
            elif sum<0:
                l+=1
            else:
                h-=1
    return ans

print(threeSum())