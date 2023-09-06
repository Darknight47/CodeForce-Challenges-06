"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/1228/A ---------
You have two integers l and r. 
Find an integer x which satisfies the conditions below: l ≤ x ≤ r.
All digits of x are different. If there are multiple answers, print any of them.

Input
The first line contains two integers l and r (1 ≤ l ≤ r ≤ 10^5).

Output
If an answer exists, print any of them. Otherwise, print −1.

Input:
121 130

Output:
123
"""
l, x = map(int, input().split())
ans = -1
founded = False
for i in range(l, x+1):
    if len(set(str(i))) == len(str(i)):
        founded = True
        ans = i
        break
print(ans)
    