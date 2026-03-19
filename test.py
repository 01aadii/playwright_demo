from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file://" + __import__("os").path.abspath("index.html"))
    page.fill("#search", "Playwright Test")
    page.click("#btn")
    print(page.text_content("#title"))
    browser.close()
