<<<<<<< HEAD
import time
import json
import random
import numpy as np
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


# --- MODUŁ 1: SCRAPER (Mózg Statystyczny) ---
class MetaScraper:
    def __init__(self):
        self.url = "https://tactics.tools/units"
        self.meta_data = {}

    def update_meta(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url, wait_until="networkidle")
            soup = BeautifulSoup(page.content(), 'html.parser')

            # Parsowanie tabeli (uproszczone dla przykładu)
            for row in soup.select("tr")[1:]:
                cols = row.find_all("td")
                if len(cols) > 5:
                    name = cols[0].get_text(strip=True)
                    win_rate = float(cols[3].get_text(strip=True).replace("%", ""))
                    self.meta_data[name] = {"base_score": win_rate}
            browser.close()
            return self.meta_data


# --- MODUŁ 2: LOGIKA DECYZYJNA (Analiza Matematyczna) ---
class DecisionEngine:
    def __init__(self, meta):
        self.meta = meta
        self.pool_sizes = {1: 22, 2: 20, 3: 17, 4: 10, 5: 9}

    def calculate_utility(self, unit_name, bench, active_traits):
        """Oblicza Utility Score (U_unit)"""
        base = self.meta.get(unit_name, {}).get("base_score", 45.0)

        # Bonus za synergię (S * T)
        synergy_bonus = 15 if any(t in active_traits for t in ["Striker", "Mage"]) else 0  # Przykład

        # Bonus za upgrade (P * V)
        count = sum(1 for u in bench if u == unit_name)
        multiplier = 1.0
        if count == 1: multiplier = 2.5  # Szukamy 2*
        if count == 2: multiplier = 5.0  # Mamy 2*, szukamy 3*

        return (base + synergy_bonus) * multiplier

    def should_roll(self, gold, hp, level):
        """Algorytm zarządzania ekonomią (EV)"""
        if hp < 25: return True  # Desperacja: Send it
        if gold > 50: return True  # Slow roll
        return False


# --- MODUŁ 3: PERCEPCJA (Wykrywanie obrazu) ---
class VisionEngine:
    def __init__(self):
        # Tutaj inicjalizujemy model YOLOv8
        # self.model = YOLO('tft_model.pt')
        pass

    def get_game_state(self):
        return {
            "shop": ["Zoe", "Blitzcrank", "Darius", "Lux", "Zoe"],
            "gold": 52,
            "hp": 76,
            "level": 7,
            "bench": ["Zoe", "Darius"],
            "active_traits": ["Mage"]
        }


# --- MODUŁ 4: WYKONAWCA (Human-like movement) ---
class ActionExecutor:
    def click_unit(self, slot_index):
        # Implementacja krzywych Beziera i randomizacji kliknięć
        x = 1080 + (slot_index * 150) + random.randint(-5, 5)
        y = 1920 + random.randint(-5, 5)
        print(f"B-Spline Move to: ({x}, {y}) -> Click Shop Slot {slot_index}")


# --- MODUŁ GŁÓWNY (Loop) ---
class TFTBot:
    def __init__(self):
        print("Inicjalizacja Bota...")
        self.scraper = MetaScraper()
        self.meta = self.scraper.update_meta()
        self.vision = VisionEngine()
        self.brain = DecisionEngine(self.meta)
        self.executor = ActionExecutor()

    def run(self):
        print("Bot uruchomiony w trybie RANKED.")
        while True:
            state = self.vision.get_game_state()

            # 1. Analiza sklepu
            for i, unit in enumerate(state["shop"]):
                score = self.brain.calculate_utility(unit, state["bench"], state["active_traits"])
                if score > 70:  # Próg opłacalności zakupu
                    self.executor.click_unit(i)

            # 2. Zarządzanie ekonomią
            if self.brain.should_roll(state["gold"], state["hp"], state["level"]):
                print("Decyzja: Rolling for upgrades...")
                # self.executor.click_roll()

            time.sleep(random.uniform(2.0, 4.0))  # Odstęp czasowy między akcjami (Human-like)


# --- START ---
if __name__ == "__main__":
    bot = TFTBot()
=======
import time
import json
import random
import numpy as np
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


