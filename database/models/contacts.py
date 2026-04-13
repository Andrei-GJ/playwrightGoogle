from sqlalchemy import select
from database.connect.dataBaseConnect import connectDB, engine, MetaData, Table, insert

# class Contacts:
Contacts = Table('contacts', MetaData(), autoload_with=engine)

def updateContact(dataContact):
    # Limpiamos todos los caracteres que no sean números
    # dataContact = {'name': 'odontología Emanuel', 'phone': 'Teléfono: 313 4842702 '}
    # Limpiamos para que quede solo números
    phone_clean = ''.join(filter(str.isdigit, dataContact['phone']))

    dataContact['phone'] = phone_clean

    print(dataContact)
    if not dataContact.get('hasContact'):
        dataContact.setdefault('hasContact', False)
    
    connectDB()

    try:
        with engine.connect() as conn:
            # 1. Consultamos si el teléfono ya existe en la BD
            check_stmt = select(Contacts).where(Contacts.c.phone == dataContact['phone'])
            result = conn.execute(check_stmt).fetchone()
            
            # 2. Si no existe un resultado (es decir, es nuevo), ejecutamos el insert
            if not result:
                updateClient = insert(Contacts).values(
                    name=dataContact['name'], 
                    phone=dataContact['phone'],
                    hasContact=dataContact['hasContact']
                )
                conn.execute(updateClient)
                conn.commit()
            # Si ya existe, no intentamos insertar y así evitamos quemar un auto-incremental (ID)
    except Exception as e:
        print(f"Error guardando contacto en BD: {e}")