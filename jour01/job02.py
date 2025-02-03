"""
This file demonstrates how to define an `Operation` class 
and initialize its attributes with given values.
"""
class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

instance = Operation(5, 3)

print(f"Le nombre1 est {instance.nombre1}")
print(f"Le nombre2 est {instance.nombre2}")