'''class Carro:
    pass

meu_carro = Carro()
meu_carro
<__main__.Carro object at 0x041135D0>
carro_do_ime = Carro()
carro_do_ime
<__main__.Carro object at 0x04113A50>
meu_carro.ano = 1968
meu_carro.modelo = 'Fusca'
meu_carro.cor = 'azul'
meu_carro.ano
1968
carro_do_ime.ano = 1981
carro_do_ime.modelo = 'Brasilia'
carro_do_ime.cor = 'amarelo'
carro_do_ime.modelo
'Brasilia'
novo_fusca = meu_carro
novo_fusca.ano += 10
meu_carro.ano
1978'''

class Pato:
  pass

pato = Pato()
patinho = Pato()
if pato == patinho:
  print("Estamos no mesmo endereço!")
else:
  print("Estamos em endereços diferentes!")
