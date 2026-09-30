class Solution(object):
    def rearrangeArray(self, nums):
        n = [0] * len(nums)

        a = 0
        b = 1

        for num in nums:
            if num > 0:
                n[a] = num
                a += 2
            else:
                n[b] = num
                b += 2

        return n