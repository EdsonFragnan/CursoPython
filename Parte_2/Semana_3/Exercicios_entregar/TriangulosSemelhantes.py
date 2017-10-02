class Triangulo:
    def __init__(self, a, b, c):
        self.lA = a
        self.lB = b
        self.lC = c

    def semelhantes(self_1, self_2):
        razao = self_1.lC / self_2.lC
        val_1 = self_1.lA / self_2.lA
        val_2 = self_1.lB / self_2.lB
        if razao == val_1 and razao == val_2:
            return True
        else:
            return False
