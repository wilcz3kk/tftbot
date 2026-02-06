import cv2
import os

# --- KONFIGURACJA ---
SOURCE_FOLDER = "tft_dataset/shop_images"
OUTPUT_FOLDER = "tft_dataset/extracted_units"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


def cut_shop_into_slots():
    files = [f for f in os.listdir(SOURCE_FOLDER) if f.endswith('.png')]
    print(f"Znaleziono {len(files)} zrzutów. Rozpoczynam wycinanie...")

    for file_name in files:
        img_path = os.path.join(SOURCE_FOLDER, file_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        height, width, _ = img.shape
        # Dzielimy szerokość na 5 równych slotów sklepu
        slot_width = width // 5

        for i in range(5):
            x_start = i * slot_width
            x_end = (i + 1) * slot_width

            # Wycinamy slot (champion + cena + nazwa)
            unit_crop = img[0:height, x_start:x_end]

            save_name = f"slot_{i}_{file_name}"
            cv2.imwrite(os.path.join(OUTPUT_FOLDER, save_name), unit_crop)

    print(f"Gotowe! Wszystkie sloty zapisano w: {OUTPUT_FOLDER}")


if __name__ == "__main__":
    cut_shop_into_slots()