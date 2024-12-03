class House:
    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def __len__(self):
         return self.number_of_floors

    def __str__(self):
       title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
       return title

    def __eq__(self, other): #1
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):    # 2
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self


my_house1 = House('ЖК Армавирский', 18)
my_house2 = House('Домик в деревне', 5)

print(my_house1)
print(my_house2)
# 1
print(my_house1 == my_house2)
# 3
print(my_house2.__add__(8))
print(my_house1 == my_house2)
# 2
print(my_house1 < my_house2)
print(my_house1 <= my_house2)
print(my_house1 > my_house2)
print(my_house1 >= my_house2)
print(my_house1 != my_house2)
# 5
print(my_house1.__radd__(7))
print(my_house2.__iadd__('8')) # не прибавляется
print(my_house2.__iadd__(8))