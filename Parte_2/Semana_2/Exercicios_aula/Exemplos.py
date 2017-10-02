def peso_altura():
    return 82, 1.80

def pagamento_semanal(valor_por_hora, num_horas = 40):
    assert valor_por_hora >= 0 and num_horas > 0
    return valor_por_hora * num_horas


def calculo(x, y = 10, z = 5):
    return x + y * z;

print(calculo(7))
print(calculo( ,12, 10))
print(calculo(7, 2))
print(calculo())
print(calculo(1, 2, 3))

def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s

print(horario_em_segundos(1,2,3))
print(horario_em_segundos (10,-10,34))
print(horario_em_segundos (3,0,50))
print(horario_em_segundos (-1,20,30))
print(horario_em_segundos (1,33,-50))
