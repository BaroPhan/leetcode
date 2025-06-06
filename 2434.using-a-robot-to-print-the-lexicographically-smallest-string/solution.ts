/*
2434. Using a Robot to Print the Lexicographically Smallest String
https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.



Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba".
Perform second operation twice p="ab", s="c", t="".
Perform first operation p="ab", s="", t="c".
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".


Constraints:
1 <= s.length <= 105
s consists of only English lowercase letters.
*/

function robotWithString(s: string): string {
    const n = s.length
    const minList = Array(n).fill('')
    minList[n - 1] = s[n - 1]
    const t: string[] = [];
    const p: string[] = [];
    for (let i = n - 2; i >= 0; i--) {
        minList[i] = s[i] < minList[i + 1] ? s[i] : minList[i + 1];
    }
    let i = 0
    while (i < n || t.length > 0) {
        while (t.length > 0 && (i === n || t[t.length - 1] <= minList[i])) {
            p.push(t.pop()!);
        }
        if (i < n) {
            t.push(s[i]);
            i += 1
        }
        // console.log('t: ', t)
        // console.log('p: ', p)
        // console.log('==============')
    }
    // console.log(p)
    return p.join('');
};