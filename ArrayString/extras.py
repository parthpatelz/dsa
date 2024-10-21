nums = [-4,-2,1,4,8]

# for i in range(len(nums)):
#         if(range(len(abs(nums[i])))):
#                 print(i)

# n= range(len(nums))-1
# for i in nums[n-1]:
#     print(i)

target=9
for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                  print(i, j)
            else:
                  print()