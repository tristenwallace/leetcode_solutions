class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(',
                '}':'{',
                ']':'['
                }
        
        stack = []
        print('checking: {}'.format(s))
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif len(stack) > 0:
                if pairs[char] == stack[-1]:
                    print(stack[-1])
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False

##############################################################################

solution = Solution()

assert solution.isValid("()") == True
assert solution.isValid("()[]{}") == True       
assert solution.isValid("(]") == False
assert solution.isValid("([)]") == False
assert solution.isValid("(") == False
assert solution.isValid("]") == False
assert solution.isValid("(])") == False


print("\nIf this the only statement, GREAT!")