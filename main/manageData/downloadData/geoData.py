import os
import shutil
from datetime import datetime

from owslib.wfs import WebFeatureService


# Create directory and save files on it
def createDir(dirName):
    if os.path.exists(dirName):
        shutil.rmtree(dirName)
    os.makedirs(dirName)
    os.chdir(dirName)


# Connect to GeoServer WFS service
def getWFS(wfsUrl):
    return WebFeatureService(wfsUrl, version='2.0.0')


# Download the available layers from wfs url
def downloadData(wfsUrl, availableLayers):
    print(f'From {wfsUrl} downloading...')

    wfs = getWFS(wfsUrl)
    contents = wfs.contents
    items = contents.items()

    for key, value in sorted(items):
        title = value.title
        if title in availableLayers:
            try:
                data = wfs.getfeature(typename=key, outputFormat='json')
                # Write to file
                fn = f'{title}.geojson'
                with open(fn, 'wb') as fh:
                    encodedData = data.read().encode()
                    fh.write(encodedData)
                print(f'Downloading: {title}')
            except Exception as error:
                print(f'Exception in {title}: {error}')


# Start downloading
def runDownloads():
    createDir('./output/geojsonData2')
    downloadData(wfsIgnUrl, availableIgnLayers)
    downloadData(wfsRouteUrl, availableRouteLayers)


###---------------------------------------------------------------------------------------------------------------------

""""Ministerio de Defensa"""
# Aeropuerto / Cuartel de bomberos / Institucion penitenciaria / Edificio de seguridad / Establecimiento Educativos
# Edificio de salud / Estacion de ferrocarril / Ferrocarril / Puerto / Universidad
wfsIgnUrl = 'http://wms.ign.gob.ar/geoserver/wfs'
availableIgnLayers = ['Aeropuerto', 'Área de fabricación y procesamiento', 'Cuartel de bomberos',
                      'Institución penitenciaria', 'Edificio de seguridad', 'Establecimiento educativo',
                      'Edificio de salud', 'Estación de ferrocarril', 'Ferrocarril', 'Puerto', 'Universidad']

"""Ministerio de Transporte"""
# Rutas Nacionales / Rutas Provinciales
wfsRouteUrl = 'http://ide.transporte.gob.ar/geoserver/ows?service=wfs&version=1.3.0&request=GetCapabilities'
availableRouteLayers = ['Rutas Nacionales', 'Rutas Provinciales']

###---------------------------------------------------------------------------------------------------------------------

### TIME BEFORE
timeBefore = datetime.now()

### Download geo data from layers
if __name__ == "__main__":
    runDownloads()

### TIME AFTER
timeAfter = datetime.now()
timeDiff = timeAfter - timeBefore

timeParsed = divmod(timeDiff.total_seconds(), 60)
print(f"Minutes: {timeParsed[0]}, Seconds: {timeParsed[1]}")
