import pandas as pd

edf=pd.read_csv('eod.csv')
cdf=pd.read_csv('comunas.csv',delimiter=';')

cd={row['Id']:row['Comuna'] for _,row in cdf.iterrows()}
edf['Origen']=edf.ComunaOrigen.apply(lambda ori: cd.get(ori))
edf['Destino']=edf.ComunaDestino.apply(lambda ori: cd.get(ori))

cerco=['LAS CONDES','PROVIDENCIA','VITACURA','LO BARNECHEA','LA REINA','ÑUÑOA','INDEPENDENCIA']
edf['ori_in']=edf.Origen.isin(cerco)
edf['des_in']=edf.Destino.isin(cerco)
edf['ori_des']=[(row['ori_in'],row['des_in']) for _,row in edf.iterrows()]
edf['cruza']=edf['ori_in']!=edf['des_in']

print(edf.cruza.value_counts(normalize=True))