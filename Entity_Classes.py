class Entity:
    '''Entity class'''
    
    def __init__(self, name, max_hp):
        '''Entity class constructor'''
        self.__name = name
        self.__max_hp = self.__hp = max_hp

        if max_hp <= 0:
            self.__max_hp = 0
            self.__is_alive = False
        else:
            self.__is_alive = True
    
    # PROTECTED METHODS
    def __gain_hp(self, amount):
        self.__hp += amount

        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp
        elif not self.__is_alive:
            self.__is_alive = True
    
    def __lose_hp(self, amount):
        self.__hp -= amount

        if self.__hp >= 0:
            self.__hp = 0
            self.__is_alive = False

    # GETTERS
    def get_name(self):
        '''Returns the name of Entity object'''
        return self.__name

    def get_hp(self):
        '''Returns the current HP of Entity object'''
        return self.__hp