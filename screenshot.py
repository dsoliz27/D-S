import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Load the local index.html using the absolute path
        file_path = os.path.abspath("index.html")
        await page.goto(f"file://{file_path}")

        # Wait a moment to render
        await page.wait_for_timeout(2000)

        # Set viewport size to capture a great desktop view
        await page.set_viewport_size({"width": 1280, "height": 1800})

        # Take a screenshot of the page
        await page.screenshot(path="screenshot.png", full_page=True)
        print("Screenshot taken successfully!")

        await browser.close()

asyncio.run(main())
