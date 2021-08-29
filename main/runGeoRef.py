import os
import main.manageData.geoRef.databaseTable.createTables as createTables
from definitions import OUTPUT_PATH

FOLDER_NAME = "geoRef"
DATA_PATH = os.path.join(OUTPUT_PATH, FOLDER_NAME)

if __name__ == '__main__':
    createTables.runAllCreateTables()
