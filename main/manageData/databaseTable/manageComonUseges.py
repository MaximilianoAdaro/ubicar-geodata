def deleteAllNotAppearingInNewData(allGId, cursor, tableName):
    toBeRemoved = []
    cursor.execute(f"""
        select gid from \"{tableName}\"
""")

    for elem in cursor.fetchall():
        toRemoveElem = elem[0]
        if toRemoveElem not in allGId:
            toBeRemoved.append(toRemoveElem)

    # We only delete if the items to be deleted are less than 20% of all data of that type.
    # Otherwise, we won't delete all the data if something went wrong.
    print("toBeRemoved", tableName, toBeRemoved)
    if len(toBeRemoved) < (0.2 * len(allGId)):
        for remove in toBeRemoved:
            cursor.execute(f"""
            delete from \"{tableName}\"
            where gid = {remove}
            """)
