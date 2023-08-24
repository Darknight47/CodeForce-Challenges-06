"""
-------------- Link for the challenge: https://codeforces.com/problemset/problem/1065/A ----------

There is a special offer in Vasya's favourite supermarket: if the customer buys a chocolate bars, 
he or she may take b additional bars for free. This special offer can be used any number of times.

Vasya currently has s roubles, and he wants to get as many chocolate bars for free. 
Each chocolate bar costs c roubles. Help Vasya to calculate the maximum possible number 
of chocolate bars he can get!

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of testcases.

Each of the next t lines contains four integers s,a,b,c (1 ≤ s,a,b,c ≤ 10^9) — the number of roubles Vasya has, 
the number of chocolate bars you have to buy to use the special offer, the number of bars you get for free, 
and the cost of one bar, respectively.

Output
Print t lines. i-th line should contain the maximum possible number of chocolate bars Vasya can get in i-th test.

Input:
2
10 3 1 1
1000000000 1 1000000000 1

Output:
13
1000000001000000000
"""
cases = int(input())
for i in range(cases):
    money, lim, free, cost = map(int, input().split())
    totalBuy = money // cost
    amountForGettingFreeB = totalBuy // lim
    freebees = free * amountForGettingFreeB
    ans = totalBuy + freebees
    print(ans)
    