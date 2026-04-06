from sqlalchemy import true
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, insert

# Carga las variables del archivo .env
load_dotenv()


# Accede a las variables de entorno
db_url = os.getenv('DATABASE_URL')
engine = create_engine(db_url)

def connectDB():
    if engine:
        try:
            with engine.connect() as conn:
                return True
        except Exception as e:
            return (e)
    else:
        return ("No se encontro la variable de entorno DATABASE_URL")