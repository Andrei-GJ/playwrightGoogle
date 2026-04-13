from sqlalchemy import select
from database.connect.dataBaseConnect import connectDB, engine, MetaData, Table

# class areas:
areas = Table('areas', MetaData(), autoload_with=engine)
def getAreas():
    print("Obteniendo areas")
    connectDB()
    try:
        with engine.connect() as conn:
            check_stmt = select(areas.c.name)
            result = conn.execute(check_stmt).fetchall()
            result = list(zip(*result))[0]
            print(result)
            return result
    except Exception as e:
        print(e)
        return e
    finally:
        conn.close()    
        engine.dispose()