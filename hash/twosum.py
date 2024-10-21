from collections import Counter,defaultdict
def twoSum():
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [7,3,2,15,6]
        target = 9
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==9:
        #             return n[i],n[j]
        #         else:
        #             return False
        # H=Counter(nums)
        hmap={}
        for i in range(len(nums)):
                hmap[nums[i]]=i
        for i in range(len(nums)):
                y=target-nums[i]

                if y in hmap:
                        # if hmap[y] != i:
                            return i,hmap[y]





print(twoSum())