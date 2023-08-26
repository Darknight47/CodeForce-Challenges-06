"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/999/A ---------

Mishka started participating in a programming contest. There are n
problems in the contest. Mishka's problem-solving skill is equal to k.

Mishka arranges all problems from the contest into a list. 
Because of his weird principles, Mishka only solves problems from one of the ends of the list. 
Every time, he chooses which end (left or right) he will solve the next problem from. 
Thus, each problem Mishka solves is either the leftmost or the rightmost problem in the list.

Mishka cannot solve a problem with difficulty greater than k. 
When Mishka solves the problem, it disappears from the list, so the length of the list decreases by 1. 
Mishka stops when he is unable to solve any problem from any end of the list.

How many problems can Mishka solve?

Input
The first line of input contains two integers n and k (1 ≤ n,k ≤ 100) 
— the number of problems in the contest and Mishka's problem-solving skill.

The second line of input contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 100), 
where a(i) is the difficulty of the i-th problem. The problems are given in order 
from the leftmost to the rightmost in the list.

Output
Print one integer — the maximum number of problems Mishka can solve.

Input:
8 4
4 2 3 1 5 1 6 4

Output:
5
"""
sze, k = map(int, input().split())
lst = list(map(int, input().split()))
leftSide = 0
rightSide = 0
rightEnd = -1
for i in range(sze):
    temp = lst[i]
    rightEnd = i
    if(temp <= k):
        leftSide += 1
    else:
        break
for j in range(sze - 1, rightEnd, -1):
    temp = lst[j]
    if(temp <= k):
        rightSide += 1
    else:
        break
print(leftSide + rightSide)
        