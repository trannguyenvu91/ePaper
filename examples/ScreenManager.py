from playwright.sync_api import sync_playwright
from PhotoManager import getImagePathToDisplay
import os

with sync_playwright() as p:
    html_file = os.path.join(os.path.dirname(__file__), "ScreenLayout.html")
    screenshot_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cache/screenshot.png")
    image_path = getImagePathToDisplay()
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        viewport={"width": 800, "height": 600}
    )
    # Pass parameter via query string
    page.goto(f"file://{html_file}?src=file://{image_path}")
    page.screenshot(path=screenshot_path, full_page=True)
    browser.close()