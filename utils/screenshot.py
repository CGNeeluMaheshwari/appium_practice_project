import os
from datetime import datetime


def take_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(path)
