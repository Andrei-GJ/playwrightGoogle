from playwright.sync_api import Page
from articlebundle.controller.articleController import getDataClient

def test_google_search(page: Page):
    page.goto("/maps")
    seccionbuscar = page.get_by_label("Buscar en Google Maps")
    seccionbuscar.fill("Odontologias en bogota")
    page.locator('button[aria-label="Buscar"]').click()
    
    dataClient = {
        'name' : '',
        'phone' : '',
    }
    getDataClient(page, dataClient)