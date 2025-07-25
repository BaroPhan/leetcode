"""
3304. Find the K-th Character in String Game I
https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.



Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Example 2:

Input: k = 10

Output: "c"



Constraints:
1 <= k <= 500
"""


class Solution:
    def kthCharacter(self, k: int) -> str:
        w = "a"
        while len(w) < k:
            next = ""
            for c in w:
                next += chr(ord(c) + 1)
            w += next
        # print(w, w[k - 1])
        return w[k - 1]
