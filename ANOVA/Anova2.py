import sqlite3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
import pingouin as pg
conection=sqlite3.connect('E:/DB SQL3/DATA_BASE_FIRST_INSERCTION_PYTHON/DB_ANIMALS.db')

query="""
    SELECT Animals_ID.NAME,Animals_features.WEIGHT,Animals_features.TIME_LIFE
    FROM Animals_features
    INNER JOIN Animals_ID ON Animals_ID.ID_ANIMAL=Animals_features.ID_ANIMAL """

Features_animals=pd.read_sql_query(query,conection)

