"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1681/A -----------
Alice and Bob play a game. Alice has n cards, the i-th of them has the integer a(i) written on it. 
Bob has m cards, the j-th of them has the integer b(j) written on it.

On the first turn of the game, the first player chooses one of his/her cards and puts it on the table (plays it).
On the second turn, the second player chooses one of his/her cards such that the integer on it is greater than 
the integer on the card played on the first turn, and plays it. On the third turn, the first player chooses 
one of his/her cards such that the integer on it is greater than the integer on the card played on the 
second turn, and plays it, and so on — the players take turns, and each player has to choose one of his/her 
cards with greater integer than the card played by the other player on the last turn.

If some player cannot make a turn, he/she loses.

For example, if Alice has 4 cards with numbers [10,5,3,8], and Bob has 3 cards with numbers [6,11,6], 
the game may go as follows:

Alice can choose any of her cards. She chooses the card with integer 5 and plays it.

Bob can choose any of his cards with number greater than 5. 
He chooses a card with integer 6 and plays it.

Alice can choose any of her cards with number greater than 6. 
She chooses the card with integer 10 and plays it.
Bob can choose any of his cards with number greater than 10. 
He chooses a card with integer 11 and plays it.
Alice can choose any of her cards with number greater than 11, but she has no such cards, so she loses.
Both Alice and Bob play optimally (if a player is able to win the game no matter how the other player plays, 
the former player will definitely win the game).

You have to answer two questions:
1. who wins if Alice is the first player?
2. who wins if Bob is the first player?

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases. 
Each test case consists of four lines.

The first line of a test case contains one integer n (1 ≤ n ≤ 50) — the number of cards Alice has.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 50) — the numbers written on the cards that Alice has.

The third line contains one integer m (1 ≤ m ≤ 50) — the number of Bob's cards.

The fourth line contains m integers b1,b2,…,bm (1 ≤ b(i) ≤ 50) — the numbers on Bob's cards.

Output
For each test case, print two lines. The first line should be Alice if Alice wins when she is the first player; 
otherwise, the first line should be Bob. 
The second line should contain the name of the winner if Bob is the first player, in the same format.

Input:
4
1
6
2
6 8
4
1 3 3 7
2
4 2
1
50
2
25 50
10
1 2 3 4 5 6 7 8 9 10
2
5 15

Output:
Bob
Bob
Alice
Alice
Alice
Bob
Bob
Bob
"""
cases = int(input())
for i in range(cases):
    alices = int(input())
    lstAlices = sorted(list(map(int, input().split())))
    bobs = int(input())
    lstBobs = sorted(list(map(int, input().split())))
    aliceBiggest = lstAlices[alices - 1]
    bobsBiggest = lstBobs[bobs - 1]
    if(aliceBiggest == bobsBiggest):
        print("Alice")
        print("Bob")
    elif(aliceBiggest > bobsBiggest):
        print("Alice")
        print("Alice")
    else:
        print("Bob")
        print("Bob")