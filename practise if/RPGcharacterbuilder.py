import random # to import the random module for generating random numbers
def create_character(name,strength,intelligence,charisma,role):
     if not isinstance(name,str):# to check the type of name
        raise TypeError("Name must be a string")
     if " " in name:# to check if the name contains spaces
        raise ValueError("Name cannot contain spaces")
     if len(name)<3 or len(name)>10:# to check the length of the name
        raise ValueError("Name must be between 3 and 10 characters")
    
     skills = (strength,intelligence,charisma ) # to create a tuple of the skills
     if not all(isinstance(skill,int) for skill in skills):# to check the type
        raise TypeError("Skills must be integers")
     if not all(1<=skill<=10 for skill in skills):# to check the range of the skills
            raise ValueError("Skills must be between 1 and 10")
     if sum(skills)>15:# to check the total points of the skills
            raise ValueError("Total skill points cannot exceed 15")
     if role not in ["Warrior","Mage","Rogue"]:# to check if the role is valid
        raise ValueError("Role must be either Warrior, Mage or Rogue")
     if role=="Warrior":# to check if the role is Warrior
        strength+=2 # to increase the strength by 2 for Warriors
     elif role=="Mage":# to check if the role is Mage
        intelligence+=2 # to increase the intelligence by 2 for Mages
     else:# to check if the role is Rogue
        charisma+=2 # to increase the charisma by 2 for Rogues

     HP = strength*10 # to calculate the HP based on the strength
     Attack = strength*2+ intelligence # to calculate the Attack based on the strength
     Defense = charisma + intelligence # to calculate the Defense based on the charisma and intelligence
     level = 1 # to set the level to 1
     return {
             "Name": name,
             "Role": role, 
             "HP": HP,
             "Attack": Attack,
             "Defense": Defense,
             "Level": level,
             "Strength": strength,
             "Intelligence": intelligence,
             "Charisma": charisma
         } 
def create_enemy ():
    return { 
        "Name":random.choice(["skeleton","Orc", "Goblin"]),
        "HP": random.randint(50, 100),
        "Attack": random.randint(5,15),
        "Defense": random.randint(3,10)
     } 
def attack(attacker, defender):
    damage =  attacker["Attack"] - defender["Defense"]# to calculate the damage based on the attacker's attack and defender's defense
    damage = max(1,damage) # to ensure that the damage is not negative
    defender["HP"] -= damage # to reduce the defender's HP by the damage
    return f"{attacker['Name']} attacks {defender['Name']} for {damage} damage! {defender['Name']} has {defender['HP']} HP left." # to return a string describing the attack and the defender's remaining HP
Player = create_character("Aragorn", 5, 3, 2, "Warrior") # to create a character with the name Aragorn, strength of 5, intelligence of 3, charisma of 2 and role of Warrior
Enemy = create_enemy() # to create a random enemy
print(Player) # to print the player's attributes
print(Enemy) # to print the enemy's attributes 
print(attack(Player, Enemy)) # to simulate an attack from the player to the enemy and print the result          
print(f"Enemy HP: {Enemy['HP']}") # to print the enemy's remaining HP

