class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for i in s:
            stack.append(i)
        for j in range(len(stack)):
            s[j] =stack.pop()