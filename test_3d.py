import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Capture console logs
        page.on('console', lambda msg: print(f"CONSOLE: {msg.text}"))
        
        print("Navigating to page...")
        await page.goto('file:///D:/googleAntigravity/Du_An/74HC595/Interactive_Wiring_Diagram.html')
        await page.wait_for_timeout(2000)
        
        print("Clicking 3D button...")
        # Evaluate Javascript to find and click the toggle button
        await page.evaluate('''() => {
            const btn = Array.from(document.querySelectorAll("button")).find(b => b.textContent.includes("SƠ ĐỒ 2D"));
            if (btn) {
                console.log("Found SƠ ĐỒ 2D button, clicking...");
                btn.click();
            } else {
                console.log("Could not find SƠ ĐỒ 2D button!");
            }
        }''')
        
        await page.wait_for_timeout(2000)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
