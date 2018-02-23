'''
    Monster Fight Program
    Author: Adam Sutton
    Date: 11/31/15

    This program takes a random number between 1 and 20 and outputs that number in a fighting simulator

    Algorithm:
    Step 1: Import random module
    Step 2: Put monster and player health into a variable
    Step 3: Make a while loop to where the program will keep looping unless either health is less than or equal to 0
    Step 4: Make condittionals for the values that the dice will roll
    Step 5: Have the program print out who won when battle is over
    Step 6: Make it to where you gain 10 experience points if you defeat the monster and if you gain 20 you level up
    Step 7: Make the items have random drops and where they cannot drop more than once
'''

import random



player_health = 100          #defining the player health and monster health so both start with 100 health points
monster_health = 100
dice = random.randint(1, 20)
experience = 0
nothing = 0
shiny_dagger = 0             #Defining all the items as 0 so that start off with that value
shield = 0
sword = 0
level = 1



print('''
As you journey on through the forest you encounter a horde of ferocious monsters.
Prepare to fight!''')

choice1 = "not s"
while choice1 != "s" and player_health >= 1:          #keeps looping as long as player is still alive
    player_health = 100          
    monster_health = 100
    print(''' Press f to fight or press s to save and quit''')
    choice1 = input(" ")
    if choice1 != "f" and choice1 != "s":                  #Conditionals that let you continue or quits the game
        print("Invalid Input")
    elif choice1 == "f":
        print("Press enter to roll the dice")
        
        


        while player_health >= 1 and monster_health >= 1:   #the program keeps looping as long as health is less than or equal to 1

            choice2 = input("")                                 
            dice = random.randint(1, 20)    #defining dice so that it will roll random number between 1 and 20
            print(dice)
            

            if dice == 1:
                print('''You missed badly and your defenses are open.
                      The monster hits you for 20 points of damage.''')
                monster_damage = 20 - shield
                player_damage = 0
                player_health = player_health - monster_damage           #Player is hit with 20 points of damage
                monster_health = monster_health - player_damage          #Monster is hit with 0 points of damage
                print("Your Health:", player_health)
                print("Monster Health:", monster_health)
                if player_health <= 0:
                    print("You died. The monster wins.")
                elif monster_health <= 0:
                    print("The monster died. You win.")
                    
                elif player_health <= 0 and monster_health <= 0:
                    print("You both fall in combat")
                

            elif dice == 20:
                print('''Perfect Hit! The monster can not attack.
                         You hit the monster for 20 points of damage.''')
                monster_damage = 0
                player_damage = 20 + shiny_dagger + sword
                player_health = player_health - monster_damage            #Player is hit with 0 points of damage
                monster_health = monster_health - player_damage          #Monster is hit with 20 points of damage
                print("Your Health:", player_health)
                print("Monster Health:", monster_health)
                if player_health <= 0:
                    print("You died. The monster wins.")
                elif monster_health <= 0:
                    print("The monster died. You win.")
                    
                elif player_health <= 0 and monster_health <= 0:
                    print("You both fall in combat")
                

                
            else:
                print('''You hit the monster for''' , dice, '''points of damage
                         The monster hits you for''' , 20 - dice, '''points of damage.''')
                monster_damage = (20 - dice) - shield
                player_damage = dice + shiny_dagger + sword
                player_health = player_health - monster_damage     #Player is hit with (20 - roll of the dice) points of damage
                monster_health = monster_health - player_damage          #Monster is hit with the value of dice points of damage
                print("Your Health:", player_health)
                print("Monster Health:", monster_health)
                if player_health <= 0:
                    print("You died. The monster wins.")
                elif monster_health <= 0:
                    print("The monster died. You win.")
                    
                elif player_health <= 0 and monster_health <= 0:
                    print("You both fall in combat")
                

            if monster_health <= 0:                         
                experience = experience + 10                        #defining experience
                print("You gained 10 experience points")
                
                
                drop_rate = (random.randint(1,100))
                if experience % 20 == 0:                             #if experience modulus 20 = 0 then you level up
                    print("You leveled up.")
                    level = level + 1
                print("Level:")
                print(level)
                if drop_rate in range(51,100):
                    print("It dropped nothing")
                    nothing = 0
                elif drop_rate in range(1,20) and (shiny_dagger != 1 and sword != 10):                   # The dagger will not drop if the sword has been dropped
                    print("It dropped a shiny dagger")
                    shiny_dagger = 1
                elif drop_rate in range(21,40) and shield != 1:
                    print("It dropped a shield")
                    shield = 1
                elif drop_rate in range(41,50) and sword != 10:
                    print("It dropped a sword")
                    sword = 10
                    shiny_dagger = 0                #If you already have a dagger and a sword drops, the sword will replace it


                
                
                  
              

