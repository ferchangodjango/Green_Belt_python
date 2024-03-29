# Cargue la tabla con datos de forma masiva
from faker import Faker
import random 
import numpy as np

#Generamos 100 valores aleatorios que sigan una distribución normal
valores_normales=np.random.normal(500,15,100)
fake=Faker()
lista_nombres_direcciones=[]
for i in range(100):
    lista_nombres_direcciones.append((fake.name(),fake.company(),fake.job(),valores_normales[i]))

print(len(lista_nombres_direcciones))