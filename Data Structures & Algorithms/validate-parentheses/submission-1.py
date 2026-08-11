class Solution:
    def isValid(self, s: str) -> bool:
        paran = ('(', ')')
        curl = ('{', '}')
        brack = ('[', ']')
        stack = []

        if s[0] in (paran[1], curl[1], brack[1]):
            return False

        for i, char in enumerate(s):
            if char == paran[0]:
                stack.append(char)
            if char == curl[0]:
                stack.append(char)
            if char == brack[0]:
                stack.append(char)
            if char == paran[1]:
                if stack and stack[-1] == paran[0]:
                    stack.pop()
                else:
                    return False
            if char == curl[1]:
                if stack and stack[-1] == curl[0]:
                    stack.pop()
                else:
                    return False
            if char == brack[1]:
                if stack and stack[-1] == brack[0]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False