class Solution(object):
    #1929. Concatenation of Array 
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
    #1920. Build Array from Permutation
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

solution = Solution()
print(solution.getConcatenation([1,2,1]))
print(solution.buildArray([0,2,1,5,3,4]))