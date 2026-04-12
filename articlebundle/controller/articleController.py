from playwright.sync_api import Page
import threading
from articlebundle.async_task.asynController import saveClientData

def getDataClient(page: Page, dataClient):
    articles = page.get_by_role("article")
    articles.first.wait_for()

    i = 0
    while True:
        articles = page.get_by_role("article")

        if i >= articles.count():
            if not validateEndList(page):
                break
            if i >= page.get_by_role("article").count():
                break
            continue

        article = articles.nth(i)
        i += 1

        if article.locator('h1[aria-label="Patrocinado"]').count() > 0:
            continue
        if article.locator('a[data-value="Sitio web"], button[data-value="Sitio web"]').count() > 0:
            continue

        name = article.locator("a[aria-label]").first.get_attribute("aria-label")
        article.click()

        sliderArticle = page.get_by_role("main", name=name)
        phone = sliderArticle.locator('button[aria-label*="Teléfono"]')

        if phone.count() > 0:
            dataClient = {
                'name' : '',
                'phone' : '',
            }
            dataClient = setDataClient(name, dataClient, phone)
            # print(dataClient)

def setDataClient(name, dataClient, phone):
    dataClient['name'] = name
    dataClient['phone'] = phone.get_attribute("aria-label")
    return saveClientData(dataClient)

def validateEndList(page: Page):
    if page.get_by_text("Has llegado al final de la lista.").count() > 0:
        return False
    
    # Intentamos localizar el panel de resultados (feed)
    panel = page.locator('div[role="feed"]')
    if panel.count() > 0:
        panel.evaluate("el => el.scrollTop = el.scrollHeight")
        page.wait_for_timeout(2000) # Un poco más de tiempo para el scroll
        return True
    
    # Si no hay panel, puede que haya pocos resultados y ya terminaron
    return False