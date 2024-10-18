from typing import List
from collections import defaultdict
from collections import deque, defaultdict

class Solution(object):
    # 1512. Number of Good Pairs: A pair (i, j) is called good if nums[i] == nums[j] and i < j.
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
    
    # 1365. How Many Numbers Are Smaller Than the Current Number
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array_with_times=[]
        counter=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    counter+=1
            array_with_times.append(counter)
            counter=0
        return array_with_times
    
    # 1365. alternative: How Many Numbers Are Smaller Than the Current Number
    def alternativeSmallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print(sorted(nums))
        return [sorted(nums).index(i) for i in nums]

    # 2418. Sort the People
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Step 1: Pairing names with their corresponding heights
        paired = [(names[i], heights[i]) for i in range(len(names))]
        print([(names[i], heights[i]) for i in range(len(names))])
        # Step 2: Sorting the pairs based on heights in descending order
        paired.sort(key=lambda x: x[1], reverse=True)
        print(paired)
        # Step 3: Extracting sorted names from the sorted pairs
        sorted_names = [names for names, heights in paired]

        return sorted_names 
    
    # 2956. Find Common Elements Between Two Arrays
    
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans1=0
        ans2=0
        ans_array=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans1+=1
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                ans2+=1
        ans_array = [ans1,ans2]
        return ans_array

    # 3146. Permutation Difference between Two Strings
    def findPermutationDifference(self, s: str, t: str) -> int:
        ht: dict[str, int] = dict()
        for i in range(len(s)):
            if s[i] in ht:
                ht[s[i]] = abs(ht[s[i]] - i)
            else:
                ht[s[i]] = i
            if t[i] in ht:
                ht[t[i]] = abs(ht[t[i]] - i)
            else:
                ht[t[i]] = i
        return sum(ht.values())

    # 496. Next Greater Element I
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=defaultdict(lambda:0) 
        for i in range(len(nums1)):
            d[nums1[i]]=i 
        st,ans=[],[0]*len(nums1) 
        j=len(nums2)-1 
        while j>=0:
            if nums2[j] in d:
                if st==[]:
                    ans[d[nums2[j]]]=-1 
                elif st!=[] and st[-1]>nums2[j]:
                    ans[d[nums2[j]]]=st[-1] 
                elif st!=[] and st[-1]<=nums2[j]:
                    while st!=[] and st[-1]<=nums2[j]:
                        st.pop() 
                    if st==[]:
                        ans[d[nums2[j]]]=-1 
                    else:
                        ans[d[nums2[j]]]=st[-1]
            st.append(nums2[j]) 
            j-=1 
        return ans

    # 1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []

    # 13. Roman to Integer
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
    # 49. Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        k=[]
        for i in strs:
            l="".join(sorted(i))
            dic.setdefault(l,[]).append(i)
      
        return dic.values()
    
    # 3. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length
    # 
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
print(solution.numIdenticalPairs([1,2,3,1,1,3]))
print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))
print(solution.alternativeSmallerNumbersThanCurrent([8,1,2,2,3]))
print(solution.sortPeople(["Mary","John","Emma"], [180,165,170]))
print(solution.findIntersectionValues([2,3,2],[1,2]))
print(solution.findPermutationDifference("abc","bac"))
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))
print(solution.twoSum([2,7,11,15], 9))
print(solution.romanToInt("LVIII"))
print(solution.groupAnagrams(["a"]))
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.findSubstring("barfoothefoobarman", words = ["foo","bar"]))