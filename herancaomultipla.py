#herancaomultipla

class Logavel:
  def __init__(self):
    self.nome_da_classe = ''
  def logar(self, mensagem):
    print('Mensagem da classe' + self.nome_da_classe + ':' + mensagem)

class Conexao:
  def __init__(self):
    self.servidor = ''
  def conectar(self):
    print('Conectando ao banco de dados no servidor ' + self.servidor)

class MySqlDatabase(Conexao, Logavel):
  def __init__(self):
    super().__init__()
    self.nome_da_classe = 'MySqlDatabase'
    self.servidor = 'Meu servidor'

def framework(item):
  if isinstance(item, Conexao):
    item.conectar()
  if isinstance(item, Logavel):
    mensagem ='Boa noite minhas queridas, SABADOUUUUUUUUU'
    item.logar(mensagem)

conexao_mysql = MySqlDatabase()
framework(conexao_mysql)

  


