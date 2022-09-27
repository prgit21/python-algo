class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, l, r = 0, 0, len(height)-1
        while (l< r):
            if height[l] <= height[r]:
                res = height[l] * (r - i)
                l+= 1
            else:
                res = height[r] * (r - i)
                r-= 1
            if res > ans: ans = res
        return ans
