class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i =1
        for i in range (n):
            nums[i]+=nums[i-1]
        return nums
