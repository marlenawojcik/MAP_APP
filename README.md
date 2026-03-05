<<<<<<< HEAD
# HoliAsk! - Znajdź swoje wymarzone wakacje

## Opis

HoliAsk! to interaktywna aplikacja webowa, która pomaga użytkownikom znaleźć idealne miejsce na wakacje na podstawie ich preferencji. Użytkownik odpowiada na 4 pytania dotyczące kontynentu, klimatu, aktywności oraz popularności miejsca, a algorytm dopasowuje najlepsze destynacje z bazy ponad 50 miejsc na całym świecie. Wyniki prezentowane są na interaktywnej mapie oraz w formie kart z opisami i zdjęciami.

---

## Spis treści

- [Szybki start](#szybki-start)
- [Technologie](#technologie)
- [Moduły systemu](#moduły-systemu)
- [Dokumentacja (szczegóły)](#dokumentacja-szczegóły)
- [API (skrót)](#api-skrót)
- [Testowanie (skrót)](#testowanie-skrót)
- [Proces i zasady pracy](#proces-i-zasady-pracy)
- [Autorzy i zespoły](#autorzy-i-zespoły)

---

## Szybki start

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/HoliAsk.git
   cd HoliAsk

2. Utwórz środowisko wirtualne i aktywuj:
bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

3. Zainstaluj zależności:
bash
pip install -r requirements.txt

4. Uruchom aplikację:
bash
python app.py
Otwórz w przeglądarce:

http://127.0.0.1:5000/

5. Widoki aplikacji
Strona główna - formularz preferencji
https://doc/assets/screenshots/home.png

Mapa rekomendacji
https://doc/assets/screenshots/map.png

Karty destynacji
https://doc/assets/screenshots/destinations.png

Technologie
Obszar	Technologia	Wersja	Rola w systemie
Backend	Python/Flask	3.10+ / 2.3+	Framework aplikacji webowej
Frontend	HTML/CSS/JavaScript	-	Warstwa prezentacji
Wizualizacja	Plotly	5.18+	Generowanie interaktywnych map
Dane	Pandas	2.0+	Przetwarzanie danych z Excel
Baza danych	Pliki Excel (.xlsx)	-	Przechowywanie danych o destynacjach

6. Moduły systemu
Projekt został podzielony na moduły:

Strona główna (Home) – formularz zbierający preferencje użytkownika
Dokumentacja modułu: doc/architecture/home.md

Moduł mapy (Map) – generowanie interaktywnej mapy z rekomendacjami
Dokumentacja modułu: doc/architecture/map.md

Moduł rekomendacji (Recommendation) – algorytm dopasowujący destynacje
Dokumentacja modułu: doc/architecture/recommendation.md

Moduł danych (Data) – zarządzanie danymi o destynacjach
Dokumentacja modułu: doc/architecture/data.md

7. Dokumentacja (szczegóły)
Dokumentacja techniczna znajduje się w katalogu doc/:

Specyfikacja funkcjonalna: doc/specification/user_stories.md

Architektura całej aplikacji: doc/architecture.md

Architektura modułów:
doc/architecture/home.md
doc/architecture/map.md
doc/architecture/recommendation.md
doc/architecture/data.md
Konfiguracja: doc/setup.md
Referencja API: doc/api_reference.md
Zasady pracy i kontrybucji: doc/contribution.md
Prowadzenie projektu: doc/project_management.md

8. Licencja
Projekt do użytku dydaktycznego.

=======
# TRAVEL_APP
>>>>>>> de2b4a3d5bf849b1ad9fd7bfef5156fba7e2b719
