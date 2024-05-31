from sqlalchemy import create_engine
import pandas as pd

db = "conagua"
url = "mysql+mysqlconnector://bd_conagua:HkW0eiFxfT5iUv31@34.72.69.10/"
path = "datos-base/catálogos-20240524T201146Z-001/catálogos/cat_parametros.csv"
engine = create_engine(url + db, echo = False)

table = "Unidad_parametro"
table_one = "Catalogo_unidades"
table_two = "Catalogo_de_parametros"

df_aux = pd.read_csv(path, skiprows=1)
df_one = pd.read_sql_table(table_one, engine)
df_two = pd.read_sql_table(table_two, engine)
df_aux = df_aux.drop(columns = ["id_parameter", "nom_param"])
df_two = df_two.drop(columns = ["cve_nom"])
cve_aux = []
unid_param_aux = []

for i in range(0, len(df_aux['unidades_param'].to_list())):
    if str(df_aux['unidades_param'].to_list()[i]).split(',') == str(df_aux['unidades_param'].to_list()[i]):
        cve_aux.append(df_aux['cve_param'].to_list()[i])
        unid_param_aux.append(df_aux['unidades_param'].to_list()[i])
    else:
        for j in range(0, len(str(df_aux['unidades_param'].to_list()[i]).split(','))):
            cve_aux.append(df_aux['cve_param'].to_list()[i])
            unid_param_aux.append(str(df_aux['unidades_param'].to_list()[i]).split(',')[j])
dict_aux = {"cve_param":cve_aux, "unidades_param":unid_param_aux}
df = pd.DataFrame(dict_aux)
df = df.merge(df_two, left_on="cve_param", right_on="cve_param", how = 'inner')
df = df.drop(columns = ["cve_param"])
df = df.rename(columns = {"unidades_param":"id_unidad"})

#df.to_sql(name = table, con = engine, if_exists = "append", index = False)
