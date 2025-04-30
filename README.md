
# 🏡 Roommate Finder

**Roommate Finder** to aplikacja webowa stworzona z myślą o osobach szukających współlokatorów — szczególnie studentach. Umożliwia przeglądanie dostępnych ofert mieszkaniowych oraz ich lokalizacji za pomocą interaktywnej mapy.

## ✨ Funkcje

- 🗺️ Wyświetlanie ofert mieszkaniowych na interaktywnej mapie dzięki Leaflet
- 🔍 Filtrowanie według lokalizacji i podstawowych preferencji
- 📝 Dodawanie i edycja ofert mieszkaniowych 
- 💾 Przechowywanie danych w bazie SQLite

## 🛠️ Technologie

- Python 3
- Flask
- Leaflet.js (open-source biblioteka mapowa)
- SQLite
- HTML/CSS

## 🚀 Jak uruchomić projekt lokalnie

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/MajaWielgus/roommate-finder.git
   cd roommate-finder
   ```

2. **Utwórz środowisko wirtualne i je aktywuj:**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. **Zainstaluj wymagane biblioteki:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Uruchom aplikację:**

   ```bash
   python run.py
   ```

## 📁 Struktura katalogów

```
roommate-finder/
├── app/              # Główna logika aplikacji 
├── instance/         # Konfiguracja i baza danych SQLite
├── migrations/       # Migracje bazy danych 
├── templates/        # Szablony HTML
├── static/           # Pliki CSS, JS, Leaflet
├── run.py            # Główny plik uruchamiający aplikację
├── requirements.txt  # Lista zależności
├── README.md         # Dokumentacja 
```

## 🗺️ Leaflet

Projekt korzysta z [Leaflet.js](https://leafletjs.com/) – biblioteki open-source do wyświetlania map interaktywnych. Dane lokalizacji ofert są oznaczane markerami.

## 👥 Autorzy

- Maja Wielgus  
- Paulina Pacuła
- Wiktoria Radzanowska

## 📄 Licencja

Projekt jest objęty licencją MIT. Szczegóły znajdują się w pliku `LICENSE`.
