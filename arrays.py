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
        
    # 35. Search Insert Position
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

    # 66. Plus One
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the list from the last element to the first
        for i in range(len(digits)-1, -1, -1):
            # If the current digit is 9, set it to 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # If the current digit is not 9, increment it by 1 and return the list
                digits[i] = digits[i] + 1
                return digits
        # If all digits are 9, prepend 1 to the list
        return [1] + digits
    
solution = Solution()
print(solution.getConcatenation([1,2,1]))
print(solution.buildArray([0,2,1,5,3,4]))
print(solution.maximumStrongPairXor([1,2,3,4,5]))
print(solution.runningSum([1,2,3,4,5]))
print(solution.removeDuplicates([2,1,1]))
print(solution.removeElement([3,2,2,3],2))
print(solution.searchInsert([1,3,5,6],7))
print(solution.plusOne([1,2,3]))