"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/381/A ------------

Sereja and Dima play a game. The rules of the game are very simple. The players have n cards in a row. 
Each card contains a number, all numbers on the cards are distinct. The players take turns, Sereja moves first. 
During his turn a player can take one card: either the leftmost card in a row, or the rightmost one. 
The game ends when there is no more cards. The player who has the maximum sum of numbers on his cards by 
the end of the game, wins.

Sereja and Dima are being greedy. Each of them chooses the card with the larger number during his move.

Inna is a friend of Sereja and Dima. She knows which strategy the guys are using, so she wants to determine 
the final score, given the initial state of the game. Help her.

Input
The first line contains integer n (1 ≤ n ≤ 1000) — the number of cards on the table. 
The second line contains space-separated numbers on the cards from left to right. 
The numbers on the cards are distinct integers from 1 to 1000.

Output
On a single line, print two integers. The first number is the number of Sereja's points at the end of the game, 
the second number is the number of Dima's points at the end of the game.

Input:
4
4 1 2 10

Output:
12 5

"""
sze = int(input())
lst = list(map(int, input().split()))
diff = sze
lastIndx = sze - 1
firstIndx = 0
sereja = 0
dima = 0
serejaChance = True
dimaChance = False
while diff >= 0:
    lastElem = lst[lastIndx]
    firstElem = lst[firstIndx]
    addedElem = 0
    if(lastElem > firstElem):
        lastIndx -= 1
        addedElem = lastElem
    else:
        firstIndx += 1
        addedElem = firstElem
    if(serejaChance):
        sereja += addedElem
        serejaChance = False
        dimaChance = True
    else:
        dima += addedElem
        dimaChance = False
        serejaChance = True
    diff = lastIndx - firstIndx
print(sereja, dima)