"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1189/A -----------

After playing Neo in the legendary "Matrix" trilogy, Keanu Reeves started doubting himself: 
maybe we really live in virtual reality? To find if this is true, he needs to solve the following problem.

Let's call a string consisting of only zeroes and ones good if it contains different numbers of zeroes and ones. 
For example, 1, 101, 0000 are good, while 01, 1001, and 111000 are not good.

We are given a string s of length n consisting of only zeroes and ones. 
We need to cut s into minimal possible number of substrings s1,s2,…,sk such that all of them are good. 
More formally, we have to find minimal by number of strings sequence of good strings s1,s2,…,sk such that their concatenation (joining) equals s, i.e. s1+s2+⋯+sk=s.

For example, cuttings 110010 into 110 and 010 or into 11 and 0010 are valid, as 110, 010, 11, 0010 are all good, 
and we can't cut 110010 to the smaller number of substrings as 110010 isn't good itself. 
At the same time, cutting of 110010 into 1100 and 10 isn't valid as both strings aren't good. 
Also, cutting of 110010 into 1, 1, 0010 isn't valid, as it isn't minimal, even though all 3 strings are good.

Can you help Keanu? We can show that the solution always exists. If there are multiple optimal answers, print any.

Input
The first line of the input contains a single integer n (1 ≤ n ≤ 100) — the length of the string s.

The second line contains the string s of length n consisting only from zeros and ones.

Output
In the first line, output a single integer k (1 ≤ k ) — a minimal number of strings you have cut s into.

In the second line, output k strings s1,s2,…,sk separated with spaces. The length of each string has to be positive. 
Their concatenation has to be equal to s and all of them have to be good.

If there are multiple answers, print any.


Input:
1
1

Output:
1
1

"""

n = int(input())
s = input()
arr = []
founded = False
zeros = s.count('0')
ones = s.count('1')
if(zeros == ones):
    while not founded:
        last_char = s[-1]
        remaining_string = s[:-1]
        s = remaining_string
        zeros = s.count('0')
        ones = s.count('1')
        if(zeros != ones):
            founded = True
        arr.append(last_char)
    print(len(arr) + 1)
    ans = s
    for i in range(len(arr) - 1, -1, -1):
        ct = arr[i]
        ans += " "
        ans += ct
    print(ans)
else:
    print(1)
    print(s)