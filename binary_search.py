from typing import List
from typing import List
from collections import defaultdict

class Solution(object):
    # 4. Median of Two Sorted Arrays
    def findMedianSortedArrays(self,nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

    # 33. Search in Rotated Sorted Array
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
    # 34. Find First and Last Position of Element in Sorted Array
    def binary_search(self, nums, target, find_first):
        s = 0
        e = len(nums) - 1
        index = -1
        while s <= e:
            mid = s + (e - s) // 2
            if nums[mid] == target:
                index = mid
                if find_first:
                    e = mid - 1  # Find first occurrence
                else:
                    s = mid + 1  # Find last occurrence
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binary_search(nums, target, True)
        last = self.binary_search(nums, target, False)
        return [first, last]
    # 69. Sqrt(x)
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right
    # 74. Search a 2D Matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,columns=len(matrix),len(matrix[0])
        top,bottom=0,rows-1
        while top<=bottom:
            row=(top+bottom)//2
            if target<matrix[row][0]:
                bottom=row-1
            elif target>matrix[row][-1]:
                top=row+1
            else:
                break
        row=(top+bottom)//2
        l,r=0,columns-1
        while l<=r:
            mid=(l+r)//2
            if target<matrix[row][mid]:
                r=mid-1
            elif target>matrix[row][mid]:
                l=mid+1
            else:
                return True
        return False
    # 81. Search in Rotated Sorted Array II
    def search_two(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1
        
        return False
solution = Solution()
print(solution.findMedianSortedArrays([1,2], [3,4]))
print(solution.search([4,5,6,7,0,1,2], 0))
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.mySqrt(64))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(solution.search_two([2,5,6,0,0,1,2],0))