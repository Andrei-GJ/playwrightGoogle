from playwright.sync_api import Page
from articlebundle.controller.articleController import getDataClient
from fixtures.locations import getLocations 
from fixtures.areas import getAreas
from fixtures.category import getCategory
import itertools
import pytest

# Obtenemos las combinaciones en tiempo de importación/colección (para pytest)
combinaciones = list(itertools.product(getCategory(), getLocations(), getAreas()))

@pytest.mark.parametrize("category, city, area", combinaciones)
def test_google_search(page: Page, category, city, area):
    # Construimos la query dinámica
    query = f"{category} en {city} {area}".strip()
    print(f"--- Iniciando barrido en: {query} ---")
    
    # NAVEGACIÓN DIRECTA: Evita errores de timeout en el buscador
    url_query = query.replace(" ", "+")
    # Al estar en headless, Google suele dejar requests colgando y dar Timeout en load. Solo esperamos domcontentloaded.
    page.goto(f"/maps/search/{url_query}", timeout=60000, wait_until="domcontentloaded")
            
    try:
        # Esperamos a que cargue al menos un resultado o el panel (máximo 10 seg)
        page.wait_for_selector('div[role="feed"], div[role="article"]', timeout=10000)
                
        # Procesamos los resultados de esta zona específica
        dataClient = {'name': '', 'phone': ''}
        getDataClient(page, dataClient)
                
    except Exception:
        print(f"Zona '{query}' sin resultados.")

    print(f"--- Barrido de '{query}' finalizado ---")