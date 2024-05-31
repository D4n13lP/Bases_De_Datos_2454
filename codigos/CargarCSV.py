from sqlalchemy import create_engine
import pandas as pd


db = "conagua"
path = 'datos-base/catálogos-20240524T201146Z-001/catálogos/cat_unidades.csv'
url = "mysql+mysqlconnector://bd_conagua:HkW0eiFxfT5iUv31@34.72.69.10/"

table = "Catalogo_unidades"
engine = create_engine(url + db, echo = False)

df = pd.read_csv(path)

#df.to_sql(name = table, con = engine, if_exists = "append", index = False)

path = 'datos-base/catálogos-20240524T201146Z-001/catálogos/cat_parametros.csv'

table = "Catalogo_de_parametros"
df = pd.read_csv(path, skiprows=1)
df = df.drop('unidades_param', axis=1)
df = df.rename(columns = {"nom_param":"cve_nom"})

#df.to_sql(name = table, con = engine, if_exists = "append", index = False)


path = 'datos-base\catálogos-20240524T201146Z-001\catálogos\cat_estacion.csv'
table = "Estado_estacion"
df = pd.read_csv(path, skiprows=1)
df = df.drop(columns = ["cve_estac", "nom_estac", "longitud", "latitud", "alt", "id_station"])
df = df.rename(columns = {"obs_estac":"desc_fecha"})

#df.to_sql(name = table, con = engine, if_exists = "append", index = False)

path = 'datos-base/históricos-20240524T201155Z-001/históricos/meteorología_2013.json'
table = "Catalogo_ciudades"
df_aux = pd.read_json(path)
data = {"city": [df_aux['pollutionMeasurements']['city']], "country": [df_aux['pollutionMeasurements']['country']]}
df = pd.DataFrame(data)

#df.to_sql(name = table, con = engine, if_exists = "append", index = False)
