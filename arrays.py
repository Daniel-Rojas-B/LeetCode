from typing import List

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
    #2932. Maximum Strong Pair XOR I
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_array=[]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(abs(nums[i]-nums[j])<=min(nums[i],nums[j])):
                    xor_array.append(nums[i]^nums[j])
        return max(xor_array)
    
    #1480. Running Sum of 1d Array
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum=[nums[0]]
        for i in range(len(nums)-1):            
            running_sum.append(running_sum[i]+nums[i+1])
        return running_sum

    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
          nums[:] = sorted(set(nums))
          return len(nums)
    
    # 27. Remove Element

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i
        
    

    
solution = Solution()
print(solution.getConcatenation([1,2,1]))
print(solution.buildArray([0,2,1,5,3,4]))
print(solution.maximumStrongPairXor([1,2,3,4,5]))
print(solution.runningSum([1,2,3,4,5]))
print(solution.removeDuplicates([2,1,1]))
print(solution.removeElement([3,2,2,3],2))