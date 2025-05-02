
# 🏡 Roommate Finder – Dokumentacja Projektu

## 1. Charakterystyka oprogramowania

### a. Nazwa skrócona
**RoommateFinder**

### b. Nazwa pełna
**Roommate Finder – Aplikacja do przeglądania ofert pokojów na wynajem**

### c. Opis i cele projektu
Roommate Finder to lekka aplikacja internetowa, która umożliwia użytkownikom przeglądanie ofert pokojów na wynajem w Trójmieście (Gdańsk, Sopot, Gdynia). Projekt skupia się na prostocie i użyteczności — użytkownik wybiera lokalizację i preferencje, a aplikacja prezentuje odpowiednie ogłoszenia.

**Główne cele aplikacji:**
- Ułatwienie przeglądania ofert pokojów z podziałem na miasta Trójmiasta
- Proste filtrowanie według podstawowych kryteriów (np. balkon, palenie, zwierzęta)
- Interaktywna mapa wskazująca wybraną lokalizację w skali ogólnej (bez dokładnych adresów)

---

## 2. Prawa autorskie

### a. Autorzy
- Maja Wielgus  
- Paulina Pacuła  
- Wiktoria Radzanowska

### b. Warunki licencyjne
Projekt objęty jest licencją **MIT**.

**Zewnętrzne komponenty:**
- [Leaflet.js](https://leafletjs.com) – open-source biblioteka mapowa (licencja BSD 2-Clause License)

Pełne treści licencji znajdują się w katalogu `licenses/`.

---

## 3. Specyfikacja wymagań

| ID  | Nazwa                   | Opis                                                   | Priorytet | Kategoria       |
|-----|--------------------------|----------------------------------------------------------|-----------|------------------|
| R1  | Przegląd ogłoszeń        | Wyświetlanie listy pokojów dostępnych w bazie           | 1         | funkcjonalne     |
| R2  | Filtrowanie ogłoszeń     | Filtrowanie po lokalizacji i preferencjach              | 1         | funkcjonalne     |
| R3  | Mapa lokalizacji         | Pokazanie ogólnej lokalizacji miasta na mapie           | 2         | funkcjonalne     |
| R4  | Responsywny interfejs    | Obsługa na urządzeniach mobilnych                       | 2         | pozafunkcjonalne |
| R5  | Przechowywanie danych    | Przechowywanie danych w bazie SQLite                    | 1         | funkcjonalne     |

---

## 4. Architektura systemu

### a. Architektura rozwojowa

| Technologia | Przeznaczenie            | Wersja     |
|-------------|--------------------------|------------|
| Python      | Backend                  | >= 3.10    |
| Flask       | Framework webowy         | 2.x        |
| SQLite      | Baza danych              | dowolna    |
| Jinja2      | Szablony HTML            | wbudowany  |
| JavaScript  | Interaktywne mapy        | dowolna    |
| Leaflet.js  | Biblioteka mapowa        | -          |
| CSS         | Stylowanie               | -          |

### b. Architektura uruchomieniowa

| Technologia           | Przeznaczenie             | Wersja     |
|-----------------------|---------------------------|------------|
| Python                | Środowisko uruchomieniowe | >= 3.10    |
| Flask                 | Serwer aplikacji          | 2.x        |
| SQLite                | Baza danych               | dowolna    |
| Przeglądarka WWW      | Interfejs użytkownika     | aktualna   |

---

## 5. Testy

### a. Sprawozdanie z testów
- Przeprowadzono testy manualne na etapie rozwoju aplikacji.
- Brak testów automatycznych.

---

## 6. Przypadki testowe

### 1. Wybór lokalizacji
- **Cel:** Zobaczyć dostępne pokoje w wybranym mieście.
- **Komentarz:** Lista rozwijana z Gdańsk/Sopot/Gdynia działa poprawnie.

### 2. Filtrowanie ofert
- **Cel:** Znaleźć pokoje z wybranymi preferencjami (balkon, palenie, zwierzęta).
- **Komentarz:** Checkboxy działają poprawnie.

### 3. Wyświetlenie wyników
- **Cel:** Zobaczyć listę pokoi z opisem i ceną.
- **Komentarz:** Lista działa poprawnie, pokazuje podstawowe dane.

### 4. Mapa z miastem
- **Cel:** Zobaczyć mapę z ogólną lokalizacją wybranego miasta.
- **Komentarz:** Mapa centruje się poprawnie.

### 5. Domyślna mapa Trójmiasta
- **Cel:** Po wejściu na stronę zobaczyć domyślny widok całego Trójmiasta.
- **Komentarz:** Działa poprawnie.

### 6. Brak wybranej lokalizacji
- **Cel:** Zobaczyć wszystkie pokoje w bazie.
- **Komentarz:** Wszystkie oferty się wyświetlają.

---

## 7. Dodatki

- Plik `requirements.txt` zawiera wszystkie zależności.
- Kod aplikacji znajduje się w folderze `roommate-finder/`
- Mapa realizowana jest z wykorzystaniem Leaflet.js (open-source, BSD 2-Clause License)
