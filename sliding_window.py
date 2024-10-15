from collections import Counter
from typing import List
from collections import deque, defaultdict

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

    # 2269. Find the K-Beauty of a Number
    def divisorSubstrings(self, num: int, k: int) -> int:
        l = 0
        r = k

        num = str(num)
        count = 0
        while r <= len(num):            
            n = int(num[l: r])

            # handle case where n could be '0'. 
            if not n:
                l += 1
                r += 1
                continue

            if int(num) % n == 0:
                count += 1   
                
            # slide window
            l += 1
            r += 1

        return count
    # 2379. Minimum Recolors to Get K Consecutive Black Blocks
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n, minOps, flips, count, i = len(blocks), 1e9, 0, 0, 0
        for j in range (n):
            if blocks[j] == 'W':
                flips += 1
                count += 1
            elif blocks[j] == 'B':
                count += 1
            if count == k:
                minOps = min(minOps, flips)
                if blocks[i] == 'W':
                    flips -= 1
                    count -= 1
                else: count -= 1
                i += 1
        return minOps
    # 1984. Minimum Difference Between Highest and Lowest of K Scores
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums = sorted(nums)
        res = nums[k-1] - nums[0]

        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i - k + 1])

        return res

    # 594. Longest Harmonious Subsequence
    class Solution:
        def findLHS(self, nums: List[int]) -> int:
            freq = Counter(nums)
            max_length = 0
            
            for key in freq:
                if key + 1 in freq:
                    max_length = max(max_length, freq[key] + freq[key+1])
                    
            return max_length
    # 30. Substring with Concatenation of All Words
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        ori_word_dict = defaultdict(int)
		
        for word in words:
            ori_word_dict[word] += 1
        
        all_word_len = len(words) * word_len
        result = []
        for i in range(word_len):
            queue = deque()
            word_dict = ori_word_dict.copy()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word_dict.get(word, 0) != 0:
                    word_dict[word] -= 1
                    queue.append(word)
                    if sum(word_dict.values()) == 0:
                        result.append(j - all_word_len + word_len)
                        last_element = queue.popleft()
                        word_dict[last_element] = word_dict.get(last_element, 0) + 1
                else:
                    while len(queue):
                        last_element = queue.popleft()
                        if last_element == word:
                            queue.append(word)
                            break
                        else:
                            word_dict[last_element] = word_dict.get(last_element, 0) + 1
                            if word_dict[last_element] > ori_word_dict[last_element]:
                                word_dict = ori_word_dict.copy()

        return result
solution = Solution()
print(solution.countGoodSubstrings("aababcabc"))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3],2))
print(solution.findLHS([1,3,2,2,5,2,3,7]))
print(solution.numberOfAlternatingGroups([1,1,1]))
print(solution.decrypt([2,4,9,3],-2))
print(solution.maximumLengthSubstring("bcbbbcba"))
print(solution.longestNiceSubstring("YazaAay"))
print(solution.divisorSubstrings(240,2))
print(solution.minimumRecolors("WBWBBBW",2))
print(solution.minimumDifference([9,4,1,7],2))
print(solution.findLHS([1,3,2,2,5,2,3,7]))
print(solution.findSubstring("barfoothefoobarman", ["foo","bar"]))