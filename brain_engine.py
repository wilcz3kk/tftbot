import json
import os


class MetaBrain:
    def __init__(self, stats_path="meta_stats.json"):
        self.wanted_units = set()
        self.load_meta(stats_path)

    def load_meta(self, path):
        if not os.path.exists(path):
            print("[Brain] Brak pliku meta_stats.json! Uruchom scraper.py.")
            return

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # Obsługa formatu LeagueOfGraphs
                if isinstance(data, dict) and "top_units" in data:
                    self.wanted_units = {u.lower() for u in data["top_units"]}
                    print(f"[Brain] Cel: {len(self.wanted_units)} jednostek z Top Tier.")
                else:
                    print("[Brain] Nieznany format pliku meta.")
        except Exception as e:
            print(f"[Brain] Błąd odczytu mety: {e}")

    def should_buy(self, unit_name):
        if not unit_name: return False
        # Porównanie bez względu na wielkość liter
        return unit_name.lower() in self.wanted_units