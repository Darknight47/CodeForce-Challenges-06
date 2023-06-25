"""
You are given a string s of length n, which consists only of the first k
letters of the Latin alphabet. All letters in string s are uppercase.

A subsequence of string s is a string that can be derived from s by deleting
some of its symbols without changing the order of the remaining symbols. 
For example, "ADE" and "BD" are subsequences of "ABCDE", but "DEA" is not.

A subsequence of s called good if the number of occurences of 
each of the first k letters of the alphabet is the same.

Find the length of the longest good subsequence of s.

Input
The first line of the input contains integers n (1 ≤ n ≤ 10^5) and k (1 ≤ k ≤ 26).

The second line of the input contains the string s of length n. 
String s only contains uppercase letters from 'A' to the k-th letter of Latin alphabet.

Output
Print the only integer — the length of the longest good subsequence of string s.

Input:
9 3
ACAABCCAB

Output:
6
"""

from collections import Counter
n, k = map(int, input().split())
lst = list(input())
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ok = True
ans = 0
for i in range(k):
    c = alphabet[i]
    if(lst.count(c) <= 0):
        ok = False
        break
if(ok):
    tempSet = set(lst)
    count = Counter(lst)
    min_count = min(count.values())
    ans = min_count * len(tempSet)
print(ans)
        