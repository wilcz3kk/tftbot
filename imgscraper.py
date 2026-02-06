import pyautogui
import time
import os
from datetime import datetime

SHOP_REGION = (450, 910, 1050, 150)  # (x, y, szerokość, wysokość)
SAVE_PATH = "tft_dataset/shop_images"
INTERVAL = 5  # sekundy
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)
def collect_data():
    print(f"Rozpoczynam zbieranie danych. Zrzut co {INTERVAL}s.")
    print("Przełącz się na okno gry! (Ctrl+C aby zatrzymać)")
    count = 0
    try:
        while True:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{SAVE_PATH}/shop_{timestamp}_{count}.png"
            screenshot = pyautogui.screenshot(region=SHOP_REGION)
            screenshot.save(filename)
            print(f"Zapisano: {filename}")
            count += 1
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print(f"\nZatrzymano. Zebrano {count} zdjęć w folderze {SAVE_PATH}.")
if __name__ == "__main__":
    collect_data()