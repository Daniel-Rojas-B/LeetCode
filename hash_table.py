
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
           

solution = Solution()
print(solution.numIdenticalPairs([1,2,3,1,1,3]))
print(solution.smallerNumbersThanCurrent([8,1,2,2,3]))
print(solution.alternativeSmallerNumbersThanCurrent([8,1,2,2,3]))
print(solution.sortPeople(["Mary","John","Emma"], [180,165,170]))
