import os
import shutil
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

# --- KONFIGURACJA ---
INPUT_DIR = "tft_dataset/extracted_units"
OUTPUT_DIR = "tft_dataset/organized_units"
NUM_CLUSTERS = 60  # Przybliżona liczba różnych jednostek w zestawie TFT

# 1. Przygotowanie modelu do ekstrakcji cech (wyciąga "sens" z obrazka)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=True).to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def extract_features(img_path):
    img = Image.open(img_path).convert('RGB')
    img = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        feature = model(img)
    return feature.cpu().numpy().flatten()


# 2. Główny proces
def organize_folders():
    images = [f for f in os.listdir(INPUT_DIR) if f.endswith(('.jpg', '.png'))]
    features = []
    valid_images = []

    print(f"Analizuję {len(images)} obrazków... To może chwilę potrwać.")

    for img_name in images:
        try:
            path = os.path.join(INPUT_DIR, img_name)
            features.append(extract_features(path))
            valid_images.append(img_name)
        except Exception as e:
            print(f"Pominięto {img_name}: {e}")

    # 3. Grupowanie podobnych obrazków
    print("Grupuje jednostki...")
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42)
    clusters = kmeans.fit_predict(features)

    # 4. Przenoszenie do folderów
    for img_name, cluster_id in zip(valid_images, clusters):
        cluster_folder = os.path.join(OUTPUT_DIR, f"Grupa_{cluster_id}")
        os.makedirs(cluster_folder, exist_ok=True)
        shutil.copy(os.path.join(INPUT_DIR, img_name), os.path.join(cluster_folder, img_name))

    print(f"Zakończono! Sprawdź folder: {OUTPUT_DIR}")


if __name__ == "__main__":
    organize_folders()