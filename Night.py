"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/595/A ----------------

One day Vitaly was going home late at night and wondering: how many people aren't sleeping at that moment? 
To estimate, Vitaly decided to look which windows are lit in the house he was passing by at that moment.

Vitaly sees a building of n floors and 2·m windows on each floor. On each floor there are m flats numbered 
from 1 to m, and two consecutive windows correspond to each flat. If we number the windows from 1 to 2·m from 
left to right, then the j-th flat of the i-th floor has windows 2·j - 1 and 2·j in the corresponding row of windows 
(as usual, floors are enumerated from the bottom). 
Vitaly thinks that people in the flat aren't sleeping at that moment if at least one of the windows 
corresponding to this flat has lights on.

Given the information about the windows of the given house, your task is to calculate the number of flats where, 
according to Vitaly, people aren't sleeping.

Input
The first line of the input contains two integers n and m (1 ≤ n, m ≤ 100) — the number of floors in the 
house and the number of flats on each floor respectively.

Next n lines describe the floors from top to bottom and contain 2·m characters each. 
If the i-th window of the given floor has lights on, then the i-th character of this line is '1', otherwise it is '0'.

Output
Print a single integer — the number of flats that have lights on in at least one window, 
that is, the flats where, according to Vitaly, people aren't sleeping.

Input:
2 2
0 0 0 1
1 0 1 1

Output:
3
"""
n, m = map(int, input().split())
ans = 0
for i in range(n):
    tempLst = list(map(int, input().split()))
    indx = 0
    for j in range(indx, len(tempLst) // 2):
        if(indx >= len(tempLst)):
            break
        first = tempLst[indx]
        second = tempLst[indx + 1]
        if(first == 1 or second == 1):
            ans += 1
        indx += 2
print(ans)