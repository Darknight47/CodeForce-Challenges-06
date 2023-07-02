"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1440/A -----------

You are given four integers n, c0, c1 and h and a binary string s of length n.

A binary string is a string consisting of characters 0 and 1.

You can change any character of the string s (the string should be still binary after the change). 
You should pay h coins for each change.

After some changes (possibly zero) you want to buy the string. To buy the string you should buy all its characters. 
To buy the character 0 you should pay c0 coins, to buy the character 1 you should pay c1 coins.

Find the minimum number of coins needed to buy the string.

Input
The first line contains a single integer t(1 ≤ t ≤10) — the number of test cases. Next 2tlines contain descriptions of test cases.

The first line of the description of each test case contains four integers n, c0, c1, h(1 ≤ n,c0,c1,h ≤ 1000).

The second line of the description of each test case contains the binary string s of length n.

Output
For each test case print a single integer — the minimum number of coins needed to buy the string.

Input:
6
3 1 1 1
100
5 10 100 1
01010
5 10 1 1
11111
5 1 10 1
11111
12 2 1 10
101110110101
2 100 1 10
00

Output:
3
52
5
10
16
22

"""

cases = int(input())
for i in range(cases):
    n, c0, c1, h = map(int, input().split())
    s = list(input())
    tempLst = []
    numberOfOnes = s.count('1')
    numberOfZeros = s.count('0')
    buyWithoutChanged = (numberOfOnes * c1) + (numberOfZeros * c0)
    tempLst.append(buyWithoutChanged)
    #change ones to zeros
    tempNumOfZeros = numberOfOnes + numberOfZeros
    tempCostOfChanges = numberOfOnes * h
    buyWithOnesChanged = (tempNumOfZeros * c0) + tempCostOfChanges
    tempLst.append(buyWithOnesChanged)
    #change zeros to ones
    tempNumOfOnes = numberOfOnes + numberOfZeros
    tempCostOfChanges = numberOfZeros * h
    buyWithZerosChanged = (tempNumOfOnes * c1) + tempCostOfChanges
    tempLst.append(buyWithZerosChanged)
    #change ones to zeros and zeros to ones
    tempZeros = numberOfOnes
    tempOnes = numberOfZeros
    tempCostOfChange = (tempZeros * h) + (tempOnes * h)
    buyWithBothChanged = (tempZeros * c0) + (tempOnes * c1) + tempCostOfChange
    tempLst.append(buyWithBothChanged)
    tempLst = sorted(tempLst)
    print(tempLst[0])
