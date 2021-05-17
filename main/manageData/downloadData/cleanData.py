from datetime import datetime

from main.manageData.downloadData.geoData import getWFS, createDir


# Download the available layers from wfs url
def downloadData(wfsUrl, availableLayers):
    print(f'From {wfsUrl} downloading...')

    wfs = getWFS(wfsUrl)
    items = wfs.contents.items()

    for key, value in sorted(items):
        title = value.title
        if title in availableLayers:
            try:
                data = wfs.getfeature(typename=key, outputFormat='json')
                # Write to file
                fn = f'{title}.geojson'
                with open(fn, 'wb') as fh:
                    data_read = data.read()

                    encodedData = data_read.encode()
                    fh.write(encodedData)
                print(f'Downloading: {title}')
            except Exception as error:
                print(f'Exception in {title}: {error}')


###---------------------------------------------------------------------------------------------------------------------

### Ministerio de Defensa
wfsIgnUrl = 'http://wms.ign.gob.ar/geoserver/wfs'
availableIgnLayers = ['Aeropuerto']

###---------------------------------------------------------------------------------------------------------------------

### TIME BEFORE
timeBefore = datetime.now()

createDir('./output3')
downloadData(wfsIgnUrl, availableIgnLayers)

### TIME AFTER
timeAfter = datetime.now()
timeDiff = timeAfter - timeBefore

timeParsed = divmod(timeDiff.total_seconds(), 60)
print(f"Minutes: {timeParsed[0]}, Seconds: {timeParsed[1]}")
