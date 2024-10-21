# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.



# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

#

from collections import defaultdict
def longestConsecutive():
    nums = [0,3,7,2,5,8,4,6,0,1]
    s=defaultdict(int)
    longest=0
    s=set(nums)
    for num in s:
        if num-1 not in s:
            next_num= num+1
            length=1
            while next_num in s:
                length+=1
                next_num+=1
            longest=max(longest,length)
    return longest




# print(longestConsecutive())