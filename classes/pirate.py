class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 23
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if self.health > 0:
            self.hitpoints()
            print(self.name + " attacked "+ ninja.name + " doing " + str(self.strength)+ " damage points!")
            ninja.health -= self.strength
            self.hitpoints()
        else:
            print(self.name + " lost the game")
        return self
    
    def hitpoints (self):
        if self.health <= 0:
            print(self.name + " fainted")
