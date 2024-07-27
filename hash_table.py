# 1512. Number of Good Pairs: A pair (i, j) is called good if nums[i] == nums[j] and i < j.
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pairs=0   
                           
        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    pairs+=1            
        return pairs

solution = Solution()
print(solution.numIdenticalPairs([1,2,3,1,1,3]))