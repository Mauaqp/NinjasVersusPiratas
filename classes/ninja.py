class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 20
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if self.health > 0:
            self.hitpoints()
            print(self.name + " attacked "+ pirate.name + " doing " + str(self.strength)+ " damage points!")
            pirate.health -= self.strength
            self.hitpoints()
        else:
            print(self.name + " lost the game")
        return self

    def hitpoints (self):
        if self.health <= 0:
            print(self.name + " fainted")