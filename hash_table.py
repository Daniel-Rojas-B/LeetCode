from typing import List
from collections import defaultdict

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

solution = Solution()
print(solution.numIdenticalPairs([1,2,3,1,1,3]))
print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))
print(solution.alternativeSmallerNumbersThanCurrent([8,1,2,2,3]))
print(solution.sortPeople(["Mary","John","Emma"], [180,165,170]))
print(solution.findIntersectionValues([2,3,2],[1,2]))
print(solution.findPermutationDifference("abc","bac"))
print(solution.nextGreaterElement([4,1,2], [1,3,4,2]))
print(solution.twoSum([2,7,11,15], 9))