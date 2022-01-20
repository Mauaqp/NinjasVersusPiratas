from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Greninja")

jack_sparrow = Pirate("Samurott")
jack_sparrow.show_stats()
michelangelo.show_stats()

#Turn 1
print("---Turn 1 ---")
michelangelo.attack(jack_sparrow)
jack_sparrow.attack(michelangelo)

#Turn 2
print("---Turn 2 ---")
michelangelo.attack(jack_sparrow)
jack_sparrow.attack(michelangelo)

#Turn 3
print("---Turn 3 ---")
michelangelo.attack(jack_sparrow)
jack_sparrow.attack(michelangelo)

#Turn 4
print("---Turn 4 ---")
michelangelo.attack(jack_sparrow)
jack_sparrow.attack(michelangelo)

#Turn 5
print("---Turn 5 ---")
michelangelo.attack(jack_sparrow)
jack_sparrow.attack(michelangelo)