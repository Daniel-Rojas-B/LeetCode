class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans

solution = Solution()
print(solution.getConcatenation([1,2,1]))