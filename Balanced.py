"""
----------- Link for the challenge: https://codeforces.com/contest/1850/problem/D ----------
You are the author of a Codeforces round and have prepared n 
problems you are going to set, problem i having difficulty a(i). 
You will do the following process:

remove some (possibly zero) problems from the list;
rearrange the remaining problems in any order you wish.
A round is considered balanced if and only if the absolute difference between the 
difficulty of any two consecutive problems is at most k (less or equal than k).

What is the minimum number of problems you have to remove so that an arrangement of problems is balanced?

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains two positive integers n (1 ≤ n ≤ 2⋅10^5) and
k (1 ≤ k ≤ 10^9) — the number of problems, and the maximum allowed absolute difference 
between consecutive problems.

The second line of each test case contains n space-separated integers a(i) (1 ≤ a(i) ≤ 10^9)
— the difficulty of each problem.

Note that the sum of n over all test cases doesn't exceed 2⋅10^5.

Output
For each test case, output a single integer — the minimum number of problems you have to 
remove so that an arrangement of problems is balanced.

"""
cases = int(input())
for i in range(cases):
    sze, diff = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    longest = 1
    tempLongest = 1
    for j in range(sze - 1):
        first = lst[j]
        second = lst[j + 1]
        temp = second - first
        if(temp <= diff):
            tempLongest += 1
        else:
            if(tempLongest > longest):
                longest = tempLongest
            tempLongest = 1
    if(tempLongest > longest):
                longest = tempLongest
                tempLongest = 1
    print(abs(sze - longest))