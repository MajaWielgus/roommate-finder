# 🏡 Roommate Finder

Roommate Finder to prosta aplikacja webowa umożliwiająca przeglądanie ofert pokojów na wynajem w Trójmieście (Gdańsk, Sopot, Gdynia). Aplikacja pozwala filtrować oferty według lokalizacji i podstawowych preferencji oraz prezentuje wyniki na interaktywnej mapie.

## ✨ Funkcje

- 🗺️ Interaktywna mapa z zaznaczonym ogólnym obszarem miasta (Leaflet.js + OpenStreetMap)
- 🔍 Filtrowanie ofert według lokalizacji i preferencji (balkon, palenie, zwierzęta)
- 🧩 Przechowywanie danych w lokalnej bazie SQLite
- 📱 Responsywny interfejs dostępny w przeglądarce

## 🛠️ Technologie

- Python 3.10+
- Flask (backend + routing)
- SQLite (baza danych)
- HTML + CSS + Jinja2 (szablony)
- JavaScript + Leaflet.js (interaktywne mapy z danymi z OpenStreetMap)

## 🚀 Jak uruchomić projekt lokalnie

1. Sklonuj repozytorium:

```
git clone https://github.com/MajaWielgus/roommate-finder.git
cd roommate-finder
```

2. Utwórz i aktywuj środowisko wirtualne:

```
python -m venv venv
# Dla Windows:
venv\Scripts\activate
# Dla macOS/Linux:
source venv/bin/activate
```

3. Zainstaluj zależności:

```
pip install -r requirements.txt
```

4. Uruchom aplikację:

```
python run.py
```

Aplikacja powinna być dostępna pod adresem http://127.0.0.1:5000/

## 📁 Struktura katalogów

```
roommate-finder/
├── app/              # Główna logika aplikacji 
├── instance/         # Baza danych SQLite i konfiguracje
├── migrations/       # Migracje bazy danych 
├── templates/        # Szablony HTML (Jinja2)
├── static/           # Pliki CSS, JS, Leaflet
├── run.py            # Główny plik uruchamiający aplikację
├── requirements.txt  # Lista zależności
├── README.md         # Dokumentacja techniczna
```

## 🗺️ Leaflet.js

Projekt korzysta z biblioteki [Leaflet.js](https://leafletjs.com), która umożliwia wyświetlanie map interaktywnych. W naszej aplikacji pokazuje ona ogólną lokalizację wybranego miasta (bez dokładnych adresów).

## 📄 Licencja

Projekt objęty jest licencją **MIT**. Szczegóły znajdują się w pliku `LICENSE`.  
Projekt korzysta również z Leaflet.js, który dostępny jest na licencji BSD 2-Clause.

## 👥 Autorzy

- Maja Wielgus  
- Paulina Pacuła  
- Wiktoria Radzanowska  
