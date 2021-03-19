import random

def play():
    user = input("what's your choice? choki for c, goo for g, paa for p\n")
    computer = random.choice(['c', 'g', 'p'])

    ##あいこの時
    if user == computer:
        return "aiko!!!!"

    ##trueの時だけreturn
    if judge_winner(user, computer):
        return "You Win!!!"

    return "You Lose!!!"    

##勝った時にtrueを返す
def judge_winner(player, opponent):
    if (player == 'c' and opponent == 'p') or (player == 'p' and opponent == 'g') or (player =='g' and opponent == 'c'):
       return True

print(play())
