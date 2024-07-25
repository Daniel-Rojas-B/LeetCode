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
        
        n=len(word)
        for i in range(n):
            if word[i]==ch:
                return word[i::-1]+word[i+1:n]
        return word

solution = Solution()
print(solution.countPairs([-6,2,5,-2,-7,-1,3],-2))
print(solution.reversePrefix('abcdefd','d'))


        