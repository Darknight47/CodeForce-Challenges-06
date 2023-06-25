"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/454/A -----------

Twilight Sparkle once got a crystal from the Crystal Mine. 
A crystal of size n (n is odd; n > 1) is an n × n matrix with a diamond inscribed into it.

You are given an odd integer n. You need to draw a crystal of size n. 
The diamond cells of the matrix should be represented by character "D". 
All other cells of the matrix should be represented by character "*". 
Look at the examples to understand what you need to draw.

Input
The only line contains an integer n (3 ≤ n ≤ 101; n is odd).

Output
Output a crystal of size n.

Input:
3

Output:
*D*
DDD
*D*

"""
n = int(input())
half = (n + 1) // 2
stars = half - 1
ds = 1
for i in range(n//2):
    sTemp = '*' * stars
    sTemp += 'D' * ds
    sTemp += '*' * stars
    stars -= 1
    ds += 2
    print(sTemp)
print('D' * ds)
stars = 1
ds = n - 2
for j in range(n//2):
    tempStr = '*' * stars
    tempStr += 'D' * ds
    tempStr += '*' * stars
    stars += 1
    ds -= 2
    print(tempStr)
