from sqlalchemy import select
from database.connect.dataBaseConnect import connectDB, engine, MetaData, Table

# class category:
category = Table('category', MetaData(), autoload_with=engine)
def getCategory():
    print("Obteniendo category")
    connectDB()
    try:
        with engine.connect() as conn:
            check_stmt = select(category.c.name).where(category.c.active == True)
            result = conn.execute(check_stmt).fetchall()
            result = list(zip(*result))[0]
            return result
    except Exception as e:
        print(e)
        return e
    finally:
        conn.close()    
        engine.dispose()