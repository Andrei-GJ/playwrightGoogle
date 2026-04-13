from playwright.sync_api import Page
from articlebundle.controller.articleController import getDataClient
from fixtures.locations import getLocations 
from fixtures.areas import getAreas
from fixtures.category import getCategory
import itertools

def test_google_search(page: Page):
    # Esta variable cambiará dinámicamente según tu base de datos
    category = getCategory()
    citys = getLocations()
    areas = getAreas()

    # itertools.product crea todas las combinaciones posibles de una vez
    combinaciones = itertools.product(category, citys, areas)

    # Un solo ciclo compacto
    for category, city, area in combinaciones:
        # Construimos la query dinámica
        query = f"{category} en {city} {area}".strip()
        print(f"--- Iniciando barrido en: {query} ---")
        
        # NAVEGACIÓN DIRECTA: Evita errores de timeout en el buscador
        url_query = query.replace(" ", "+")
        page.goto(f"/maps/search/{url_query}")
                
        try:
            # Esperamos a que cargue al menos un resultado o el panel (máximo 10 seg)
            page.wait_for_selector('div[role="feed"], div[role="article"]', timeout=10000)
                    
            # Procesamos los resultados de esta zona específica
            dataClient = {'name': '', 'phone': ''}
            getDataClient(page, dataClient)
                    
        except Exception:
            print(f"Zona '{area}' sin resultados. Saltando a la siguiente...")
            continue

    print("--- Barrido completo de la metrópolis finalizado ---")