class Idade:   
  def __init__(self):   
    self._age = 0
  # using the getter method
  @property   
  def age(self):
    print('Getter Method')   
    return self._age

  # using the setter method   
  @age.setter
  def age(self, value):   
    self._age = value
  def envelhecer(self):
    self._age += 1

#Cria objeto com idade default
thais = Idade()   
print(thais.age)

#Set idade desejada  
thais.age = 25 
print(thais.age)

#Aplica método da classe Idade
thais.envelhecer()  
    
#Get idade final
print(thais.age)  