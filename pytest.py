import os
import shutil

from owslib.wfs import WebFeatureService

# Datos a obtener:
# Escuelas, universidades, hospitales y centros de salud, policía y bomberos
# Transporte público, rutas, autopistas, puertos y aeropuertos

# wfs_url = 'http://mapa.educacion.gob.ar/geoserver/ows?service=wfs&version=1.1.0&request=GetCapabilities'

# Transport data
# Colectivos - Estaciones - Puertos - Ferrocarril - Subtes - Ruta Nacional / Provincial
wfs_url = 'https://ide.transporte.gob.ar/geoserver/ows?service=wfs&version=1.3.0&request=GetCapabilities'

# Hospitales privados / publios
# wfs_url = 'http://ide.sedronar.gov.ar/geoserver/wfs'

# Universidades
# wfs_url = 'http://mapa.educacion.gob.ar/geoserver/ows?version=1.1.0'

# Connect to GeoServer WFS service.
wfs = WebFeatureService(wfs_url, version='2.0.0')

keys = wfs.contents.keys()
total_files = len(keys)

# print("KEYS")
# for key, value in wfs.contents.items():
#     print(f'{value.title} --> {key}')

dir = './output2'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
os.chdir(dir)

print(f'files to create: {total_files}')
created_num = 0

for key in sorted(keys):
    print(f'{total_files - created_num} files remaining')

    try:
        data = wfs.getfeature(typename=key, outputFormat='JSON')
        # Write to file
        fn = f'{key}.geojson'
        with open(fn, 'wb') as fh:
            fh.write(data.read().encode())
    except Exception as error:
        print(f'Exception in {key}: {error}')

    created_num += 1
