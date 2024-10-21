# 217. Contains Duplicate


# Example 1:

# Input: 
nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

s=set()
h=False
for i in nums:
    if i in s:
        h=True
    else:
        s.add(i)

print(h)

# nums = [1,2,3,1]

# for i in range(len(nums)):
#                 for j in range(i+1,len(nums)):
#                     if nums[i]==nums[j]:
#                         print("true")
#                         break