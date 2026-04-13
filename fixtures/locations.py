from sqlalchemy import select
from database.connect.dataBaseConnect import connectDB, engine, MetaData, Table

# class locations:
locations = Table('locations', MetaData(), autoload_with=engine)
def getLocations():
    print("Obteniendo ubicaciones")
    connectDB()
    try:
        with engine.connect() as conn:
            check_stmt = select(locations.c.name).where(locations.c.active == True)
            result = conn.execute(check_stmt).fetchall()
            result = list(zip(*result))[0]
            return result
    except Exception as e:
        print(e)
        return e
    finally:
        conn.close()    
        engine.dispose()