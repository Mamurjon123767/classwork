import random 
import time
print("---Welcome to dice game---")
print("get ready")
for i in range(3, 0, -1):
    print(i)
    time.sleep(2)
print("go")
player1_score = 0
player2_score = 0
rounds = int(input("How many rounds do you want the players to play "))
for i in range(1, round + 1):
    print("/n---round{i}---")
    input("player 1 press enter to role the dice")
    roll1 = random.radiant(1, 6)
    print("player 1 rolled:", roll1)
    player1_score += roll1
    input("player 2 press enter to role the dice")
    roll2 = random.radiant(1, 6)
    print("player 2 rolled:", roll2)
    player2_score += roll2
print("/n final score")
print("player 1's total score: ", player1_score)
print("player 2's :", player2_score )
if player1_score > player2_score:
    print("player1 wins")
elif player2_score > player1_score:
    print("palyer2 wins")
else:
    print("its a tie ")

