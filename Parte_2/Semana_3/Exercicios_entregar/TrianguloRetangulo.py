class Triangulo:
    def __init__(self, a, b, c):
        self.lA = a
        self.lB = b
        self.lC = c

    def retangulo(self):
        if self.lA <= 0 or self.lB <= 0 or self.lC <= 0:
            return False
        else:
            if self.lA + self.lB > self.lC and self.lB + self.lC > self.lA:
                if self.lA == self.lB and self.lA == self.lC and self.lB == self.lC:
                    return False
                #elif self.lA != self.lB and self.lA != self.lC and self.lB != self.lC:
                #    print('Aqui_4')
                #    return False
                elif self.lA == self.lB or self.lA == self.lC or self.lB == self.lC:
                    return False
                if self.lA**2 == self.lB**2+self.lC**2 or self.lB**2 == self.lA**2 + self.lC**2 or self.lC**2 == self.lA**2 + self.lB**2:
                    return True
            else:
                return False
