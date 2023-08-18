"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1651/A --------

Consider a playoff tournament where 2n athletes compete. 
The athletes are numbered from 1 to 2n.

The tournament is held in n stages. 
In each stage, the athletes are split into pairs in such a way that each athlete belongs 
exactly to one pair. In each pair, the athletes compete against each other, and exactly 
one of them wins. The winner of each pair advances to the next stage, the athlete who was 
defeated gets eliminated from the tournament.

The pairs are formed as follows:

in the first stage, athlete 1 competes against athlete 2; 3 competes against 4; 
5 competes against 6, and so on; in the second stage, the winner of the match "1–2" 
competes against the winner of the match "3–4"; the winner of the match "5–6" competes 
against the winner of the match "7–8", and so on;
the next stages are held according to the same rules.
When athletes x and y compete, the winner is decided as follows:

if x+y is odd, the athlete with the lower index wins (i. e. if x < y, then x wins, otherwise y wins);
if x + y is even, the athlete with the higher index wins. 
The following picture describes the way the tournament with n=3 goes.

Input:
2
3
1

Output:
7
1
"""

cases = int(input())
for i in range(cases):
    sze = int(input())
    ans = 2 ** sze
    print(ans - 1)