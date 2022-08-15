class Carro:
  def __init__(self):
    self.ligado = False
    self.cor = 'vermelho'
    self.modelo = 'fusca'
    self.velocidade = 60
  
  def ligar(self):
    self.ligado = True
  
  def desligar(self):
    self.ligado = False
    self.velocidade = 0

  def acelera(self):
    if not self.ligado:
      return
    else:
      self.velocidade += 10

  def desacelera(self):
    if not self.ligado:
      return
    else:
      self.velocidade -= 10

  def __str__(self) -> str:
    return f'Carro - ligado {self.ligado} - cor {self.cor}  - modelo {self.modelo} - velocidade {self.velocidade}'

fusca = Carro()
fusca.ligar()
fusca.acelera()
fusca.desacelera()
fusca.desligar()
print('Carro: ',fusca)
