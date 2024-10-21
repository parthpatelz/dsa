# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import defaultdict
def majorityElement():
    nums = [2,2,1,1,2,1,2]
    # s=defaultdict(int)
    # for i in nums:
    #     s[i]+=1
    # print(s)
    # high=0
    # ans=-1
    # for key,val in s.items():
    #     if val>high:
    #         high=val
    #         ans=key
    # return ans
    count=0
    ans=-1

    for i in nums:
        if count==0:
            ans=nums[i]
        else:
            count+=1

    return ans



print(majorityElement())