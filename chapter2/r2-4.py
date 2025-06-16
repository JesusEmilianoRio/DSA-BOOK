"""
Write a Python class, Flower, that has three instance variables of type str,
 int,andfloat, that respectively represent the name of the flower, its num
ber of petals, and its price. Your class must include a constructor method
 that initializes each variable to an appropriate value, and your class should
 include methods for setting the value of each type, and retrieving the value
 of each type.
"""

class Flower:
    """A flower sales"""
    def __init__(self, name_flower = "Romina", num_petal = 5, price = 50.0):
        """
        Create a new Flower instance.

        The initial price is 50.0

        name_flower the name of the flower (e.g., 'Rosa')
        num_petal   the total of petals it has (e.g., 5)
        price       the cost of each flower (measured in pesos)
        """

        self.name_flower = name_flower
        self.num_petal = num_petal
        self.price = price

    def get_name_flower(self):
        """Return the name of the flower"""
        return self.name_flower

    def get_num_petal(self):
        """Return the number of petals"""
        return self.num_petal

    def get_price(self):
        """Return the price of the flower"""
        return self.price

    def set_name_flower(self, name_flower):
        """Set a new name of the flower"""
        self.name_flower = name_flower

    def set_num_petal(self, num_petal):
        """Set a new number of petals"""
        self.num_petal = num_petal

    def set_price(self, price):
        """Set a new price of the flower"""
        self.price = price


