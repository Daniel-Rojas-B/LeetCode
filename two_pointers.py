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

solution = Solution()
print(solution.countPairs([-6,2,5,-2,-7,-1,3],-2))
print(solution.reversePrefix('abcdefd','d'))
print(solution.minimumAverage([1,9,8,3,10,5]))
print(solution.alternativeMinimumAverage([1,9,8,3,10,5]))


