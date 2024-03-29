import sqlite3
from Random_data import lista_nombres_direcciones

try:
    conection_1=sqlite3.connect('E:/DB SQL3/DATA_BASE_FIRST_INSERCTION_PYTHON/DB_ANIMALS.db')
    cursor_1=conection_1.cursor()
    for i in range(len(lista_nombres_direcciones)):
        cursor_1.execute(""" INSERT INTO PEOPLE (NAME,COMPANY,JOB,PROFIT_DAILY)
                        VALUES (?,?,?,?)""",lista_nombres_direcciones[i])
        result=cursor_1.fetchall()
        
        conection_1.commit()


except sqlite3.Error as e:
    print(f'Tuviste un error de tipo {e}')

finally:
    conection_1.close()
    print("La conexión ha sido cerrada")
