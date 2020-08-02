# This is a monster game! It is a one-on-one fight! Can you beat your enemy?

#Import random function
import random

#I define the weapon class
class Weapon:
    weapon_kind = ""
    attack_strength = 0

#I deifne the shield class
class Shield:
    shield_kind = ""
    defense_strength = 0

#I define the moster class
class Monster:
    name = ""
    life_points = 100
    weapon = Weapon()
    shield = Shield()

    def attack(self, strength):
        return strength

    def defend(self, efficiency):
        return efficiency

#I create the sword weapon
sword = Weapon()
sword.weapon_kind = "Sword"
sword.attack_strength = 5
#I create the axe weapon
axe = Weapon()
axe.weapon_kind = "Axe"
axe.attack_strength = 10
#I create the iron shield
iron = Shield()
iron.shield_kind = "Iron"
iron.defense_strength = 10
#I create the wooden shield
wooden = Shield()
wooden.shield_kind = "Wooden"
wooden.defense_strength = 5

#I create the first monster
venom = Monster()
venom.name = "Venom"
venom.weapon = sword
venom.shield = iron
#I create the second monster
goblin = Monster()
goblin.name = "Goblin"
goblin.weapon = axe
goblin.shield = wooden

#Initialize main loop 
play = True
#Initialize monsters
player1 = goblin
player2 = goblin

#Initialize attacks values
attack1 = 0
attack2 = 0

#Initialize defense values
defense1 = 0
defense2 = 0

#Initialize lost life points
lost1 = 0
lost2 = 0

#Initialize counter
i = 0

#Main loop starts here
while play == True:

    #Player 1 chooses the monster
    player1_choice = input("Hi Player 1! Choose your monster: Goblin/Venom\n").strip().lower()
    if player1_choice == "goblin":
        player1 = goblin
    elif player1_choice == "venom":
        player1 = venom

    #Player 2 chooses the monster 
    player2_choice = input("Hi Player 2! Choose your monster: Goblin/Venom\n").strip().lower()
    if player2_choice == "goblin":
        player2 = goblin
    elif player2_choice == "venom":
        player2 = venom

    #Game loop starts here
    while player1.life_points > 0 and player2.life_points> 0:
        
        i = i + 1
        #player 1 attacks
        player1_attacks = input("Player 1, do you want to attack?yes/no\n").strip().lower()
        if player1_attacks == "yes":
            attack1 = player1.attack(player1.weapon.attack_strength*random.randint(1, 10))
        elif player1_attacks == "no":
            attack1 = player1.attack(player1.weapon.attack_strength*0)
        print("Player 1 attacked with a strength of " + str(attack1) + " life points")
        #player 2 defends
        player2_defends = input("Player 2, do you want to defend?yes/no\n").strip().lower()
        if player2_defends == "yes":
            defense2 = player2.defend(player2.shield.defense_strength*random.randint(1, 10))
        elif player2_defends == "no":
            defense2 = player2.defend(player2.shield.defense_strength*0)
        print("Player 2 defended for " + str(defense2) + " life points")
        #player 2 attacks
        player2_attacks = input("Player 2, do you want to attack?yes/no\n").strip().lower()
        if player2_attacks == "yes":
            attack2 = player2.attack(player2.weapon.attack_strength*random.randint(1, 10))
        elif player2_attacks == "no":
            attack2 = player2.attack(player1.weapon.attack_strength*0)
        print("Player 2 attacked with a strength of " + str(attack2) + " life points")
        #player 1 defends
        player1_defends = input("Player 1, do you want to defend?yes/no\n").strip().lower()
        if player1_defends == "yes":
            defense1 = player1.defend(player1.shield.defense_strength*random.randint(1, 10))
        elif player1_defends == "no":
            defense1 = player1.defend(player1.shield.defense_strength*0)
        print("Player 1 defended for " + str(defense1) + " life points")

        #fighting round calculation
        lost1 = attack2 - defense1
        lost2 = attack1 - defense2
        if lost1 < 0:
            lost1 = 0
        else:
            lost1 = lost1

        if lost2 < 0:
            lost2 = 0
        else:
            lost2 = lost2

        player1.life_points = player1.life_points - lost1
        player2.life_points = player2.life_points - lost2
        
        print("Player 1 lost " + str(lost1) + " life points in this round")
        print("Player 2 lost " + str(lost2) + " life points in this round")

        if lost2 > lost1:
            print("Player 1 won round " + str(i) + "!!!")
        elif lost2 < lost1:
            print("Player 2 won round " + str(i) + "!!!")
        else:
            print("Round " + str(i) + " was a draw!")

        #Did any one die?
        if player1.life_points <= 0:
            print("Player 2 won the battle!!!")
        elif player2.life_points <= 0:
            print("Player 1 won the battle!!!")
        else:
            print("Player 1 has " + str(player1.life_points) + " life points left")
            print("Player 2 has " + str(player2.life_points) + " life points left")
            print("Next round!!!")
    
    #The players are asked to play again
    user_wish = input("Do you want to play again?: yes/no\n").strip().lower()
    if user_wish == "yes":
        play = True
    elif user_wish == "no":
        play = False
    else:
        print("Please type only 'yes' or 'no'")
print("Thanks for playing with us! See you next time!!!")