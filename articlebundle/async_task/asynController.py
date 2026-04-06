import threading
from dotenv import load_dotenv

from database.models.contacts import updateContact

load_dotenv()

def saveClientData(dataClient):
    # Crear y empezar un hilo (thread) para que no bloquee el hilo principal
    thread = threading.Thread(target=updateContact, args=(dataClient,))
    thread.start()