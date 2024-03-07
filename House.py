class House:
    # CONSTRUCTOR
    def __init__(self, area:int, name:str):
        '''Constructor'''
        self.__area = area # in square meters
        self.__name = name

        self.__door_is_open = False
    
    # STRING OBJECT REPRESENTATION
    def __str__(self):
        return f'[House Object ({self.__name})]'

    # METHODS
    def print_details(self):
        '''Prints the name and area of House object'''
        print('# HOUSE DETAILS:')
        print('Name:', self.__name)
        print('Area:', self.__area, 'sq. meters')

    def open_door(self):
        '''Opens the door of House object'''
        print(f'[{self.__name}]', end=' ')

        if not self.__door_is_open:
            self.__door_is_open = True
            print('The door is now open.')
        else:
            print('The door is already opened.')
    
    def close_door(self):
        '''Closes the door of House object'''
        print(f'[{self.__name}]', end=' ')

        if self.__door_is_open:
            self.__door_is_open = False
            print('The door is now close.')
        else:
            print('The door is already closed.')
    
    def get_area(self):
        '''Returns the area of House object'''
        return f'{self.__area} square meters'
    
    def get_name(self):
        '''Returns the name of House object'''
        return self.__name


h1 = House(30, 'Bahay ko')

h1.print_details()
h1.open_door()
h1.close_door()

print(h1.get_name(), h1.get_area())