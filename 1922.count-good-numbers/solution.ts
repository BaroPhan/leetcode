/*
1922. Count Good Numbers
https://leetcode.com/problems/count-good-numbers
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303
 

Constraints:
1 <= n <= 1015
*/

function countGoodNumbers(n: number): number {
  const prime = 4;
  const even = 5;
  const mod = 1000000007;
  const half = Math.floor(n / 2);
  let res = 0n;

  if (n % 2 === 0) {
    res =
      (modPowBigInt(even, half, mod) * modPowBigInt(prime, half, mod)) %
      BigInt(mod);
  } else {
    res =
      (modPowBigInt(even, half + 1, mod) * modPowBigInt(prime, half, mod)) %
      BigInt(mod);
  }

  return Number(res);
}

function modPowBigInt(base: number, exponent: number, mod: number) {
  let baseBigInt = BigInt(base) % BigInt(mod);
  let result = 1n;
  let exponentBigInt = BigInt(exponent);
  const modBigInt = BigInt(mod);

  while (exponentBigInt > 0) {
    if (exponentBigInt % 2n === 1n) {
      result = (result * baseBigInt) % modBigInt;
    }
    exponentBigInt = exponentBigInt / 2n;
    baseBigInt = (baseBigInt * baseBigInt) % modBigInt;
  }

  return result;
}
