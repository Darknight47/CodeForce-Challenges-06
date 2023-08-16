"""
---------- Link for the challenge: https://codeforces.com/contest/1729/problem/B --------

Polycarp has a string s consisting of lowercase Latin letters.

He encodes it using the following algorithm.

He goes through the letters of the string s from left to right and for each letter Polycarp considers its number in the alphabet:

if the letter number is single-digit number (less than 10), then just writes it out; 
if the letter number is a two-digit number (greater than or equal to 10), then it writes it out and adds the number 0 after.
For example, if the string s is code, then Polycarp will encode this string as follows:

'c' — is the 3-rd letter of the alphabet. Consequently, Polycarp adds 3 to the code (the code becomes equal to 3);
'o' — is the 15-th letter of the alphabet. Consequently, Polycarp adds 15 to the code and also 0 (the code becomes 3150);
'd' — is the 4 -th letter of the alphabet. Consequently, Polycarp adds 4 to the code (the code becomes 31504);
'e' — is the 5 -th letter of the alphabet. 
Therefore, Polycarp adds 5 to the code (the code becomes 315045).
Thus, code of string code is 315045.

You are given a string t resulting from encoding the string s. 
Your task is to decode it (get the original string s by t).

Input
The first line of the input contains an integer q (1 ≤ q ≤ 10^4) — the number of test cases in the input.

The descriptions of the test cases follow.

The first line of description of each test case contains one integer n (1 ≤ n ≤ 50) — 
the length of the given code.

The second line of the description of each test case contains a string t of length n — the given code. 
It is guaranteed that there exists such a string of lowercase Latin letters, as a result of encoding which the string t is obtained.

Output
For each test case output the required string s — the string that gives string t as the result of encoding. 
It is guaranteed that such a string always exists. It can be shown that such a string is always unique.

"""

import string
alphabet = list(string.ascii_lowercase)
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(input())
    indx = sze 
    ans = ""
    while True:
        indx -= 1
        if(indx < 0):
            break
        c = arr[indx]
        if(c == '0'):
            indx -= 1
            c2 = arr[indx]
            indx -= 1
            c3 = arr[indx]
            ct = c3 + c2
            num1 = int(ct) - 1
            ans += alphabet[num1]
        else:
            num2 = int(c) - 1
            ans += alphabet[num2]
    print(ans[::-1])