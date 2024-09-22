from typing import List

class Solution(object):
    #2824. Count Pairs Whose Sum is Less than Target 
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        counter=0
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if (nums[i]+nums[j]<target and i<j):
                    counter+=1
                    print(str(nums[i])+'+'+str(nums[j])+"<"+str(target))
        return counter

    # 2000. Reverse Prefix of Word

    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        word_length=len(word)
        for i in range(word_length):
            if word[i]==ch:
                return word[i::-1]+word[i+1:word_length]
        return False
    
    # 3194. Minimum Average of Smallest and Largest Elements
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        n=len(nums)
        nums.sort()
        min_avg=((min(nums)+max(nums))/2)
        for i in range(1,n):
            avg=(nums[i]+nums[n-1-i])/2
            if avg<min_avg:
                min_avg=avg
        
        return min_avg
    
    # 3194. Alternative: Minimum Average of Smallest and Largest Elements
    def alternativeMinimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        ans = 1e9
        i, j = 0, len(nums)-1
        while i <= j:
            ans = min(ans, (nums[i]+nums[j])/2.0)
            i += 1
            j -= 1
        return ans
    
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
    # 28. Find the Index of the First Occurrence in a String
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

solution = Solution()
print(solution.countPairs([-6,2,5,-2,-7,-1,3],-2))
print(solution.reversePrefix('abcdefd','d'))
print(solution.minimumAverage([1,9,8,3,10,5]))
print(solution.alternativeMinimumAverage([1,9,8,3,10,5]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(solution.removeElement([0,1,2,2,3,0,4,2],2))
print(solution.strStr("sadbutsad", "sad"))
