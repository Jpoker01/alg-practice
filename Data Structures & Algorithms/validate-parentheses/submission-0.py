class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []

        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            else:
                if not stack or stack.pop() != c:
                    return False
        
        #return true only if stack empty
        return not stack
        