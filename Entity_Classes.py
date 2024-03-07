class Entity:
    '''Entity class'''
    
    def __init__(self, name, max_hp):
        '''Entity class constructor'''
        self.__name = name
        self.__max_hp = self.__hp = max_hp

        if max_hp <= 0:
            self.__max_hp = self.__hp = 0
            self.__is_alive = False
            print(f'A wild {self} has spawned, but died immediately... (0 HP)')
        else:
            self.__is_alive = True
            print(f'A wild {self} has spawned! ({self.get_hp()} HP)')
    
    # PROTECTED METHODS
    def __gain_hp(self, amount):
        self.__hp += amount

        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp
        elif not self.__is_alive:
            self.__is_alive = True
    
    def __lose_hp(self, amount):
        self.__hp -= amount

        if self.__hp <= 0 and self.__is_alive:
            self.__hp = 0
            self.__is_alive = False

    # GETTERS
    def get_name(self):
        '''Returns the name of Entity object (str)'''
        return self.__name

    def get_hp(self):
        '''Returns the current HP of Entity object (int)'''
        return self.__hp

    def get_max_hp(self):
        '''Returns the maximum HP an Entity object can get (int)'''
        return self.__max_hp

    def get_alive(self):
        '''Returns the current alive state of Entity object (bool)'''
        return self.__is_alive

    # MAGIC METHOD
    def __str__(self):
        return f'Entity \'{self.__name}\''


class Friendly_Entity(Entity):
    '''Non-attacking Entity class (inherited from Entity class)'''

    def __init__(self, name: str, max_hp: int):
        '''Friendly Entity class constructor'''
        super().__init__(name, max_hp)


class Attacking_Entity(Entity):
    '''Damage-dealing Entity class (inherited from Entity class)'''

    def __init__(self, name: str, max_hp: int):
        '''Attacking Entity class constructor'''
        super().__init__(name, max_hp)

    # ACTION METHODS
    def attack(self, Receiver: Entity, attack_damage: int):
        '''Attacks the given Entity or related object with specified amount of damage'''
        if Receiver.get_alive() == False:
            print(f'{Receiver} is already dead... (0 HP)')
        elif attack_damage < 0:
            print(f'{self} can\'t deal a negative amount of damage to {Receiver}...')
        elif attack_damage == 0:
            print(f'{self} attacks {Receiver}, but nothing happened...')
        elif self.get_alive() == False:
            print(f'{self} can\'t attack because of 0 HP...')
        else:
            if Receiver.get_hp() < attack_damage:
                attack_damage = Receiver.get_hp()
            Receiver._Entity__lose_hp(attack_damage)
            if Receiver == self:
                print(f'{self} attacks itself, dealing {attack_damage} attack damage!')
            else:
                print(f'{self} attacks {Receiver}, dealing {attack_damage} attack damage!')

            if Receiver.get_alive() == False:
                print(f'{Receiver} fainted... (0 HP)')
            else:
                print(f'{Receiver} now has {Receiver.get_hp()} HP.')

    def heal(self, amount: int):
        '''Restores an amount of HP of Entity or related object'''
        if self.get_alive() == False:
            print(f'{self} can\'t be healed because of 0 HP... Try to \'revive\' it instead!')
        elif amount < 0:
            print(f'{self} can\'t be healed with negative points...')
        elif amount == 0:
            print(f'The healing given to {self} is not healing... ({self.get_hp()} HP)')
        elif self.get_hp() == self.get_max_hp():
            print(f'{self} can\'t be healed no more...')
        else:
            self._Entity__gain_hp(amount)
            if self.get_max_hp() > self.get_hp() + amount:
                amount = self.get_max_hp() - self.get_hp()
            print(f'{self} HP was restored by {amount} points! ({self.get_hp()} HP)')

    def revive(self):
        '''Revives a dead Entity or related object'''
        if self.get_alive() == False:
            self._Entity__gain_hp(self.get_max_hp())
            print(f'{self} was successfully revived! ({self.get_hp()} HP)')
        else:
            print(f'{self} is still alive... ({self.get_hp()} HP)')


class Monster(Attacking_Entity):
    '''Monster class (inherited from Attacking Entity class)'''

    def __init__(self, name: str, max_hp: int):
        '''Monster class constructor'''
        super().__init__(name, max_hp)

    # MAGIC METHOD
    def __str__(self):
        '''String representation of Monster object'''
        return f'Monster \'{self.get_name()}\''


class Player(Attacking_Entity):
    '''Player class (inherited from Attacking Entity class)'''

    def __init__(self, name: str, max_hp: int):
        '''Player class constructor'''
        super().__init__(name, max_hp)

    # MAGIC METHOD
    def __str__(self):
        '''String representation of Player object'''
        return f'Player \'{self.get_name()}\''


class Animal(Friendly_Entity):
    '''Animal class (inherited from Friendly Entity class)'''

    def __init__(self, name: str, max_hp: int):
        '''Animal class constructor'''
        super().__init__(name, max_hp)

    # MAGIC METHOD
    def __str__(self):
        '''String representation of Animal object'''
        return f'Animal \'{self.get_name()}\''