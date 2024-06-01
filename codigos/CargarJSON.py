from sqlalchemy import create_engine
import pandas as pd

db = "conagua"
path = 'meteorologia_json.csv'
url = "mysql+mysqlconnector://bd_conagua:HkW0eiFxfT5iUv31@34.72.69.10/"

table = "Meteorologia"
parent_table_one = "Catalogo_de_estaciones"
parent_table_two = "Catalogo_de_parametros"
engine = create_engine(url + db, echo = False)

df = pd.read_csv(path)
df_parent_one = pd.read_sql_table(parent_table_one, engine)
df_parent_two = pd.read_sql_table(parent_table_two, engine)
df_parent_one = df_parent_one.drop(columns = ['nom_estac', 'longitud', 'latitud', 'alt', 'id_obs_estac', 'id_city'])
df_parent_two = df_parent_two.drop(columns = ['cve_nom'])
df = df.merge(df_parent_one, left_on= "estacion", right_on= "cve_estac", how="inner")
df = df.merge(df_parent_two, left_on= "parametro", right_on= "cve_param", how="inner")
df = df.drop(columns=["parametro", "estacion", "cve_estac", "cve_param"])

def subir_datos_por_lotes(dataframe, nombre_tabla, tamano_lote):
    """
    Sube un DataFrame a una tabla MySQL por lotes usando SQLAlchemy.

    Args:
        dataframe (pandas.DataFrame): El DataFrame que contiene los datos a subir.
        nombre_tabla (str): El nombre de la tabla en la base de datos MySQL.
        tamano_lote (int): El tamaño de cada lote de datos a subir.
    """
    db = "conagua"
    url = "mysql+mysqlconnector://bd_conagua:HkW0eiFxfT5iUv31@34.72.69.10/"
    engine = create_engine(url + db, echo = False)
    with engine.connect() as conn:
        for i in range(0, len(dataframe), tamano_lote):
            lote_datos = dataframe[i:i + tamano_lote]
            #lote_datos.to_sql(name = nombre_tabla, con = engine, if_exists = "append", index = False)
            
        
subir_datos_por_lotes(df, table, 10000)