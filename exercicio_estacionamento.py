import numpy as np
class Veiculo:
  def __init__(self, placa, estacionado = False):
    self.placa = placa
    self.estacionado = estacionado
  
  def estacionar(self):
    self.estacionado = True

  def sair_da_vaga(self):
    self.estacionado = False

class Moto(Veiculo):
  def __init__(self, placa, estacionado = False):
    super().__init__(placa, estacionado)

class Carro(Veiculo):
  def __init__(self, placa, estacionado = False):
    super().__init__(placa, estacionado)

class Vaga:
  def __init__(self, id, tipo, livre = True, placa = "nenhuma"):
    self.id = id
    self.tipo = tipo
    self.livre = livre
    self.placa = "nenhuma"
  
  def ocupar(self, placa):
    self.livre = False
    self.placa = placa

  def desocupar(self):
    self.livre = True
    self.placa = "nenhuma"

class Estacionamento:
  def __init__(self, vagas_de_carro, vagas_de_moto):
    vagas_carro = []
    vagas_moto = []
    for element in range(1, vagas_de_carro+1):
      vagas_carro.append(Vaga( element, "carro"))
    for element in range(vagas_de_carro+1, vagas_de_carro + vagas_de_moto+1):
      vagas_moto.append(Vaga( element, "moto"))
    self.vagas_carro = vagas_carro
    self.vagas_moto = vagas_moto
    self.total_vagas_livres_carro = vagas_de_carro
    self.total_vagas_livres_moto = vagas_de_moto
  
  def estacionar_carro(self, carro):
    status_vagas_carro = []
    for vaga in self.vagas_carro:
      status_vagas_carro.append(vaga.livre)
    if True in status_vagas_carro:
      idx_livre = status_vagas_carro.index(True)
      self.vagas_carro[idx_livre].ocupar(carro.placa)
      carro.estacionar()
      self.total_vagas_livres_carro -= 1
    else:
      print("Nenhuma vaga livre, espere mais")

  def estacionar_moto(self, moto):
    status_vagas_moto = []
    for vaga in self.vagas_moto:
      status_vagas_moto.append(vaga.livre)
      
    status_vagas_carro = []
    for vaga in self.vagas_carro:
      status_vagas_carro.append(vaga.livre)
      
    if True in status_vagas_moto:
      idx_livre = status_vagas_moto.index(True)
      self.vagas_moto[idx_livre].ocupar(moto.placa)
      moto.estacionar()
      self.total_vagas_livres_moto -= 1
    elif True in status_vagas_carro:
      idx_livre = status_vagas_carro.index(True)
      self.vagas_carro[idx_livre].ocupar(moto.placa)
      self.total_vagas_livres_carro -= 1
    else:
      print("Nenhuma vaga livre, espere mais")

  def remover_carro(self, carro):
    placas_carro_estacionamento = []
    for vaga in self.vagas_carro:
      placas_carro_estacionamento.append(vaga.placa)
    if carro.placa in placas_carro_estacionamento:
      idx_placa_ocupada = placas_carro_estacionamento.index(carro.placa)
      self.vagas_carro[idx_placa_ocupada].desocupar()
      carro.sair_da_vaga()
      self.total_vagas_livres_carro += 1
    else:
      print("Este carro não esté neste estacionamento")

  def remover_moto(self, moto):
    placas_moto_estacionamento = []
    placas_carro_estacionamento = []
    for vaga in self.vagas_carro:
      placas_carro_estacionamento.append(vaga.placa)
    for vaga in self.vagas_moto:
      placas_moto_estacionamento.append(vaga.placa)
    if moto.placa in placas_carro_estacionamento:
      idx_placa_ocupada = placas_carro_estacionamento.index(carro.placa)
      self.vagas_carro[idx_placa_ocupada].desocupar()
      moto.sair_da_vaga()
      self.total_vagas_livres_carro += 1
    elif moto.placa in placas_moto_estacionamento:
      idx_placa_ocupada = placas_moto_estacionamento.index(moto.placa)
      self.vagas_moto[idx_placa_ocupada].desocupar()
      moto.sair_da_vaga()
      self.total_vagas_livres_moto += 1  
    else:
      print("Esta moto não esté neste estacionamento")

  def estado_do_estacionamento(self):
    print(f"O Estacionamento tem {self.total_vagas_livres_carro} vagas disponíveis de carro e {self.total_vagas_livres_moto} vagas dispóniveis de moto.")

estacionamento1 = Estacionamento(25, 25)
fusca = Carro("1234")
moto1 = Moto("1111")
moto2 = Moto("1234")


estacionamento1.estacionar_carro(fusca)
#estacionamento1.estacionar_moto(moto1)
estacionamento1.estacionar_moto(moto2)

estacionamento1.remover_carro(fusca)
estacionamento1.remover_moto(moto1)

estacionamento1.estado_do_estacionamento()

