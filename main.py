<<<<<<< HEAD
import pyautogui
import time
import random
import numpy as np
import cv2

from mouse_engine import HumanMouse
from vision_engine import UnitRecognizer
from brain_engine import MetaBrain

SHOP_REGION = (480, 915, 960, 160)
XP_BUTTON = (360, 950)
BENCH_SLOTS = [
    (420, 740), (530, 740), (640, 740), (750, 740), (860, 740),
    (970, 740), (1080, 740), (1190, 740), (1300, 740)
]
BOARD_SPOTS = [
    (500, 600), (650, 600), (800, 600), (950, 600), (1100, 600), (1250, 600)
]


class TFTFullBot:
    def __init__(self):
        print("--- INICJALIZACJA BOTA ---")
        self.mouse = HumanMouse()
        self.vision = UnitRecognizer()
        self.brain = MetaBrain()
        pyautogui.FAILSAFE = True

    def buy_routine(self):
        screenshot = pyautogui.screenshot(region=SHOP_REGION)
        frame = np.array(screenshot)[:, :, ::-1].copy()  # PIL -> OpenCV
        h, w, _ = frame.shape
        slot_w = w // 5
        bought_something = False
        for i in range(5):
            x_start = i * slot_w
            unit_crop = frame[0:h, x_start:x_start + slot_w]
            name = self.vision.identify_unit(unit_crop)

            if name:
                if self.brain.should_buy(name):
                    print(f"[Shop] Slot {i + 1}: Kupuję {name} (META)")
                    cx = SHOP_REGION[0] + x_start + (slot_w // 2)
                    cy = SHOP_REGION[1] + (h // 2)
                    self.mouse.human_click(cx, cy)
                    bought_something = True
                    time.sleep(random.uniform(0.3, 0.6))

        return bought_something

    def deploy_routine(self):
        if random.randint(1, 4) != 1: return

        print("[Deploy] Próba wystawienia jednostek...")
        slots_to_check = random.sample(range(5), 3)  # Sprawdź 3 losowe sloty z pierwszych 5

        for i in slots_to_check:
            bench_x, bench_y = BENCH_SLOTS[i]
            target_x, target_y = random.choice(BOARD_SPOTS)
            target_x += random.randint(-20, 20)
            target_y += random.randint(-20, 20)
            self.mouse.drag_and_drop(bench_x, bench_y, target_x, target_y)
            time.sleep(random.uniform(0.4, 0.7))

    def economy_routine(self):
        """Zarządzanie złotem - Kupowanie XP"""
        if random.randint(1, 25) == 25:
            print("[Economy] Kupuję XP...")
            self.mouse.human_click(XP_BUTTON[0], XP_BUTTON[1])

    def run(self):
        print("BOT GOTOWY. Przełącz się na grę (Borderless).")
        print("Ctrl+C w konsoli aby zatrzymać.")

        try:
            while True:
                did_buy = self.buy_routine()
                if did_buy or random.random() > 0.7:
                    self.deploy_routine()
                self.economy_routine()
                wait_time = random.uniform(2.0, 4.0) if did_buy else random.uniform(4.0, 6.0)
                time.sleep(wait_time)
        except KeyboardInterrupt:
            print("\nZatrzymano bota.")
        except Exception as e:
            print(f"\nKrytyczny błąd: {e}")
if __name__ == "__main__":
    bot = TFTFullBot()
=======
import pyautogui
import time
import random
import numpy as np
import cv2

from mouse_engine import HumanMouse
from vision_engine import UnitRecognizer
from brain_engine import MetaBrain

SHOP_REGION = (480, 915, 960, 160)
XP_BUTTON = (360, 950)
BENCH_SLOTS = [
    (420, 740), (530, 740), (640, 740), (750, 740), (860, 740),
    (970, 740), (1080, 740), (1190, 740), (1300, 740)
]
BOARD_SPOTS = [
    (500, 600), (650, 600), (800, 600), (950, 600), (1100, 600), (1250, 600)
]


class TFTFullBot:
    def __init__(self):
        print("--- INICJALIZACJA BOTA ---")
        self.mouse = HumanMouse()
        self.vision = UnitRecognizer()
        self.brain = MetaBrain()
        pyautogui.FAILSAFE = True

    def buy_routine(self):
        screenshot = pyautogui.screenshot(region=SHOP_REGION)
        frame = np.array(screenshot)[:, :, ::-1].copy()  # PIL -> OpenCV
        h, w, _ = frame.shape
        slot_w = w // 5
        bought_something = False
        for i in range(5):
            x_start = i * slot_w
            unit_crop = frame[0:h, x_start:x_start + slot_w]
            name = self.vision.identify_unit(unit_crop)

            if name:
                if self.brain.should_buy(name):
                    print(f"[Shop] Slot {i + 1}: Kupuję {name} (META)")
                    cx = SHOP_REGION[0] + x_start + (slot_w // 2)
                    cy = SHOP_REGION[1] + (h // 2)
                    self.mouse.human_click(cx, cy)
                    bought_something = True
                    time.sleep(random.uniform(0.3, 0.6))

        return bought_something

    def deploy_routine(self):
        if random.randint(1, 4) != 1: return

        print("[Deploy] Próba wystawienia jednostek...")
        slots_to_check = random.sample(range(5), 3)  # Sprawdź 3 losowe sloty z pierwszych 5

        for i in slots_to_check:
            bench_x, bench_y = BENCH_SLOTS[i]
            target_x, target_y = random.choice(BOARD_SPOTS)
            target_x += random.randint(-20, 20)
            target_y += random.randint(-20, 20)
            self.mouse.drag_and_drop(bench_x, bench_y, target_x, target_y)
            time.sleep(random.uniform(0.4, 0.7))

    def economy_routine(self):
        """Zarządzanie złotem - Kupowanie XP"""
        if random.randint(1, 25) == 25:
            print("[Economy] Kupuję XP...")
            self.mouse.human_click(XP_BUTTON[0], XP_BUTTON[1])

    def run(self):
        print("BOT GOTOWY. Przełącz się na grę (Borderless).")
        print("Ctrl+C w konsoli aby zatrzymać.")

        try:
            while True:
                did_buy = self.buy_routine()
                if did_buy or random.random() > 0.7:
                    self.deploy_routine()
                self.economy_routine()
                wait_time = random.uniform(2.0, 4.0) if did_buy else random.uniform(4.0, 6.0)
                time.sleep(wait_time)
        except KeyboardInterrupt:
            print("\nZatrzymano bota.")
        except Exception as e:
            print(f"\nKrytyczny błąd: {e}")
if __name__ == "__main__":
    bot = TFTFullBot()
>>>>>>> e48f7e2627e94352550c9ccfe972866c23e1c126
    bot.run()