import sqlite3
from Insert_time_of_live import Animals_ID_Name

try:
    conection=sqlite3.connect('E:/DB SQL3/DATA_BASE_FIRST_INSERCTION_PYTHON/DB_ANIMALS.db')
    cursor=conection.cursor()
    for i in range(len(Animals_ID_Name)):
        cursor.execute("""INSERT INTO Animals_ID ([NAME])
                        VALUES (?)""",(Animals_ID_Name[i],))
    cursor.fetchall()
    conection.commit()
except sqlite3.Error as e:
    print(f'tienes un error de tipo {e}')

finally:
    conection.close()
    print("La concección se cerro exitosamente")
