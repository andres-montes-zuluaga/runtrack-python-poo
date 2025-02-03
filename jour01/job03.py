class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        return self.nombre1 + self.nombre2

instance = Operation(5, 3)

print(f"Le nombre1 est {instance.nombre1}")
print(f"Le nombre2 est {instance.nombre2}")

addition = instance.addition()

print(f"Le résultat de l'addition est {addition}")