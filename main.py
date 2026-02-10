import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
total = dice1 + dice2
print(f'Your Dice : {dice1} and {dice2}')

if total == 7 or total == 11:
    print("Players Wins")
elif total ==2 or total ==3 or total == 12:
    print("Casino Wins")
else:
    goal = total
    while True:
     dice1 = random.randint(1,6)
     dice2 = random.randint(1,6)
     print(f'Your Dice : {dice1} and {dice2}')
     total = dice1 + dice2
     if total == goal:
        print("PLayer wins")
        break
     if total == 7:
        print("casino wins")
        break
