class Usuario:
    def __init__(self, nome, cpf, endereco, saldoConta, idade):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.saldoConta = saldoConta
        self.idade = idade

    def adicionarDinheiro(self, dinheiro):
        return self.saldoConta + dinheiro
    def removerDinheiro(self, dinheiro):
        return self.saldoConta - dinheiro
    def multiplicarDinheiro(self, dinheiro):
        return self.saldoConta * dinheiro
    def indentificarIdade(self):
        if self.idade < 18:
            print("Menor de idade")
        elif self.idade > 65:
            print("Velho de mais")
        else:
            print("Maior de idade")

usuario1 = Usuario("Lucas", "1234", "Rua Dois", 10, 20)
usuario1.adicionarDinheiro(10)
print(usuario1.removerDinheiro(11))
print(usuario1.saldoConta)
print(usuario1.multiplicarDinheiro(20))
usuario1.indentificarIdade()