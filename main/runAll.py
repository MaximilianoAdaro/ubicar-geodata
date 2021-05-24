import os
import manageData.downloadData.geoData as geoDataDownload
import manageData.databaseTable.createTables as createTables
from definitions import OUTPUT_PATH

FOLDER_NAME = "geojsonData6"
DATA_PATH = os.path.join(OUTPUT_PATH, FOLDER_NAME)

if __name__ == '__main__':
    geoDataDownload.createDir(DATA_PATH)
    geoDataDownload.runDownloads()
    createTables.runAllCreateTables()
