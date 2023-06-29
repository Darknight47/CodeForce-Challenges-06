"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1807/B -----------

Mihai and Bianca are playing with bags of candies. 
They have a row a of n bags of candies. The i-th bag has a(i)candies.
The bags are given to the players in the order from the first bag to the n-th bag.

If a bag has an even number of candies, Mihai grabs the bag. Otherwise, Bianca grabs the bag.
Once a bag is grabbed, the number of candies in it gets added to the total number of candies of
the player that took it.

Mihai wants to show off, so he wants to reorder the array so that at any moment 
(except at the start when they both have no candies), Mihai will have strictly more 
candies than Bianca. Help Mihai find out if such a reordering exists.

Input
The first line of the input contains an integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of bags in the array.

The second line of each test case contains n space-separated integers a(i) 
(1 ≤ a(i) ≤100) — the number of candies in each bag.

Output
For each test case, output "YES" (without quotes) if such a reordering exists, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES"
will be recognized as a positive answer).

Input:
3
4
1 2 3 4
4
1 1 1 2
3
1 4 3

Output:
YES
NO
NO
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    even = 0
    odd = 0
    for j in range(sze):
        if(lst[j] % 2 == 0):
            even += lst[j]
        elif(lst[j] % 2 == 1):
            odd += lst[j]
    if(even > odd):
        print("YES")
    else:
        print("NO")