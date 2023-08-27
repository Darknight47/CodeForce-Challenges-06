"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/1583/A ---------

A bow adorned with nameless flowers that bears the earnest hopes of an equally nameless person.

You have obtained the elegant bow known as the Windblume Ode. 
Inscribed in the weapon is an array of n (n ≥ 3) 
positive distinct integers (i.e. different, no duplicates are allowed).

Find the largest subset (i.e. having the maximum number of elements) of this array such that its sum is a composite number. 
A positive integer x is called composite 
if there exists a positive integer y such that 1 < y < x and x is divisible by y.

If there are multiple subsets with this largest size with the composite sum, you can output any of them. 
It can be proven that under the constraints of the problem such a non-empty subset always exists.

Input
Each test consists of multiple test cases. 
The first line contains the number of test cases t (1 ≤ t ≤ 100). 
Description of the test cases follows.

The first line of each test case contains an integer n (3 ≤ n ≤ 100) — the length of the array.

The second line of each test case contains n distinct integers 
a1,a2,…,an (1 ≤ a(i) ≤ 200) — the elements of the array.

Output
Each test case should have two lines of output.

The first line should contain a single integer x: the size of the largest subset with composite sum. 
The next line should contain x space separated integers representing the indices of the subset of the initial array.

Input:
4
3
8 1 2
4
6 9 4 2
9
1 2 3 4 5 6 7 8 9
3
200 199 198

Output:
2
2 1
4
2 1 4 3
9
6 9 1 2 3 4 5 7 8
3
1 2 3 
"""
cases = int(input())
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    founded = False
    indx = sze - 1
    totalSum = sum(lst)
    if(not is_prime(totalSum)):
        print(sze)
        for j in range(sze):
            print(j + 1, end=' ')
    else:
        ans = ""
        oddFounded = False
        for n in range(sze):
            temp = lst[n]
            if(temp % 2 == 1 and not oddFounded):
                oddFounded = True
            else:
                ans += str(n + 1) + " "
        print(sze - 1)
        print(ans)
    