import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def scrape_meta_comps():
    # LeagueOfGraphs jest łatwiejsze do zescrapowania
    url = "https://www.leagueofgraphs.com/tft/comps"

    with sync_playwright() as p:
        print("Uruchamianie przeglądarki...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Pobieranie danych z: {url}")
        page.goto(url, wait_until="domcontentloaded")  # Szybsze ładowanie

        # Czekamy na listę championów (ikony)
        try:
            page.wait_for_selector("img", timeout=10000)
        except:
            print("Timeout. Strona ładuje się zbyt długo.")
            browser.close()
            return

        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')

        # Struktura danych
        meta_data = {
            "top_units": [],  # Płaska lista wszystkich jednostek do kupowania
            "comps": []  # Szczegółowe składy
        }

        # Szukamy głównych bloków z kompozycjami
        # LeagueOfGraphs używa tabel lub divów z klasą .box
        # Tutaj szukamy wierszy z championami

        # Znajdujemy wszystkie bloki z ikonami championów w składach
        comp_rows = soup.select("tr")

        print(f"Analizuję {len(comp_rows)} potencjalnych składów...")

        unique_units = set()

        for row in comp_rows:
            # Szukamy obrazków championów w wierszu
            imgs = row.select("img")
            comp_units = []

            for img in imgs:
                # LeagueOfGraphs ma nazwy w 'alt', np. "Warwick"
                name = img.get("alt")

                # Filtrujemy śmieci (ikony traitów, przedmiotów itp.)
                # Championy mają zazwyczaj czyste nazwy, traity mają "Trait" w nazwie lub są małe
                if name and "Trait" not in name and "Item" not in name:
                    # Czasami nazwy mają dopiski, bierzemy pierwsze słowo lub całość
                    # LeagueOfGraphs format: "Warwick"
                    clean_name = name.strip()

                    # Ignorujemy puste lub bardzo długie nazwy (błędy parsowania)
                    if len(clean_name) < 20:
                        comp_units.append(clean_name)
                        unique_units.add(clean_name)

            if len(comp_units) >= 4:  # Uznajemy to za sensowny skład
                meta_data["comps"].append({
                    "units": comp_units
                })
                # Ograniczamy do 10 najlepszych składów (są one na górze strony)
                if len(meta_data["comps"]) >= 10:
                    break

        meta_data["top_units"] = list(unique_units)
        browser.close()

    if not meta_data["top_units"]:
        print("BŁĄD: Nie znaleziono jednostek. Struktura strony mogła się zmienić.")
    else:
        with open('meta_stats.json', 'w', encoding='utf-8') as f:
            json.dump(meta_data, f, indent=4)
        print(f"SUKCES! Zapisano {len(meta_data['comps'])} topowych składów.")
        print(f"Bot będzie polował na {len(meta_data['top_units'])} różnych championów.")


if __name__ == "__main__":
    scrape_meta_comps()