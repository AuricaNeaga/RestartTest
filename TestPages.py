import asyncio
import shutil
from pyppeteer import launch
from filecmp import dircmp
import pathlib


dirpath = pathlib.Path("Output")
if dirpath.is_dir():
    shutil.rmtree(dirpath)
dirpath.mkdir(parents=True, exist_ok=False)

async def main():
    args = ['--window-size=1920,1080','--start-maximized', '--disable-infobars']
    browser = await launch(headless = True, args = args);
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto('https://landingpage-dev.redplatform.com/en/')
    await page.screenshot({'path': 'Output/home.png'})
    await page.goto('https://landingpage-dev.redplatform.com/en/earn-from-energy/')
    await page.screenshot({'path': 'Output/earn-from-energy.png'})
    await page.goto('https://landingpage-dev.redplatform.com/en/gtk-for-manufacturers/')
    await page.screenshot({'path': 'Output/gtk-for-manufacturers.png'})
    await page.goto('https://landingpage-dev.redplatform.com/en/green-certification-for-companies/')
    await page.screenshot({'path': 'Output/green-certification-for-companies.png'})
    await page.goto('https://landingpage-dev.redplatform.com/en/red-for-suppliers/')
    await page.screenshot({'path': 'Output/red-for-suppliers.png'})
    await page.goto('https://landingpage-dev.redplatform.com/en/faq/')
    await page.screenshot({'path': 'Output/faq.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
dcmp = dircmp('Output', 'Expected')
print("Check differences in files: ", dcmp.diff_files)
