class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo     = m
        self.ano        = a
        self.cor        = c
        self.vel        = 0
        self.maxV       = vm # Velocidade máxima

    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print(  '%s %s %d'%(self.modelo, self.cor, self.vel)    )
        elif self.vel < self.maxV:
            print(  '%s %s indo a %d Km/h'%(self.modelo, self.cor, self.vel)    )
        else:
            print(  '%s %s indo muito raaaaaaapiiiiiidoooooo!'%(self.modelo, self.cor)    )

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

