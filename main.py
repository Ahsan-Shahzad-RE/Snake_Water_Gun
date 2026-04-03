'''
-1 for water
0 for gun
1 for snake
'''
# print("Welcome to the Snake , Water , Gun Game " )

import random 
computer = random.choice([-1 , 0 , 1])

your_string = input("Enter your choice :")
your_dict = {"s" : 1 , "w" : -1 , "g" : 0}

reverse_dict = {1 : "snakes" , -1 : "water" , 0 : "gun"}

you = your_dict[your_string]

print(f"you chose {reverse_dict[you]}\ncomputer chose {reverse_dict[computer]}")

#snake drinks water -- snake wins 
#water drowns gun -- water wins 
#gun kills snake -- gun wins 

if computer == you :
    print("it's a draw")

else :
    if computer == -1 and you == 0:
            print("you win!")
    elif computer == 0 and you == 1:
            print("you lose!")
    elif computer == -1 and you == 1:
            print("you win!")
    elif computer == 1 and you == -1:
            print("you lose!")
    elif computer == 0 and you == -1:
            print("you lose!")
    elif computer == 1 and you == 0:
            print("you win!")
   
    else :
           print("something went wrong 😑")


#there is a concept COMPUTER - YOU , we can use this statment to minimize the if statements 

