import random
def user():
    print("chose one 'ROCK','PAPER',SCISSOR'")
    choice=input("your choice:").lower()
    if choice in ['rock','paper','scissor']:
        return choice
    else:
        print("select only in 'rock,'paper,'scissor'")
    return user()
def computer_choice():
    return random.choice(['rock','paper','scissor'])
def win_lose(user_choice,computer):
    if user_choice==computer:
        return "It was a tie"
    elif (user_choice=='rock' and computer=='paper') or (user_choice=='paper' and computer=='scissor') or (user_choice=='scissor' and computer=='rock'):
        return "COMPUTER WINS!!"
    else:
        return "USER WINS!!!!"
user_choice=user()
computer=computer_choice()
print(f"you choosed--{user_choice}")
print(f"computer choice-- {computer}")
result=win_lose(user_choice,computer)
print(result)