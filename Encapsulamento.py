#Encapsulamento

class Pessoa:
  def __init__(self, nome, profissao, identidade):
    self._nome = nome
    self.profissao = profissao
    self.__identidade = identidade
  
  def __str__(self):
    return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'

pessoa1 = Pessoa('Ana', 'progamadora', '123456')
print(pessoa1)


# Ao alterar um atributo protegido vamos conseguir, agora privado não é possível alterar
pessoa1._nome = 'Maria'
print(pessoa1._nome)

pessoa1.__identidade = '444444'
print(pessoa1.__identidade)

