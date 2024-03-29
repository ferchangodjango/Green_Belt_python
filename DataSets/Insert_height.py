import sqlite3
from Insert_time_of_live import Animals_totals

try:
    conection=sqlite3.connect('E:/DB SQL3/DATA_BASE_FIRST_INSERCTION_PYTHON/DB_ANIMALS.db')
    cursor=conection.cursor()
    for i in range(len(Animals_totals)):
        cursor.execute("""INSERT INTO Animals_life (ID_WEIGHT,ID_ANIMAL,TIME_LIFE)
                       VALUES (?,?,?)""",Animals_totals[i])
    cursor.fetchall()
    conection.commit()
except sqlite3.Error as e:
    print(f'Tienes un error de tipo {e}')

finally:
    conection.close()
    print("La conección se ha cerrado exitosamente")