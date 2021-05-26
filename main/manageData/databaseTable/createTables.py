"""MultiPolygonData"""
availableIgnLayersMultiPolygon = ['Área de fabricación y procesamiento']

"""MultiLineStringData"""
availableIgnLayersMultiLine = ['Ferrocarril']

"""PointData"""
availableIgnLayersPoint = \
    ['Cuartel de bomberos', 'Institución penitenciaria', 'Edificio de seguridad',
     'Establecimiento educativo', 'Edificio de salud', 'Estación de ferrocarril', 'Puerto', 'Universidad']


def runAllCreateTables():
    import main.manageData.databaseTable.MultiPolygonGeomData.MultiPolygonData as MultiPolygonData
    import main.manageData.databaseTable.MultiPolygonGeomData.MultiPolygonCleanJson as MultiPolygonCleanJson

    import main.manageData.databaseTable.MultiLineStringGeomData.MultiLineStringData as MultiLineStringData
    import main.manageData.databaseTable.MultiLineStringGeomData.MultiLineStringCleanJson as MultiLineStringCleanJson

    import main.manageData.databaseTable.PointGeomData.PointData as pointData
    import main.manageData.databaseTable.PointGeomData.PointCleanJson as pointCleanJson

    from main.config.postgresConnection import connectAndExcecute

    print("-----------------------------------------------------------------------------------------------------------")

    """MultiPolygonData"""
    for dataName in availableIgnLayersMultiPolygon:
        connectAndExcecute(MultiPolygonData.createMultiPolygonGeomDataTable, dataName)
        connectAndExcecute(MultiPolygonCleanJson.importMultiPolygonGeomData, dataName)
        print("-------------------------------------------------------------------------------------------------------")

    """MultiLineStringData"""
    for dataName in availableIgnLayersMultiLine:
        connectAndExcecute(MultiLineStringData.createMultiPointGeomDataTable, dataName)
        connectAndExcecute(MultiLineStringCleanJson.importMultiPointGeomData, dataName)
        print("-------------------------------------------------------------------------------------------------------")

    """PointData"""
    for dataName in availableIgnLayersPoint:
        connectAndExcecute(pointData.createPointGeomDataTable, dataName)
        connectAndExcecute(pointCleanJson.importPointGeomData, dataName)
        print("-------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    runAllCreateTables()
