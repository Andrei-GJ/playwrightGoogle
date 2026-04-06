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
            updateClient = insert(Contacts).values(
                name=dataContact['name'], 
                phone=dataContact['phone'],
                hasContact=dataContact['hasContact']
            )
            conn.execute(updateClient)
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
        engine.dispose()

    