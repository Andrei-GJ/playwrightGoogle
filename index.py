from playwright.sync_api import Page
from articlebundle.controller.articleController import getDataClient

def test_google_search(page: Page):
    # Esta variable cambiará dinámicamente según tu base de datos
    termino_busqueda = "Odontologias en bogota" 
    
    if " en " in termino_busqueda.lower():
        partes = termino_busqueda.lower().split(" en ")
        rubro = partes[0].strip()
        ciudad = partes[-1].strip()
    else:
        rubro = termino_busqueda
        ciudad = ""

    # Barrido Cardinal: Universal para cualquier metrópolis
    # Esto multiplica por 5 el área de cobertura sin hardcodear barrios
    zonas = ["", "Norte", "Sur", "Occidente", "Oriente"]

    for zona in zonas:
        # Construimos la query dinámica
        query = f"{rubro} en {ciudad} {zona}".strip()
        print(f"--- Iniciando barrido en: {query} ---")
        
        # NAVEGACIÓN DIRECTA: Evita errores de timeout en el buscador
        url_query = query.replace(" ", "+")
        page.goto(f"https://www.google.com/maps/search/{url_query}")
        
        try:
            # Esperamos a que cargue al menos un resultado o el panel (máximo 10 seg)
            page.wait_for_selector('div[role="feed"], div[role="article"]', timeout=10000)
            
            # Procesamos los resultados de esta zona específica
            dataClient = {'name': '', 'phone': ''}
            getDataClient(page, dataClient)
            
        except Exception:
            print(f"Zona '{zona}' sin resultados o tardó mucho. Saltando a la siguiente...")
            continue

    print("--- Barrido completo de la metrópolis finalizado ---")
