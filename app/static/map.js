document.addEventListener("DOMContentLoaded", function () {
    // Inicjalizacja mapy
    const map = L.map('map').setView([54.40, 18.58], 9.5);

    // Dodanie warstwy z OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap',
        maxZoom: 18
    }).addTo(map);

    // Wczytanie danych miasta z HTML (przekazanych przez Flask)
    const cityCoordinates = JSON.parse(document.getElementById('map').getAttribute('data-city-coordinates'));

    // Pobieramy dane wybranego miasta z atrybutu data-selected-city
    const selectedCity = JSON.parse(document.getElementById('map').getAttribute('data-selected-city'));  // Przekazane przez Flask

    // Dodajemy logowanie do konsoli, żeby sprawdzić, co jest w zmiennej selectedCity
    console.log("Wybrane miasto:", selectedCity);
    console.log("Dane miast:", cityCoordinates);

    // Sprawdzamy, czy wybrane miasto ma dane w cityCoordinates
    if (selectedCity && cityCoordinates[selectedCity]) {
        const city = cityCoordinates[selectedCity];
        console.log("Dane dla wybranego miasta:", city);

        // Tworzymy kółko na mapie dla wybranego miasta
        L.circle([city.lat, city.lng], {
            color: 'pink',
            fillColor: '#ca72c0',
            fillOpacity: 0.3,
            radius: city.radius
        }).addTo(map);
    } else {
        // Jeśli nie wybrano miasta lub nie ma danych dla miasta, dodajemy ogólną mapę
        console.log("Brak danych dla wybranego miasta.");
        // Opcjonalnie: Zmiana domyślnej lokalizacji mapy (np. Trójmiasto)
        map.setView([54.40, 18.58], 9.5);
    }
});
