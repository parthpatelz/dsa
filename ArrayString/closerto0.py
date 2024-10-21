def findClosestNumber():
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-4,-2,1,4,8]


# if abs(num) < abs(s) or (abs(num) == abs(s) and num > s):
#                         s = num  # Update s if num is closer to zero or equally close but larger
        
        # smallest = 0
        # for i in nums:
        #     if abs(i) == 0:
        #         return 0
        #     elif smallest == 0 or abs(i) < abs(smallest):
        #         smallest = i
        #     elif abs(i) == abs(smallest):
        #         if i > smallest:
        #             smallest = i
        # return smallest
        
        s = nums[0]
        for num in nums[1:]:
                if abs(num) < abs(s) or (abs(num)==abs(s) and num > s):
                        s= num
        return s


print(findClosestNumber())