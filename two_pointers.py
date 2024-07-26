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
    
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        n=len(nums)        
        nums.sort()
        min_avg=(nums[0]+nums[-1])/2
        for i in range(1,n//2):
            avg=(nums[i]+nums[n-1-i])/2
            if avg<min_avg:
                min_avg=avg
        return min_avg

solution = Solution()
print(solution.countPairs([-6,2,5,-2,-7,-1,3],-2))
print(solution.reversePrefix('abcdefd','d'))
print(solution.minimumAverage([7,8,3,4,15,13,4,1]))

