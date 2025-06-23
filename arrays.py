from typing import List
from typing import List
from collections import defaultdict

class Solution(object):
    # 11. Container With Most Water
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
    #1929. Concatenation of Array 
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
    #1920. Build Array from Permutation
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
    #2932. Maximum Strong Pair XOR I
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_array=[]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(abs(nums[i]-nums[j])<=min(nums[i],nums[j])):
                    xor_array.append(nums[i]^nums[j])
        return max(xor_array)
    
    #1480. Running Sum of 1d Array
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum=[nums[0]]
        for i in range(len(nums)-1):            
            running_sum.append(running_sum[i]+nums[i+1])
        return running_sum

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
        
    # 35. Search Insert Position
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

    # 66. Plus One
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the list from the last element to the first
        for i in range(len(digits)-1, -1, -1):
            # If the current digit is 9, set it to 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # If the current digit is not 9, increment it by 1 and return the list
                digits[i] = digits[i] + 1
                return digits
        # If all digits are 9, prepend 1 to the list
        return [1] + digits
    
    # 1. Two Sum
    def twoSum(self, nums, target):
        # Create a dictionary to store numbers and their corresponding indices
        number_map = {}

        # Loop through the array
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - num

            # Check if the difference already exists in the dictionary
            if diff in number_map:
                # If it exists, return the indices of the current number and the number that adds up to the target
                return [i, number_map[diff]]

            # If it doesn't exist, add the current number and its index to the dictionary
            number_map[num] = i
        
        # If no two numbers add up to the target, return None
        return None

    # 11. Container With Most Water
    def maxArea(self, height):
        left = 0            # Left pointer starting from the leftmost edge
        right = len(height) - 1  # Right pointer starting from the rightmost edge
        maxWater = 0        # Initialize the maximum water capacity
        
        while left < right:
            # Calculate the width of the container
            width = right - left
            
            # Calculate the height of the container (the minimum height between the two lines)
            h = min(height[left], height[right])
            
            # Calculate the water capacity of the current container
            water = width * h
            
            # Update the maximum water capacity if the current container holds more water
            maxWater = max(maxWater, water)
            
            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxWater
# 15. 3Sum
    def threeSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            res = set()
            nums.sort()
            for i, a in enumerate(nums):
                if i > 0 and a == nums[i-1]: continue

                l, r = i + 1, len(nums) - 1
                while l < r:
                    sum = a + nums[l] + nums[r]
                    if sum > 0: r -=1
                    elif sum < 0: l +=1
                    else: 
                        if (a, nums[l], nums[r]) not in res:
                            res.add((a, nums[l], nums[r]))
                        l +=1
            return [list(s) for s in res]

# 49. Group Anagrams    
    def getSignature(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)

        result.extend(groups.values())

        return result
    
    # 36. Valid Sudoku
    def isValidSudoku(self, board):
        return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
        
    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
        
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])

        for i in range(1, target + 1):
            for candidate in candidates:
                if candidate <= i:
                    for prev in dp[i - candidate]:
                        temp = prev + [candidate]
                        temp.sort()
                        if temp not in dp[i]:
                            dp[i].append(temp)
        return dp[target] 

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(result, [], candidates, target, 0)
        return result
    
    def backtrack(self, result: List[List[int]], current: List[int], candidates: List[int], remaining: int, start: int):
        if remaining < 0:
            return
        elif remaining == 0:
            result.append(list(current))
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                self.backtrack(result, current, candidates, remaining - candidates[i], i + 1)
                current.pop()
        
    # 15. 3Sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
    # 16. 3Sum closest
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff

solution = Solution()

print(solution.getConcatenation([1,2,1]))
print(solution.buildArray([0,2,1,5,3,4]))
print(solution.maximumStrongPairXor([1,2,3,4,5]))
print(solution.runningSum([1,2,3,4,5]))
print(solution.removeDuplicates([2,1,1]))
print(solution.removeElement([3,2,2,3],2))
print(solution.searchInsert([1,3,5,6],7))
print(solution.plusOne([1,2,3]))
print(solution.twoSum([3,2,4],6))
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.threeSum([0,0,0]))
print(solution.groupAnagrams([""]))
print(solution.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(solution.combinationSum([2,3,6,7],7))
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSumClosest([-1,2,1,-4],1))