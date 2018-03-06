# Dice-Roller-Game
/Introduction/
- This python program was created in the fall of 2015 during my sophomore semester in my CS 230 Fundamentals of Computing course. This was one of the first projects I had done in this course and it was during a time my programming knowledge was very little compared to now. While this program is not very impressive in terms of coding skills, it is special to me for being one of my first successful python programs.

/Description/ 
- This program is a simple text adventure game that takes a random number between one and twenty and outputs that number into a fighting simulator. 
- You are the hero protagonist that encounters a horde of monsters that you fight one by one. You and each monster start out with one-hundred health points each.
- Once you defeat a monster you will have an option to keep fighting or save and quit.(The save function was never implemented properly and I was unable to get that feature working.)
- Each time you fight a monster your health will reset back to 100. 
- If you reach zero health points you will achieve a game over and you will have an option to start over. 
- The number you roll is implemented as the attack damage you deal(Example: If you roll a fourteen, you will deal fourteen damage to the monster.) and subtracting that number from twenty is how much damage the monster deals.(Example: If you roll a fourteen, the monster will deal six damage to you). 
- The special case where you roll a twenty will result in you dealing a critical hit (twenty points of damage) to the monster and it will be unable to attack you (zero points of damage). 
- The other special case where you roll a zero will result in the monster dealing a critical hit to you (twenty points of damage) and you will be unable to attack (zero points of damage).
- Another part of this game is experience. This feature does not affect gameplay at all, but it was implemented as practice.
- You, the player, will start the game at level one and each time you successfully defeat a monster you will receive 10 experience points. 
- To gain a new level you have to achieve twenty experience points (defeating two monsters). There is no cap to the amount of levels you can achieve. 
- The final important key feature is item drops.
- Every time you defeat a monster, there is a slight chance that it will drop one of four items.
- There is a twenty percent chance that it will drop a shiny dagger. There is a twenty percent chance that it will drop a shield. There is a ten percent chance it will drop a sword. Finally, there is a fifty percent chance that it will drop absolutely nothing
- The game is programmed to where if an item is dropped in that play through it cannot drop again. The items actually affect the gameplay. 
- If you receive a shiny dagger, every hit you deal will add an additional one damage (example: If you roll a six you will deal seven damage.). 
- If a monster drops a sword you will never have a chance to receive a shiny dagger and if you have a shiny dagger equipped, when a monster drops a sword the sword will replace the shiny dagger. 
- If you receive a shield, every hit you receive from the monster will be subtracted by one (example: If the monster deals eighteen damage you will be hit with seventeen damage.).
- If you receive a sword, every hit you deal will add an additional ten damage (example: If you roll a three you will deal thirteen damage.). 

/Algorithm/
- The first step in creating this program is implementing the random library. The random module is key for this program.
- The next step was to create your variables and define them. They include: player health, monster health, dice, experience, nothing, shiny dagger, shield, sword, and level.
- The next step is to create your while loop that loops until the player health is equal to 0.
- The next step is to make your conditionals for the dice.
- The final step is to make the items have random drops where they cannot drop multiple times.

