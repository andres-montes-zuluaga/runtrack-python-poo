class Student:
    def __init__(self, nom, prenom, numero, credits):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credits = 0
        self.level = self._student_eval(self.__credits)
    
    def add_credits(self, credits):
        if credits <= 0:
            print("Le nombre de crédits à ajouter doit être égal ou supérieur à 1.")
        else:
            self.__credits += credits
            self.level = self._student_eval(self.__credits)
    
    def _student_eval(self, credits):
        if credits < 60:
            return "Insuffisant"
        elif credits < 70:
            return "Passable"
        elif credits < 80:
            return "Bien"
        elif credits < 90:
            return "Très bien"
        else:
            return "Excellent"
    
    def student_info(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"id: {self.__numero}")
        print(f"Évaluation: {self.level}")


student1 = Student("Doe", "John", 145, 0)
student1.add_credits(33)
student1.add_credits(33)
student1.add_credits(33)

student1.student_info()