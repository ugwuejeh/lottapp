import random

def lottery_pool():
    while 1:

          Username = input("Enter your name here ")
          User_number = int(input("Choose a number between 0 and 50: "))
          winning_number = 30


         #  Check if the number is not greater than 50
          if User_number > 50:
             print("You are disqualified!!!. You didnt choose a number between 0 and 50.")
          else:
    # Generate a random number for the lottery
             User_number = random.randint(0, 50)
    
    # Check if the user won the lottery
             if User_number == winning_number:
               print("Congratulations, you won the lottery!",winning_number)
             
             else:
               print("Sorry, you didn't win the lottery. Your randomly generated number is", User_number,)
          break



  
lottery_pool()