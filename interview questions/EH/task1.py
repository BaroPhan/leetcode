"""
Task 1
Write a function function solution(x, y) that, given a string x and a string y, returns a boolean that checks whether all of the characters in the string y exist at some point in the string x. Furthermore, the characters from y need to occur in the same order in x. There may be additional characters in string x, so long as each character from y appears and the order is maintained.

If all of the characters from y appear in x in the correct order return the boolean true, otherwise return false.

Both of the input strings will consist of alpha-numeric characters only. The length of the strings may be quite large so performance should be a consideration for your solution.

Example 1
x = "ABCD"
y = "AC"
Result = true
The expected result is true because "A" and "C" both appear in "ABCD" and in that order.

Example 2
x = "ABCD"
y = "CA"
Result = false
The expected result is false because even though "C" and "A" both appear in "ABCD" the order in x is different to y.

Example 3
x = "ABCAD"
y = "BA"
Result = true
The expected result is true because "B" and "A" both appear in "ABCAD". Note, the first "A" appears before the "B" but then there is a subsequent "A" so the result should be true.
"""



class Solution:
    def task1(self, x: str, y: str) -> bool:
        print(y[0])
        for char in x:
            if char == y[0]:
                y = y[1:]
            if not y: 
                return True
        return False

sol = Solution()
result = sol.task1("ABCD", "CA")
print(result)