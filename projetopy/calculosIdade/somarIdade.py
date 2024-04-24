def somarIdade(idadePessoa1, idadePessoa2):
    resultado = idadePessoa1 + idadePessoa2
    if resultado >= 50 and resultado <= 60:
        print("É maior que 50")
        print(resultado * 2)
    elif resultado >= 70 or resultado == 62:
        print("É maior que 60")
        print(resultado / 2)
    else:
        print("É menor que 50 e menor que 60")
somarIdade(25, 25)

listaDeFrutas = ['Banana','Maçã','Laranja',2]
print(listaDeFrutas[3])