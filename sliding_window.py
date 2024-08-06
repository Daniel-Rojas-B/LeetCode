from collections import Counter

class Solution(object):
    # 1876. Substrings of Size Three with Distinct Characters
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """    
        counter=0
        for i in range(len(s) - 2):
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                counter += 1

        return counter
    # 219. Contains Duplicate II
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hset={}
        for i in range(len(nums)):
            if nums[i] in hset and abs(i-hset[nums[i]]<=k):
                return True
            hset[nums[i]]=i
        return False
    # 594. Longest Harmonious Subsequence
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = Counter(nums)
        print(tmp)
        keys = tmp.keys()
        print(keys)
        max = 0
        for num in keys:
            if num - 1 in keys:
                if tmp[num - 1] + tmp[num] > max:
                    max = tmp[num - 1] + tmp[num]
        return max
    # 3206. Alternating Groups I
    
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        if n < 3:
            return 0

        ans = 0
        for i in range(n - 2):
            if colors[i] == colors[i + 2] and colors[i] != colors[i + 1]:
                ans += 1
        
        if colors[0] == colors[n - 2] and colors[0] != colors[n - 1]:
            ans += 1
        
        if colors[0] != colors[1] and colors[1] == colors[n - 1]:
            ans += 1
        
        return ans
    
solution = Solution()
print(solution.countGoodSubstrings("aababcabc"))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3],2))
print(solution.findLHS([1,3,2,2,5,2,3,7]))
print(solution.numberOfAlternatingGroups([1,1,1]))