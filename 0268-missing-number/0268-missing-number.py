class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        a=0
        b=0
        for i in range(n):
           a^=nums[i]
           b^=i
        a^=n
        return a^b 
        