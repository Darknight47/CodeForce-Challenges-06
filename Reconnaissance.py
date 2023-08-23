"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/34/A ----------

n soldiers stand in a circle. For each soldier his height ai is known. 
A reconnaissance unit can be made of such two neighbouring soldiers, whose heights 
difference is minimal, i.e. |ai - aj| is minimal. So each of them will be less noticeable with the other. 
Output any pair of soldiers that can form a reconnaissance unit.

Input
The first line contains integer n (2 ≤ n ≤ 100) — amount of soldiers. 
Then follow the heights of the soldiers in their order in the circle — n space-separated 
integers a1, a2, ..., an (1 ≤ ai ≤ 1000). The soldier heights are given in clockwise or counterclockwise direction.

Output
Output two integers — indexes of neighbouring soldiers, who should form a reconnaissance unit. 
If there are many optimum solutions, output any of them. Remember, that the soldiers stand in a circle.

Input:
5
10 12 13 15 10

Output:
5 1
"""
sze = int(input())
lst = list(map(int, input().split()))
diff = abs(lst[0] - lst[sze - 1])
ans = f"{1} {sze}"
for i in range(sze - 1):
    first = lst[i]
    second = lst[i + 1]
    diffTemp = abs(first - second)
    if(diffTemp < diff):
        diff = diffTemp
        ans = f"{i + 1} {i + 2}"
print(ans)