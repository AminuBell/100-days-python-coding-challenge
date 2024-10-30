import random
from art import logo, vs    
from game_data import data
 

def format_data(account):
    """" formating the account in to printable format """
    account_name = account["name"]
    account_descr = account["description"]
    country = account["country"]
    return f"{account_name}, a {account_descr}, from {country}"


def check_answer(a_account_followers,b_account_follower,guess):
    """checking who has more followers """
    if a_account_followers > b_account_follower:
        return guess == "a"
    else:
        return guess == "b"


#score tracker
score = 0

#game switch
game_should_continue = True

#getting random account form data file
b_account = random.choice(data)


#game switch is on
while game_should_continue:


    #Display art (logo)
    print(logo)


    #select random accounts from game data and making sure Both a & b aren't the same 
    a_account = b_account
    b_account = random.choice(data)
    while a_account == b_account:
        b_account = random.choice(data)
   
    #printing a_account details
    print(f"Compare A: {format_data(a_account)}")
    
    
    #Display (VS) art
    print(vs) 
    

    #printing b_account details
    print(f"Against B: {format_data(b_account)}")


    #ask user to guess or to input guess
    guess = input("Who has more followers? A or B: ").lower()


    # getting followers of each account
    a_account_followers = a_account["follower_count"]
    b_account_follower = b_account["follower_count"]


    #checking aswer of who has more followers
    is_correct = check_answer( a_account_followers,b_account_follower, guess)


    #giving user feedback after guess
    if is_correct:
        score +=1
        print(f"you got it right your current score is {score}")
    else:
        game_should_continue = False
        print(f"sorry!, thats wrong your final score is {score}")





