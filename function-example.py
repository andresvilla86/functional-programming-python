#Una funciona puramente solo depende de su entrada para determinar una salida (si existe)
#no retiene data

#Ejemplo

def suma(x,y):
  x + y

#notese que en un ejemplo OO es posible cambiar el valor "age" sin necesidad de cambiar la entrada  
class Person:
  def __init__(self, name, age):
    self.name
    self.age
    
  def increase_age(self):
    self.age += 1
    
  def get_age(self):
    return self.age
