import os, time, pandas as pd
DATA = os.getenv('DATA_FOLDER')
#GEOCGR_FOLDER = os.path.join(DATA_FOLDER,'por-tema/4_proyectos_priv-y-publ/geo-cgr')
carpeta_salida = 'por-tema/4_proyectos_priv-y-publ/geo-cgr/1-originales'
#GEOCGR_FOLDER = os.path.join(DATA_FOLDER,'GeoCGR')
#sftp://3.209.62.189/home/bitnami/DATA/por-tema/4_proyectos_priv-y-publ/geo-cgr/1-originales
print('FOLDER', carpeta_salida)
comunas = pd.read_excel('cut_2018_v03.xls')      # esto debiera vivir en una API
#fuente: http://www.subdere.gov.cl/sites/default/files/documentos/cut_2018_v03.xls

url_base='https://www.contraloria.cl/opencgrapp/geocgr/api/comunas/%05d/newobras'
t0 = time.time()
sdf = pd.DataFrame()
print(f'TOTAL comunas: {len(comunas)}')

for ix, row in comunas.iterrows():
    url = url_base %(row['Código Comuna 2017'])
    udf = pd.read_json(url)
    comuna = row['Nombre Comuna']
    udf['comuna'] = comuna
    udf['provincia'] = row['Nombre Provincia']
    udf['código_comuna'] = row['Código Comuna 2017']
    udf['región'] = row['Código Región']
    #udf.to_json(f"COMUNAS/{comuna}.json")        # to geo_json??
    sdf = sdf.append(udf, sort=False)
    if ix%20==10:
        print(f'[{ix}/{len(comunas)}]','Region=',row['Código Región'],len(sdf),round(time.time()-t0,2))
    #tc = time.time()
    #sdf.to_parquet(f'base_temp_{ix}_{tc}.pq')
    del udf

filename = f'base_geocgr_{time.strftime("%Y%m%d")}.pq'

full_path = os.path.join(DATA, carpeta_salida, filename)
print(f'{len(sdf)} contratos grabados en {full_path}')
sdf.to_parquet(full_path)
