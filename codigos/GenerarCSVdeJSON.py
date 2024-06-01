import pandas as pd

dict_aux = {"mesurementAgency": [], "parametro": [], "fecha": [], "hora": [],"estacion":[], "valor": [], "anio": []}

i = 2013
s = ""
t = ""

for i in range(2013, 2024):
    aux_fecha = -1
    path = "datos-base/históricos-20240524T201155Z-001/históricos/meteorología_"+str(i)+".json"
    df = pd.read_json(path)
    dias = [key for key in dict(df['pollutionMeasurements']['date']).keys()]
    #Enero
    for j in range(1,32):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-01-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Febrero
    #Por si es bisiesto
    if i%4 == 0:
        for j in range(1,30):
            if j<10:
                s = "0"
            else:
                s = ""
            for k in range(1,25):
                aux_fecha += 1
                if k<10:
                    t = "0"
                else:
                    t = ""
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('RH')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('TMP')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('WSP')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('WDR')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('PBa')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
    else:
        for j in range(1,29):
            if j<10:
                s = "0"
            else:
                s = ""
            for k in range(1,25):
                aux_fecha += 1
                if k<10:
                    t = "0"
                else:
                    t = ""
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('RH')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('TMP')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('WSP')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('WDR')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
                for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                    dict_aux["mesurementAgency"].append("SIMAT")
                    dict_aux["parametro"].append('PBa')
                    dict_aux["estacion"].append(key)
                    dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-02-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                    dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                    dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                    dict_aux["anio"].append(i)
    #Marzo
    for j in range(1,32):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-03-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Abril
    for j in range(1,31):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-04-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Los registros de 2023 llegan hasta abril
    if i == 2023:
        break
    #Mayo
    for j in range(1,32):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-05-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Junio
    for j in range(1,31):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-06-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Julio
    for j in range(1,32):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-07-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Agosto
    for j in range(1,32):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-08-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Septiembre
    for j in range(1,31):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-09-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Octubre
    for j in range(1,32):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-10-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Noviembre
    for j in range(1,31):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-11-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
    #Diciembre
    for j in range(1,32):
        if j<10:
            s = "0"
        else:
            s = ""
        for k in range(1,25):
            aux_fecha += 1
            if k<10:
                t = "0"
            else:
                t = ""
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['RH']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('RH')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['RH'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('TMP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['TMP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WSP')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['WSP'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('WDR')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['WDR'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
            for key, value_date in dict(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa']).items():
                dict_aux["mesurementAgency"].append("SIMAT")
                dict_aux["parametro"].append('PBa')
                dict_aux["estacion"].append(key)
                dict_aux["valor"].append(df['pollutionMeasurements']['date'][str(i) + '-12-' + s + str(j) + ' ' + t + str(k) + ':00']['PBa'][key])
                dict_aux["fecha"].append(str(dias[aux_fecha]).split(" ")[0])
                dict_aux["hora"].append(str(dias[aux_fecha]).split(" ")[1])
                dict_aux["anio"].append(i)
        
df = pd.DataFrame(dict_aux)
df.to_csv("meteorologia_json.csv", index = False)
   