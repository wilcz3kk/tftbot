import imagehash
from PIL import Image
import os


class UnitRecognizer:
    def __init__(self, reference_folder="tft_dataset/extracted_units"):
        self.references = {}
        # Ładujemy wzorce do pamięci
        for unit_name in os.listdir(reference_folder):
            unit_path = os.path.join(reference_folder, unit_name)
            if os.path.isdir(unit_path):
                img_file = os.listdir(unit_path)[0]  # bierzemy pierwsze zdjęcie
                full_path = os.path.join(unit_path, img_file)
                self.references[unit_name] = imagehash.phash(Image.open(full_path))

    def identify(self, crop_img):
        target_hash = imagehash.phash(Image.fromarray(crop_img))
        best_match = None
        min_distance = 100  # Im mniejszy dystans, tym bardziej podobne obrazy

        for name, ref_hash in self.references.items():
            distance = target_hash - ref_hash  # Obliczanie różnicy bitowej
            if distance < min_distance:
                min_distance = distance
                best_match = name
        return best_match if min_distance < 15 else "Unknown"