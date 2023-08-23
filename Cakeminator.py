"""
------- Link for the challenge: https://codeforces.com/problemset/problem/330/A ---------

You are given a rectangular cake, represented as an r × c grid. 
Each cell either has an evil strawberry, or is empty. 
For example, a 3 × 4 cake may look as follows:

The cakeminator is going to eat the cake! Each time he eats, he chooses a row or a column that does 
not contain any evil strawberries and contains at least one cake cell that has not been eaten before, 
and eats all the cake cells there. He may decide to eat any number of times.

Please output the maximum number of cake cells that the cakeminator can eat.

Input
The first line contains two integers r and c (2 ≤ r, c ≤ 10), 
denoting the number of rows and the number of columns of the cake. 
The next r lines each contains c characters — the j-th character of the i-th line denotes the content of 
the cell at row i and column j, and is either one of these:

'.' character denotes a cake cell with no evil strawberry;
'S' character denotes a cake cell with an evil strawberry.

Output
Output the maximum number of cake cells that the cakeminator can eat.

Input:
3 4
S...
....
..S.

Output:
8
"""
r, c = map(int, input().split())
arr = []
rows = 0
cols = 0
for i in range(r):
    rowTemp = input()
    if(rowTemp.count('S') >= 1):
        arr.append(rowTemp)
    else:
        rows += 1
for j in range(c):
    col = True
    for l in range(len(arr)):
        ch = arr[l][j]
        if(ch == 'S'):
            col = False
            break
    if(col):
        cols += 1
ans = (rows * c) + (cols * len(arr))
print(ans)