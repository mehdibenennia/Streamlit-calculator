class Calcul:
    def __init__(self, valeur1, valeur2):
        self.valeur1 = valeur1
        self.valeur2 = valeur2

    def calcul_somme(self):
        return self.valeur1 + self.valeur2

    def cacul_soustraction(self):
        return self.valeur1 - self.valeur2

    def cacul_multiplication(self):
        return self.valeur1 * self.valeur2

    def cacul_division(self):
        try:
            result = self.valeur1 / self.valeur2
        except ZeroDivisionError:
            result = "Cannot divide on 0"
        return result
