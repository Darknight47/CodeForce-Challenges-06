"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1676/A ------------

A ticket is a string consisting of six digits. A ticket is considered lucky if the sum of the first three 
digits is equal to the sum of the last three digits. Given a ticket, output if it is lucky or not. 
Note that a ticket can have leading zeroes.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 10^3) — the number of testcases.

The description of each test consists of one line containing one string consisting of six digits.

Output
Output t lines, each of which contains the answer to the corresponding test case. 
Output "YES" if the given ticket is lucky, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

"""

cases = int(input())
for i in range(cases):
    num = int(input())
    first = 0
    temp = 0
    second = 0
    while(num > 0):
        dig = num % 10
        temp += 1
        num = num // 10
        if(temp < 4):
            first += dig
        else:
            second += dig
    print("YES" if first == second else "NO")