from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the html file
        file_path = os.path.abspath("test_preview.html")
        page.goto(f"file://{file_path}")

        # Wait a bit for any animations or fonts
        page.wait_for_timeout(1000)

        # Take a screenshot
        screenshot_path = os.path.abspath("verification/theme_preview.png")
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
