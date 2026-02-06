import pyautogui
import random
import time
import pytweening


class HumanMouse:
    def __init__(self):
        # Wyłączamy FailSafe, żeby bot nie wyłączał się przy rogach ekranu,
        # ale zachowaj ostrożność!
        pyautogui.FAILSAFE = True
        pyautogui.MINIMUM_DURATION = 0.1
        pyautogui.MINIMUM_SLEEP = 0.05
        pyautogui.PAUSE = 0.05

    def move_to(self, x, y):
        """
        Przesuwa mysz do celu używając krzywych Beziera (pytweening).
        To gwarantuje dotarcie do celu i eliminuje "kręcenie się".
        """
        current_x, current_y = pyautogui.position()

        # Oblicz dystans
        dist = ((x - current_x) ** 2 + (y - current_y) ** 2) ** 0.5

        # Dostosuj prędkość do dystansu (im dalej, tym szybciej)
        # Randomizacja czasu ruchu (np. 0.3s - 0.8s)
        base_duration = random.uniform(0.3, 0.6)
        if dist > 500:
            base_duration += 0.3

        # Używamy easeOutQuad - startuje szybciej, zwalnia przy celu (jak ręka)
        # Czasami używamy easeOutCubic dla zmienności
        tween_mode = pytweening.easeOutQuad if random.random() > 0.5 else pytweening.easeOutCubic

        pyautogui.moveTo(x, y, duration=base_duration, tween=tween_mode)

    def human_click(self, x, y):
        """
        Symuluje naturalne kliknięcie z lekkim rozrzutem (Jitter).
        """
        # Dodajemy losowy margines błędu (nie klikaj idealnie w środek piksela)
        offset_x = random.randint(-8, 8)
        offset_y = random.randint(-8, 8)

        final_x = x + offset_x
        final_y = y + offset_y

        # 1. Ruch do celu
        self.move_to(final_x, final_y)

        # 2. Wciśnięcie
        pyautogui.mouseDown()

        # 3. Losowe przytrzymanie (ludzie nie klikają w 0.001s)
        time.sleep(random.uniform(0.08, 0.15))

        # 4. Puszczenie
        pyautogui.mouseUp()

    def drag_and_drop(self, start_x, start_y, end_x, end_y):
        """
        Przeciąganie jednostki (Drag & Drop) - stabilne.
        """
        # Idź do jednostki
        self.move_to(start_x, start_y)
        time.sleep(random.uniform(0.1, 0.2))

        # Chwyć
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.1, 0.2))

        # Przeciągnij do celu
        # Tutaj ruch może być nieco wolniejszy/dokładniejszy
        pyautogui.moveTo(end_x, end_y, duration=random.uniform(0.4, 0.7), tween=pytweening.easeOutQuad)

        # Puść
        time.sleep(random.uniform(0.1, 0.2))
        pyautogui.mouseUp()