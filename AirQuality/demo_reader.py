from openaq import OpenAQ
import geojson

api=OpenAQ()

locs=api.locations(country='CL', df=True, limit=1000)
print(f'Found {len(locs)} locations in Chile')

glocs = [geojson.Point((loc['coordinates.latitude'],
                        loc['coordinates.longitude']))
                         for _, loc in locs.iterrows()]

fc=geojson.FeatureCollection([geojson.Feature(gloc) for gloc in glocs])
geojson.dump(fc, open('chile.json','w'))

last=api.latest(country='CL', df=True, limit =10000)
print(f'latest records: {len(last)}')

last=last[last.value>0]
print(last.groupby(['parameter']).agg(['min','mean','max'])['value'].round(2))
last.to_csv('aire.csv', index=False)  # make geoJson!

print('BAD BOYS:')
print(last[last.parameter=='so2'].sort_values('value').tail())
