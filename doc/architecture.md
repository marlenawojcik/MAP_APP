
---

## PLIK: doc/architecture.md

```markdown
# Architektura aplikacji HoliAsk! (wspólna)

## 1. Cel i zakres architektury

Niniejszy dokument opisuje wspólną architekturę aplikacji HoliAsk! - systemu do rekomendacji miejsc wakacyjnych. Dokument przedstawia ogólną strukturę systemu, technologie, konwencje oraz elementy przekrojowe. Szczegółowe opisy modułów znajdują się w dedykowanych plikach w katalogu `doc/architecture/`.

---

## 2. Widok systemu jako całości

System składa się z następujących głównych elementów:

1. **Warstwa UI (templates/static)** – interfejs użytkownika: formularz preferencji, mapa, karty destynacji
2. **Backend (Flask + blueprinty)** – logika aplikacji, routing, przetwarzanie danych
3. **Warstwa danych** – pliki Excel (.xlsx) zawierające dane o destynacjach, opisach i zdjęciach
4. **Moduł wizualizacji** – generowanie interaktywnych map za pomocą Plotly
5. **Moduł rekomendacji** – algorytm dopasowujący destynacje do preferencji

---

## 3. Stos technologiczny (wspólny)

| Obszar | Technologia | Wersja | Rola w systemie |
|--------|-------------|--------|-----------------|
| Backend | Flask | 2.3+ | Framework aplikacji webowej |
| Frontend | HTML5/CSS3/JavaScript | - | Warstwa prezentacji |
| Wizualizacja | Plotly Express | 5.18+ | Generowanie interaktywnych map |
| Przetwarzanie danych | Pandas | 2.0+ | Obsługa plików Excel |
| Baza danych | Pliki Excel (.xlsx) | - | Przechowywanie danych o destynacjach |


---

## 4. Konwencje i standardy w repozytorium

### 4.1 Konwencje nazewnictwa

- **Blueprinty**: nazwa_bp (np. `home_bp`, `mapa_bp`)
- **Endpointy**: `/`, `/map`
- **Funkcje**: snake_case (np. `generate_map`, `oblicz_dopasowanie`)
- **Pliki Python**: snake_case (np. `generate_map.py`)
- **Szablony HTML**: nazwa opisowa (np. `formularz.html`, `mapa.html`)
- **Klasy CSS**: kebab-case (np. `destination-card`, `section-header`)

### 4.2 Wspólne biblioteki / utilities

- **Pandas** – odczyt danych z plików Excel
- **Plotly** – generowanie map
- **Flask** – routing i szablony

5. Przepływ danych
    1. Użytkownik wypełnia formularz na stronie głównej (/) i wysyła dane metodą POST do /map
    2. Blueprint mapa_bp odbiera dane i przekazuje do funkcji oblicz_dopasowanie()
    3. Funkcja oblicz_dopasowanie():
        -Odczytuje plik Zeszyt1.xlsx
        -Dla każdej destynacji sprawdza zgodność z preferencjami
        -Oblicza sumę punktów (lub 0 jeśli któraś preferencja jest niedostępna)
        -Zwraca listę wyników dla wszystkich destynacji
    4. Funkcja generate_map() tworzy interaktywną mapę Plotly:
        -Przygotowuje DataFrame z destynacjami i wynikami
        -Generuje mapę z punktami o rozmiarze i kolorze zależnym od popularności
    5. Funkcja nazwy() z dodanie_info.py:
        -Sortuje destynacje według wyników
        -Dla każdej destynacji pobiera opis i nazwę pliku zdjęcia z Zeszyt2.xlsx
    6. Widok mapa.html renderuje:
        -Mapę wygenerowaną przez Plotly
        -Karty z destynacjami (zdjęcie + opis)

6. Model danych (część wspólna)
Zakres modelu danych wspólnego
Projekt nie wykorzystuje relacyjnej bazy danych. Dane przechowywane są w plikach Excel:
Zeszyt1.xlsx – dane geograficzne i macierz preferencji
Zeszyt2.xlsx – opisy destynacji i nazwy plików ze zdjęciami

7. Cross-cutting concerns
7.1 Obsługa błędów i logowanie
Błędy są wypisywane na konsolę za pomocą print()

W przypadku braku danych w Excelu, aplikacja zwraca pustą listę

Mapa Plotly generowana jest nawet dla pustych wyników

7.2 Bezpieczeństwo
Walidacja danych wejściowych na poziomie formularza (HTML5 required)

Brak sekretów w repozytorium

Ochrona CSRF (Flask-WTF) – do implementacji w przyszłości

8. Decyzje architektoniczne
Decyzja: Wykorzystanie plików Excel zamiast bazy danych
Powód: Prostota implementacji, łatwość edycji danych, brak potrzeby relacyjnego modelu
Konsekwencje: Ograniczona skalowalność, brak transakcyjności

Decyzja: Algorytm dopasowania oparty na sumie punktów z macierzy
Powód: Szybkość obliczeń, łatwość modyfikacji wag
Konsekwencje: Brak zaawansowanego uczenia maszynowego

Decyzja: Podział na blueprinty Flask
Powód: Modularność, łatwość rozwoju przez zespoły
Konsekwencje: Wyraźny podział odpowiedzialności

Decyzja: Wykorzystanie Plotly do wizualizacji
Powód: Interaktywność, łatwość integracji z Flask
Konsekwencje: Zależność od zewnętrznej biblioteki

9. Ograniczenia, ryzyka i dalszy rozwój
Ograniczenia:
-Brak skalowalności przy dużej liczbie destynacji
-Brak personalizacji użytkownika
-Brak cache'owania wyników

Ryzyka:
-Uszkodzenie plików Excel
-Błędy w danych wejściowych
-Wydajność przy generowaniu mapy dla wielu punktów

Propozycje usprawnień:
-Migracja do relacyjnej bazy danych (PostgreSQL)
-Implementacja systemu logowania i zapisywania historii
-Dodanie cache dla wyników zapytań
-Rozszerzenie algorytmu o uczenie maszynowe
