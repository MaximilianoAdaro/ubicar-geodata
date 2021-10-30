"""MultiPolygonData"""
availableIgnLayersMultiPolygon = ["multi_polygon_manufacturing_and_processing_area"]

"""MultiLineStringData"""
availableIgnLayersMultiLine = ["multi_line_string_railway"]
# availableIgnLayersMultiLine = ['multi_line_string_railway', 'multi_line_string_national_route', 'multi_line_string_state_route']

"""PointData"""
availableIgnLayersPoint = \
    ["point_airport", "point_fire_station", "point_penitentiary", "point_security_building",
     "point_educational_establishment", "point_health_building", "point_train_station",
     "point_port", "point_university"]

"""PointDataCiudad"""
availableIgnLayersPointCiudad = ["point_subway_station"]


def runAllCreateTables():
    import main.manageData.geoEspatialData.databaseTable.MultiPolygonGeomData.MultiPolygonData as MultiPolygonData
    import \
        main.manageData.geoEspatialData.databaseTable.MultiPolygonGeomData.MultiPolygonCleanJson as MultiPolygonCleanJson

    import \
        main.manageData.geoEspatialData.databaseTable.MultiLineStringGeomData.MultiLineStringData as MultiLineStringData
    import \
        main.manageData.geoEspatialData.databaseTable.MultiLineStringGeomData.MultiLineStringCleanJson as MultiLineStringCleanJson

    import main.manageData.geoEspatialData.databaseTable.PointGeomData.PointData as PointData
    import main.manageData.geoEspatialData.databaseTable.PointGeomData.PointCleanJson as PointCleanJson

    import main.manageData.geoEspatialData.databaseTable.PointSubwayCiudadGeomData.PointSubwayCiudadData as PointCiudadData
    import main.manageData.geoEspatialData.databaseTable.PointSubwayCiudadGeomData.PointSubwayCiudadCleanJson as PointCiudadCleanJson

    from main.config.postgresConnection import connectAndExcecute

    print("-----------------------------------------------------------------------------------------------------------")

    """MultiPolygonData"""
    for dataName in availableIgnLayersMultiPolygon:
        connectAndExcecute(MultiPolygonData.createMultiPolygonGeomDataTable, dataName)
        connectAndExcecute(MultiPolygonCleanJson.importMultiPolygonGeomData, dataName)
        print("-------------------------------------------------------------------------------------------------------")

    """PointData SubwayCiudad"""
    for dataName in availableIgnLayersPointCiudad:
        connectAndExcecute(PointCiudadData.createPointGeomDataTable, dataName)
        connectAndExcecute(PointCiudadCleanJson.importPointGeomData, dataName)
        print("-------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    runAllCreateTables()
