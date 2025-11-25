import os
from datetime import datetime

def take_screenshot(driver, folder="reports/screenshots"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    path = os.path.join(folder, filename)

    driver.save_screenshot(path)  # Selenium / Appium
    # playwright: await page.screenshot(path=path)

    return path
