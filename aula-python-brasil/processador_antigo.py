import re
from playwright.sync_api import Playwright, sync_playwright, expect

ROUND_MAX = 10

def run(playwright: Playwright) -> None:
    round_atual = 1
    browser = playwright.chromium.launch(headless=False, slow_mo=1500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rpachallenge.com/")
    while round_atual <= ROUND_MAX:
        page.locator("label", has_text="Email").locator("xpath=following-sibling::input").fill("g@email.com")
        page.locator("label", has_text="Address").locator("xpath=following-sibling::input").fill("rua das ruas, 555")
        page.locator("label", has_text="First Name").locator("xpath=following-sibling::input").fill("Guilherme")
        page.locator("label", has_text="Company Name").locator("xpath=following-sibling::input").fill("Magalu")
        page.locator("label", has_text="Last Name").locator("xpath=following-sibling::input").fill("Ribeiro")
        page.locator("label", has_text="Role in Company").locator("xpath=following-sibling::input").fill("Analista de Dados")
        page.locator("label", has_text="Phone Number").locator("xpath=following-sibling::input").fill("16991920988")
        page.get_by_role("button", name="Submit").click()
        round_atual += 1

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)