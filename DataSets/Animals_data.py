import numpy as np
import random 

Numero_de_datos=5000
ID_cientificos=[i+1 for i in range(100)]

ID_cientificos_Random=[random.sample(ID_cientificos,1)[0] for i in range(Numero_de_datos)]
Cat_name=['CAT' for i in range(Numero_de_datos)]
Dog_name=['DOG' for i in range(Numero_de_datos)]
Wolf_name=['WOLF' for i in range(Numero_de_datos)]
Horse_name=['HORSE' for i in range(Numero_de_datos)]

CAT_id=[1 for i in range(Numero_de_datos)]
DOG_id=[2 for i in range(Numero_de_datos)]
WOLF_id=[3 for i in range(Numero_de_datos)]
HORSE_id=[4 for i in range(Numero_de_datos)]

Cat_weight=np.random.normal(5,1,Numero_de_datos)
Dog_weight=np.random.normal(40,5,Numero_de_datos)
Wolf_weight=np.random.normal(60,20,Numero_de_datos)
Horse_weight=np.random.normal(400,30,Numero_de_datos)

Cat_live=np.random.normal(15,2,Numero_de_datos)
Dog_live=np.random.normal(15,3,Numero_de_datos)
Wolf_live=np.random.normal(12,2,Numero_de_datos)
Horse_live=np.random.normal(30,5,Numero_de_datos)


Cat_Total_data=[(ID_cientificos_Random[i],CAT_id[i],Cat_weight[i],Cat_live[i]) for i in range(Numero_de_datos)]
Dog_Total_data=[(ID_cientificos_Random[i],DOG_id[i],Dog_weight[i],Dog_live[i]) for i in range(Numero_de_datos)]
Wolf_Total_data=[(ID_cientificos_Random[i],WOLF_id[i],Wolf_weight[i],Wolf_live[i]) for i in range(Numero_de_datos)]
Horse_Total_data=[(ID_cientificos_Random[i],HORSE_id[i],Horse_weight[i],Horse_live[i]) for i in range(Numero_de_datos)]
Animals_totals=[]
Animals_totals.extend(Cat_Total_data)
Animals_totals.extend(Dog_Total_data)
Animals_totals.extend(Wolf_Total_data)
Animals_totals.extend(Horse_Total_data)
