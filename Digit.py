"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1811/A ----------

You have a positive number of length n and one additional digit.

You can insert this digit anywhere in the number, including at the beginning or at the end.

Your task is to make the result as large as possible.

For example, you have the number 76543, and the additional digit is 4. 
Then the maximum number you can get is 765443, and it can be obtained in two ways — 
by inserting a digit after the 3th or after the 4th digit of the number.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The descriptions of the test cases follow.

The first line of the description of each test case contains two integers n and d (1 ≤ n ≤ 2⋅10^5; 0 ≤ d ≤9) — 
the length of the number and an additional digit, respectively.

The second line of the description of each test case contains a string consisting of n digits — 
the number that you have initially. It is guaranteed that the number does not contain leading zeros.

It is guaranteed that the sum of n for all test cases does not exceed 2⋅10^5.

Output
For each test case, output a string consisting of n+1
digits — the maximum possible number that can be obtained.

Input:
11
5 4
76543
1 0
1
2 5
44
3 6
666
5 6
13579
5 8
97531
19 4
9876543210123456789
5 7
73737
8 1
20000000
7 0
7058959
12 1
828127127732

Output:
765443
10
544
6666
613579
987531
98765443210123456789
773737
210000000
70589590
8281271277321

"""
cases = int(input())
for i in range(cases):
    sze, dig = map(int, input().split())
    s = input()
    lst = list(s)
    ans = ""
    insertIndx = -1
    for j in range(sze):
        tempDig = int(lst[j])
        if(tempDig < dig):
            insertIndx = j
            break
    if(insertIndx == -1):
        insertIndx = sze + 1
    ans = s[0:insertIndx]
    ans += str(dig)
    ans += s[insertIndx:]
    print(ans)