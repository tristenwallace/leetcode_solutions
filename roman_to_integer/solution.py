class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
                }
        count = 0
        previous_char = ''
        for char in reversed(s):
            if (char == 'I' and previous_char in ['V','X']) \
                or (char == 'X' and previous_char in ['L','C']) \
                or (char == 'C' and previous_char in ['D','M']):
                    count -= values[char]
            else:
                count += values[char]
            previous_char = char
        
        return count

solution = Solution()

tests = ["III",
        "LVIII",
        "MCMXCIV"
        ]
for test in tests:
    assert solution.romanToInt(test)

print("\nIf this the only statement, GREAT!")