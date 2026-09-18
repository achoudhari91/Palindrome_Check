class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# Example
x = 121

solution = Solution()
print(solution.isPalindrome(x))
