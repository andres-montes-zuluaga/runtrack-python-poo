"""
This file demonstrates how to define an `Operation` class 
and create an instance of this class.
"""
class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

instance = Operation(5, 3)
print(instance)