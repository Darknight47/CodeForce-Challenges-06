"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1207/A ------
There are two types of burgers in your restaurant — hamburgers and chicken burgers! 
To assemble a hamburger you need two buns and a beef patty. 
To assemble a chicken burger you need two buns and a chicken cutlet.

You have b buns, p beef patties and f chicken cutlets in your restaurant. 
You can sell one hamburger for h dollars and one chicken burger for c dollars. 
Calculate the maximum profit you can achieve.

You have to answer t independent queries.

Input
The first line contains one integer t (1 ≤ t ≤ 100) – the number of queries.

The first line of each query contains three integers b, p and f (1 ≤ b, p, f ≤ 100) 
— the number of buns, beef patties and chicken cutlets in your restaurant.

The second line of each query contains two integers h and c (1 ≤ h, c ≤ 100) 
— the hamburger and chicken burger prices in your restaurant.

Output
For each query print one integer — the maximum profit you can achieve.

Input:
3
15 2 3
5 10
7 5 2
10 12
1 100 100
100 100

Output:
40
34
0
"""
cases = int(input())
for i in range(cases):
    buns, beefPatties, chickenCutlets = map(int, input().split())
    burgerPrice, chickenPrice = map(int, input().split())
    if(buns % 2 == 1):
        buns -= 1
    breads = buns // 2
    ans = 0
    if(burgerPrice >= chickenPrice):
        burgers = min(breads, beefPatties)
        breads -= burgers
        chickens = min(breads, chickenCutlets)
        ans = (burgers * burgerPrice) + (chickens * chickenPrice)
    else:
        chickens = min(breads, chickenCutlets)
        breads -= chickens
        burgers = min(breads, beefPatties)
        ans = (burgers * burgerPrice) + (chickens * chickenPrice)
    print(ans)        