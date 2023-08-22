"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1611/A --------

Polycarp has an integer n that doesn't contain the digit 0. 
He can do the following operation with his number several (possibly zero) times:

Reverse the prefix of length l (in other words, l leftmost digits) of n. 
So, the leftmost digit is swapped with the l-th digit from the left, the second digit from the left swapped with (l−1)-th left, etc. 
For example, if n=123456789 and l = 5, then the new value of n will be 543216789.

Note that for different operations, the values of l can be different. 
The number l can be equal to the length of the number n — in this case, the whole number n is reversed.

Polycarp loves even numbers. Therefore, he wants to make his number even. 
At the same time, Polycarp is very impatient. He wants to do as few operations as possible.

Help Polycarp. Determine the minimum number of operations he needs to perform with 
the number n to make it even or determine that this is impossible.

You need to answer t independent test cases.

Input
The first line contains the number t (1 ≤ t ≤ 10^4) — the number of test cases.

Each of the following t lines contains one integer n (1 ≤ n < 10^9). 
It is guaranteed that the given number doesn't contain the digit 0.

Output
Print t lines. On each line print one integer — the answer to the corresponding test case. 
If it is impossible to make an even number, print -1.

Input:
4
3876
387
4489
3

Output:
0
2
1
-1

"""
cases = int(input())
for i in range(cases):
    tempStr = input()
    tempNum = int(tempStr)
    firstDig = int(tempStr[0])
    lastDig = int(tempStr[len(tempStr) - 1])
    founded = False
    if(lastDig % 2 == 0):
        print(0)
    else:
        if(firstDig % 2 == 0):
            print(1)
        else:  
            while(tempNum > 0):
                dig = tempNum % 10
                tempNum = tempNum // 10
                if(dig % 2 == 0):
                    founded = True
                    break
            if(not founded):
                print(-1)
            else:
                print(2)