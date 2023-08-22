"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1669/B ---------

Given an array a of n elements, print any value that appears at least three times 
or print -1 if there is no such value.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains an integer n (1 ≤ n ≤ 2⋅10^5) — the length of the array.

The second line of each test case contains n integers 
a1,a2,…,an (1 ≤ ai ≤ n) — the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print any value that appears at least three times or print -1 if there is no such value.

Input:
7
1
1
3
2 2 2
7
2 2 3 3 4 2 2
8
1 4 3 4 3 2 4 1
9
1 1 1 2 2 2 3 3 3
5
1 5 2 4 3
4
4 4 4 4

Output:
-1
2
2
4
3
-1
4

"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    freq = {}
    ans = -1
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if(freq[num] >= 3):
            ans = num
            break
    print(ans)