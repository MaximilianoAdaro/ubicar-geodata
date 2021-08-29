def runAllCreateTables():
    import main.manageData.geoRef.databaseTable.state.StateData as StateData
    import main.manageData.geoRef.databaseTable.state.StateCleanJson as StateCleanJson

    import main.manageData.geoRef.databaseTable.cities.CityData as CityData
    import main.manageData.geoRef.databaseTable.cities.CityCleanJson as CityCleanJson

    from main.config.postgresConnection import connectAndExcecute

    print("-----------------------------------------------------------------------------------------------------------")

    """State"""
    dataName = 'state'
    connectAndExcecute(StateData.createStateGeomDataTable, dataName)
    connectAndExcecute(StateCleanJson.importStateGeomData, dataName)

    print("-------------------------------------------------------------------------------------------------------")

    """City"""
    dataName = 'city'
    connectAndExcecute(CityData.createCityGeomDataTable, dataName)
    connectAndExcecute(CityCleanJson.importCityGeomData, dataName)


if __name__ == '__main__':
    runAllCreateTables()
