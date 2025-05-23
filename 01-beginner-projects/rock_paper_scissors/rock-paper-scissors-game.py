## Acknowledgements
# - Dr. Angela Yu and the App Brewery team for the course content and project inspiration
# - This project is completed as part of the "100 Days of Code: The Complete Python Pro Bootcamp"
# - This project represents my personal interpretation of the exercise instructions provided in the course.



import random

# OBNOXIOUS ASCII ART FOR ROCK/PAPER/SCISSORS

rock = '''                                                       
                                *#%#%%#%                
                              +%=      .#*.             
                           .%##          *##            
            ..............=##              +#+          
         .+%##%#%%#%%#%##%###*               %*:        
       .%*                                     :%.      
      =##                                       %*      
   ..%=: =-=-:#        -                        -#.     
  .#*  *:       :#*#  .+                        :*.     
  ## +#               .*                        +*.     
  %- %     =          =.                       =%:      
  #+ %      .-#+=    +:   'ROCK'             .##.       
   .-@           ....                       #+...       
    .%#+                                * ##=. ..       
     .## =** =                          *#+......      .
      **       .+*-                     **              
      **            ***                 #*. .           
       :@  .-                         :#:..             
       .@     ++#:.                 :%+.                
       .*#*        ++=             *+...                
        .+#  *#+                 ##..                   
     ....+#-      *#:          =#*..                    
          ..-*%*:            .#.                        
            ....+#*%#-      %*:.                        
             ........:-=*%#*:..                         
                      . ....                            
                        ....                            
'''

paper = '''                            
                                    .:%. +#% :.         
                       .............**      -##*+.      
                    .+*                            =*#. 
                   .%=                                % 
                 :%:                                  % 
                +#.      ::                          .%.
               #:       #                            *# 
              .%      -%                           :**. 
               #*   #=                            %+..  
               .=*%#         'PAPER'          + ##:..   
               .*#.                           =#:       
             .##=                             +*..      
            :##                              .#=        
           #:                               %-.         
         *%        %                      :%..          
      .:%.       *.                      *:..           
     .*+       *-       #:      .      %#.              
   .%:       ..       :.      #      #*.                
  :%:      .*:      :*      :%     +#+.                 
 .#       #        %      :+      %.                    
 -#     :%       =*      *:     *#.                     
  +%#  .%       +       %     %*.                       
  ..=++*%     =%#     -#%-  =#+..                       
       .:#%**%#.*#+  #+..:+*.                           
        ....-....:=*+:........                                                             
'''

scissors = '''
                                      ......            
                                    .*######+           
                                  +#:       .%*         
                         ....... %.           .%        
                       +#%%%%%%%%#*             %#      
                     +#                           %*    
                   =*                              %.   
                 =#-      ..                       %:   
                .#       .#                        %.   
                -#  +++                           %*    
          .. %%#---             'SCISSORS'      @*:..   
        .*%%#                               : :%+..     
    :%#.                                    :%* . .     
    :#               +  .*                  :#....      
    -%         -###   :*#                   #+...       
     *%#..:%%*:.-#   :+                   *#.           
                .# -.       -.          =*.             
              ...#*        *          -*=...            
               +#        ##=         #+.                
             *#        *#  :       #-.                  
            %:       .*:  -+#%   %-...                  
           %.      .*+.      .+##:..                    
           %.    .#=.                                   
           ..*###-.                                 
'''

draw = '''
█████╗ ██████╗  █████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔══██╗██║    ██║
██║  ██║██████╔╝███████║██║ █╗ ██║
██║  ██║██╔══██╗██╔══██║██║███╗██║
██████╔╝██║  ██║██║  ██║╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ 
'''

win = '''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝                                                        
'''

lose = '''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝
'''

computer_chose_ascii = '''

▀█▀ █ █ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █ █ ▀█▀ █▀▀ █▀█   █▀▀ █ █ █▀█ █▀ █▀▀ 
 █  █▀█ █▀▀   █   █ █ █ ▀ █ █▀▀ █ █  █  █▀▀ █▀▄   █   █▀█ █ █ ▀▀ █▀▀ 
 ▀  ▀ ▀ ▀▀▀   ▀▀▀ ▀▀▀ ▀   ▀ ▀   ▀▀▀  ▀  ▀▀▀ ▀ ▀   ▀▀▀ ▀ ▀ ▀▀▀ ▀▀ ▀▀▀ ▀ ▀ ▀   

'''



# Introduce the game to the player
print("Welcome to Rock, Paper, Scissors!")
print("Can you beat the computer?")

# Get user's choice
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Print user selection with visual separator
print("==============================================================================")
print("YOU CHOSE:")

# Display user's choice and check if it's valid
if user_selection == 0:
    print("==============================================================================")
    print(rock)

elif user_selection == 1:
    print("==============================================================================")
    print(paper)

elif user_selection == 2:
    print("==============================================================================")
    print(scissors)

else:
    print("Invalid selection. Please choose 0, 1, or 2.")


# Possible choices for the CPU
# I did a list instead of random.randint(0,2) like Dr. Angela Yu had did so the if/elif/else statements were easier to read.
# She used a list only to print the ASCII art
# I think this implementation is better on the eyes, but it may use more lines of code.

game_list = ["rock", "paper", "scissors"]

# CPU randomly selects one option
computer_choice = random.choice(game_list)


# Game logic
# Check for all possibilities


# User selects '0' (rock)
if user_selection == 0 and computer_choice == "rock":
    # USER: 0 CPU: rock (DRAW)
    print(computer_chose_ascii)
    print(rock)
    print(draw)

elif user_selection == 0 and computer_choice == "paper":
    # USER: 0 CPU: paper (USER loses, Rock loses to paper)
    print(computer_chose_ascii)
    print(paper)
    print(lose)

elif user_selection == 0 and computer_choice == "scissors":
    # USER: 0 CPU: scissors (USER wins, Rock wins against scissors)
    print(computer_chose_ascii)
    print(scissors)
    print(win)

# User selects '1' (paper)
elif user_selection == 1 and computer_choice == "rock":
    # USER: 1 CPU: rock (USER wins, Paper wins against rock)
    print(computer_chose_ascii)
    print(rock)
    print(win)

elif user_selection == 1 and computer_choice == "paper":
    # USER: 1 CPU: paper (DRAW)
    print(computer_chose_ascii)
    print(paper)
    print(draw)

elif user_selection == 1 and computer_choice == "scissors":
    # USER: 1 CPU: scissors (USER loses, Paper loses to scissors)
    print(computer_chose_ascii)
    print(scissors)
    print(lose)

# User selects '2' (scissors)
elif user_selection == 2 and computer_choice == "rock":
    # USER: 2 CPU: rock (USER loses, Scissors loses to rock)
    print(computer_chose_ascii)
    print(rock)
    print(lose)

elif user_selection == 2 and computer_choice == "paper":
    # USER: 2 CPU: paper (USER wins, Scissors wins against paper)
    print(computer_chose_ascii)
    print(paper)
    print(win)

elif user_selection == 2 and computer_choice == "scissors":
    # USER: 2 CPU: scissors (DRAW)
    print(computer_chose_ascii)
    print(scissors)
    print(draw)
