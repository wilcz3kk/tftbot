import cv2
import os
import imagehash
from PIL import Image


class UnitRecognizer:
    def __init__(self, reference_folder="tft_dataset/organized_units"):
        self.references = {}
        if not os.path.exists(reference_folder):
            print(f"[Vision] BŁĄD: Folder {reference_folder} nie istnieje!")
            return

        count = 0
        for unit_name in os.listdir(reference_folder):
            unit_path = os.path.join(reference_folder, unit_name)
            if os.path.isdir(unit_path):
                files = [f for f in os.listdir(unit_path) if f.endswith(('.jpg', '.png'))]
                if files:
                    img_path = os.path.join(unit_path, files[0])
                    # Obliczamy hash dla obrazu wzorcowego
                    self.references[unit_name] = imagehash.phash(Image.open(img_path))
                    count += 1
        print(f"[Vision] Załadowano {count} wzorców jednostek.")

    def identify_unit(self, crop_cv2_img):
        try:
            # Konwersja BGR (OpenCV) na RGB (PIL)
            rgb_img = cv2.cvtColor(crop_cv2_img, cv2.COLOR_BGR2RGB)
            target_hash = imagehash.phash(Image.fromarray(rgb_img))

            best_match = None
            min_distance = 18  # Czułość dopasowania (im mniej, tym precyzyjniej)

            for name, ref_hash in self.references.items():
                distance = target_hash - ref_hash
                if distance < min_distance:
                    min_distance = distance
                    best_match = name
            return best_match
        except Exception:
            return None