"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/1633/A ------

You are given an integer n. 
You have to change the minimum number of digits in it in such a way that 
the resulting number does not have any leading zeroes and is divisible by 7.

If there are multiple ways to do it, print any of them. 
If the given number is already divisible by 7, leave it unchanged.

Input
The first line contains one integer t (1 ≤ t ≤ 990) — the number of test cases.

Then the test cases follow, each test case consists of one line containing one integer n (10 ≤ n ≤ 999).

Output
For each test case, print one integer without any leading zeroes — the result of your changes 
(i. e. the integer that is divisible by 7 and can be obtained by changing the minimum possible number of digits in n).

If there are multiple ways to apply changes, print any resulting number. 
If the given number is already divisible by 7, just print it.

Input:
3
42
23
377

Output:
42
28
777
"""

cases = int(input())
for i in range(cases):
    num = int(input())
    next_div = num + (7 - num % 7)
    print(next_div)