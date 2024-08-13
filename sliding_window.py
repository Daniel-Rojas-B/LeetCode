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
    
    # 1652. Defuse the Bomb
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        output=[]
        for i in range(len(code)):
            if k>0:
                sum=0
                j=i+1
                m=k
                while(m):
                    sum+=code[j%len(code)]
                    m-=1
                    j+=1
                output.append(sum)
            elif k==0:
                output.append(0)
            else:
                sum=0
                j=i-1
                m=k
                while(m):
                    sum+=code[j%len(code)]                    
                    m+=1
                    j-=1
                output.append(sum)
        return output
        
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        maxLen = 0
        for i in range(n):
            arr = [0] * 26
            for j in range(i, n):
                arr[ord(s[j]) - ord('a')] += 1
                if arr[ord(s[j]) - ord('a')] == 3:
                    break
                maxLen = max(maxLen, j - i + 1)
        return maxLen

    # 1763. Longest Nice Substring
    def longestNiceSubstring(self, s: str) -> str:
        
        # If length of string is less than 2, there is no way we can get a nice substring out of it
        if len(s) < 2 : return ""
        
        # A set of all characters in the given string
        ulSet = set(s)
        
        for i,c in enumerate(s):
            # If character is lowercase and the set does not have its uppercase variation or vice versa
            # It means that we need to not consider this character at all and so, find the longest substring till this character and after this character
            # Repeat this till we reach the end
            if c.swapcase() not in ulSet:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                
                return s2 if len(s2) > len(s1) else s1
        
        
        # If the above recursive calls don't happen that means our string has each character in lowercase and uppercase already so we can return it
        return s


solution = Solution()
print(solution.countGoodSubstrings("aababcabc"))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3],2))
print(solution.findLHS([1,3,2,2,5,2,3,7]))
print(solution.numberOfAlternatingGroups([1,1,1]))
print(solution.decrypt([2,4,9,3],-2))
print(solution.maximumLengthSubstring("bcbbbcba"))
print(solution.longestNiceSubstring("YazaAay"))