# --- MODUŁ 1: SCRAPER (Mózg Statystyczny) ---
class MetaScraper:
    def __init__(self):
        self.url = "https://tactics.tools/units"
        self.meta_data = {}

    def update_meta(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url, wait_until="networkidle")
            soup = BeautifulSoup(page.content(), 'html.parser')

            # Parsowanie tabeli (uproszczone dla przykładu)
            for row in soup.select("tr")[1:]:
                cols = row.find_all("td")
                if len(cols) > 5:
                    name = cols[0].get_text(strip=True)
                    win_rate = float(cols[3].get_text(strip=True).replace("%", ""))
                    self.meta_data[name] = {"base_score": win_rate}
            browser.close()
            return self.meta_data


# --- MODUŁ 2: LOGIKA DECYZYJNA (Analiza Matematyczna) ---
class DecisionEngine:
    def __init__(self, meta):
        self.meta = meta
        self.pool_sizes = {1: 22, 2: 20, 3: 17, 4: 10, 5: 9}

    def calculate_utility(self, unit_name, bench, active_traits):
        """Oblicza Utility Score (U_unit)"""
        base = self.meta.get(unit_name, {}).get("base_score", 45.0)

        # Bonus za synergię (S * T)
        synergy_bonus = 15 if any(t in active_traits for t in ["Striker", "Mage"]) else 0  # Przykład

        # Bonus za upgrade (P * V)
        count = sum(1 for u in bench if u == unit_name)
        multiplier = 1.0
        if count == 1: multiplier = 2.5  # Szukamy 2*
        if count == 2: multiplier = 5.0  # Mamy 2*, szukamy 3*

        return (base + synergy_bonus) * multiplier

    def should_roll(self, gold, hp, level):
        """Algorytm zarządzania ekonomią (EV)"""
        if hp < 25: return True  # Desperacja: Send it
        if gold > 50: return True  # Slow roll
        return False


# --- MODUŁ 3: PERCEPCJA (Wykrywanie obrazu) ---
class VisionEngine:
    def __init__(self):
        # Tutaj inicjalizujemy model YOLOv8
        # self.model = YOLO('tft_model.pt')
        pass

    def get_game_state(self):
        return {
            "shop": ["Zoe", "Blitzcrank", "Darius", "Lux", "Zoe"],
            "gold": 52,
            "hp": 76,
            "level": 7,
            "bench": ["Zoe", "Darius"],
            "active_traits": ["Mage"]
        }


# --- MODUŁ 4: WYKONAWCA (Human-like movement) ---
class ActionExecutor:
    def click_unit(self, slot_index):
        # Implementacja krzywych Beziera i randomizacji kliknięć
        x = 1080 + (slot_index * 150) + random.randint(-5, 5)
        y = 1920 + random.randint(-5, 5)
        print(f"B-Spline Move to: ({x}, {y}) -> Click Shop Slot {slot_index}")


# --- MODUŁ GŁÓWNY (Loop) ---
class TFTBot:
    def __init__(self):
        print("Inicjalizacja Bota...")
        self.scraper = MetaScraper()
        self.meta = self.scraper.update_meta()
        self.vision = VisionEngine()
        self.brain = DecisionEngine(self.meta)
        self.executor = ActionExecutor()

    def run(self):
        print("Bot uruchomiony w trybie RANKED.")
        while True:
            state = self.vision.get_game_state()

            # 1. Analiza sklepu
            for i, unit in enumerate(state["shop"]):
                score = self.brain.calculate_utility(unit, state["bench"], state["active_traits"])
                if score > 70:  # Próg opłacalności zakupu
                    self.executor.click_unit(i)

            # 2. Zarządzanie ekonomią
            if self.brain.should_roll(state["gold"], state["hp"], state["level"]):
                print("Decyzja: Rolling for upgrades...")
                # self.executor.click_roll()

            time.sleep(random.uniform(2.0, 4.0))  # Odstęp czasowy między akcjami (Human-like)


# --- START ---
if __name__ == "__main__":
    bot = TFTBot()
>>>>>>> e48f7e2627e94352550c9ccfe972866c23e1c126
    bot.run()