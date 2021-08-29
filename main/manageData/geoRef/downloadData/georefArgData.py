import json
import urllib.request

from main.manageData.geoEspatialData.downloadData.geoData import createDir


# Download the file from URL
def downloadData(urlToDownload, fileTitle):
    print(f'From {urlToDownload} downloading...')

    try:
        with urllib.request.urlopen(urlToDownload) as url:
            data = json.loads(url.read().decode())

        # Write to file
        fn = f'{fileTitle}.json'
        with open(fn, 'w') as fh:
            fh.write(data)
            fh.close()
        print(f'Downloading: {fileTitle}')
    except Exception as error:
        print(f'Exception in {fileTitle}: {error}')


urlToDownload = "https://apis.datos.gob.ar/georef/api/localidades.json"

if __name__ == '__main__':
    createDir('./output/geoRef')

    downloadData(urlToDownload, "localidades")
