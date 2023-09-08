"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1300/A -----------
Guy-Manuel and Thomas have an array a of n integers [a1,a2,…,an]. 
In one step they can add 1 to any element of the array. Formally, in one step they can choose any integer index i
(1 ≤ i ≤ n) and do ai:=ai+1.

If either the sum or the product of all elements in the array is equal to zero, Guy-Manuel and Thomas 
do not mind to do this operation one more time.

What is the minimum number of steps they need to do to make both the sum and the product of all 
elements in the array different from zero? 
Formally, find the minimum number of steps to make a1+a2+…+an≠0and a1⋅a2⋅…⋅an≠0.

Input
Each test contains multiple test cases.

The first line contains the number of test cases t
(1 ≤ t ≤ 10^3). The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 100) — the size of the array.

The second line of each test case contains n 
integers a1,a2,…,an (−100 ≤ a(i) ≤100) — elements of the array .

Output
For each test case, output the minimum number of steps required to make both sum and 
product of all elements in the array different from zero.

Input:
4
3
2 -1 -1
4
-1 0 0 1
2
-1 2
3
0 -2 1

Output:
1
2
0
2
"""

cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = sorted(list(map(int, input().split())))
    lstSum = 0
    lstMul = 1
    ans = 0
    zeros = 0
    for j in range(sze):
        temp = lst[j]
        if(temp == 0):
            zeros += 1
            lst[j] = 1
        lstSum += lst[j]
        lstMul *= lst[j]
    while True:
        if(lstSum != 0 and lstMul != 0):
            break
        lst[0] = lst[0] + 1
        ans += 1
        lstSum += 1
    print(ans + zeros)    
    