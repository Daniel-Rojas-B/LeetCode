from typing import List
from typing import List
from collections import defaultdict
from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def list_to_linked_list(items):
    """Convert a Python list to a linked list."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

class Solution(object):
    # 2. Add two numbers
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = current = ListNode(0)

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, val = divmod(v1 + v2 + carry, 10)

            current.next = ListNode(val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

    def reverse(self, x: int) -> int:
        mod = 2**31  # Modulo for overflow checking
        sign = -1 if x < 0 else 1
        x *= sign
        
        reversed_number = int(str(x)[::-1])
        
        # Check for overflow
        if reversed_number > mod - 1:
            return 0
        return sign * reversed_number
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x

    def intToRoman(self, num: int) -> str:
        Roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman

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
    
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def decode(num):
            ans = 0
            for i in num:
                ans = ans*10 +(ord(i) - ord('0'))
            return ans

        def encode(s):
            news = ''
            while s:
                a = s % 10
                s = s // 10
                news = chr(ord('0') + a) + news
            return news
        
        return encode(decode(num1)*decode(num2))

    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for j in range(n//2):
                row[j], row[~j] = row[~j], row[j]
        return A

    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
    # Convert the range to a list so we can modify it
        numbers = list(range(1, n + 1))
        permutation = ''
        k -= 1  # To make k zero-indexed
        while n > 0:
            n -= 1
            # Get the index of the current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # Remove the handled number
            numbers.pop(index)  # Use pop instead of remove for efficiency

        return permutation
    
    # math C(m+n-2,n-1)
    def uniquePaths1(self, m, n):
        if not m or not n:
            return 0
        return math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1))
    
    # O(m*n) space   
    def uniquePaths2(self, m, n):
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    # O(n) space 
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
    
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

def linked_list_to_list(head):
    """Convert a linked list back to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Input lists
list1 = [2, 4, 3]
list2 = [5, 6, 4]

# Convert input lists to linked lists
l1 = list_to_linked_list(list1)
l2 = list_to_linked_list(list2)

solution = Solution() 
result = solution.addTwoNumbers(l1, l2)

output = linked_list_to_list(result)
print(output)

print(solution.reverse(123))
print(solution.isPalindrome(1221))
print(solution.intToRoman(3749))
print(solution.romanToInt("MCMXCIV"))
print(solution.divide(10,3))
print(solution.multiply("2","3"))
print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.myPow(2,10))
print(solution.getPermutation(3,3))
print(solution.uniquePaths(3,7))
print(solution.plusOne([4,3,2,1]))