from Entity_Classes import Entity, Player, Monster, Animal


if __name__ != '__main__':
	exit()


# Spawn a Player, a Monster, and an Animal object
player = Player('Steve',20)
zombie = Monster('Zombie',10)
cow = Animal('Cow',5)

# Spawn a premature entity
prematured = Entity('Prematured',0)

# Display the current HP of entities
print("Player:",player.get_hp())
print("Zombie:",zombie.get_hp())
print("Cow:",cow.get_hp())
print("Premature Entity:",prematured.get_hp())

# Display the current life state of entities
print("Player is alive:",player.get_alive())
print("Zombie is alive:",zombie.get_alive())
print("Cow is alive:",cow.get_alive())
print("Premature Entity is alive:",prematured.get_alive())

# Player kills the cow, dealing 5 attack damage
player.attack(cow,5)

# Display the current life state of the cow
print("Cow is alive:",cow.get_alive())

# Zombie attacks the player, dealing 3 attack damage
zombie.attack(player,3)

# Zombie tries to attack the player with a negative attack damage
zombie.attack(player,-3)

# Zombie attacks the player with no damage
zombie.attack(player,0)

# Player finishes the zombie with 10 attack damage
player.attack(zombie,10)

# Player tries to attack the dead zombie, but it is already dead
player.attack(zombie,1)

# Zombie can't attack as it is already dead
zombie.attack(player,1)

# Player was healed by 3 HP
player.heal(3)

# Player wants to be healed again, but it has reached full health
player.heal(20)

# Player wants to be healed by 0 points
player.heal(0)

# Zombie was revived, restoring to full health
zombie.revive()

# Zombie became enraged, dealing a death blow to player
zombie.attack(player,20)

# Player tries to heal, but cannot because it is dead
player.heal(20)

# Player was revived, restoring to full health
player.revive()