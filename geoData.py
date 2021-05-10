import os
import shutil
from datetime import datetime

from owslib.wfs import WebFeatureService

### Datos a obtener:
# - hospitales y centros de salud, policía y bomberos
# - Transporte público, puertos y aeropuertos

# Ministerio de Defensa
wfs_url = 'http://wms.ign.gob.ar/geoserver/wfs'
# Aeropuerto / Cuartel de bomberos / Institucion penitenciaria / Edificio de seguridad / Establecimiento Educativos
# Edificio de salud / Estacion de ferrocarril / Ferrocarril / Puerto / Universidad

# Ministerio de Transporte
# wfs_url = 'http://ide.transporte.gob.ar/geoserver/ows?service=wfs&version=1.3.0&request=GetCapabilities'
# Rutas Nacionales / Rutas Provinciales

# Ministerio de Educación
# wfs_url = 'http://mapa.educacion.gob.ar/geoserver/ows?service=wfs&version=1.1.0&request=GetCapabilities'

### Transport data
# wfs_url = 'https://ide.transporte.gob.ar/geoserver/ows?service=wfs&version=1.3.0&request=GetCapabilities'
# Colectivos - Estaciones - Puertos - Ferrocarril - Subtes - Ruta Nacional / Provincial


### Hospitales privados / publios


# Connect to GeoServer WFS service.
wfs = WebFeatureService(wfs_url, version='2.0.0')
print(wfs_url)

keys = wfs.contents.keys()
total_files = len(keys)

print("KEYS")
for key, value in wfs.contents.items():
    print(f'{value.title}')

dir = './output5'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)
os.chdir(dir)

print(f'files to create: {total_files}')
created_num = 0

timeBefore = datetime.now()
print("Time before: ", timeBefore)

for key, value in sorted(wfs.contents.items()):
    print(f'{total_files - created_num} files remaining')

    try:
        data = wfs.getfeature(typename=key, outputFormat='JSON')
        # Write to file
        fn = f'{value.title}.json'
        with open(fn, 'wb') as fh:
            fh.write(data.read().encode())
    except Exception as error:
        print(f'Exception in {value.title}: {error}')

    created_num += 1

timeAfter = datetime.now()
print("Time after: ", timeAfter)

timeDiff = timeAfter - timeBefore

value = divmod(timeDiff.total_seconds(), 60)
print(f"Minutes: {value[0]}, Seconds: {value[1]}")
