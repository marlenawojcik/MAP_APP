# Architektura modułu: Dane (Data)

## 1. Cel modułu

Moduł danych odpowiada za zarządzanie danymi o destynacjach, ich opisami oraz zdjęciami. Dostarcza funkcje do odczytu danych z plików Excel oraz pobierania informacji o destynacjach na podstawie wyników dopasowania.

---

## 2. Zakres funkcjonalny (powiązanie z User Stories)

- **US-013** — Jako użytkownik chcę widzieć opis każdej rekomendowanej destynacji.
- **US-014** — Jako użytkownik chcę widzieć zdjęcie każdej rekomendowanej destynacji.

---

## 3. Granice modułu

### 3.1 Moduł odpowiada za
- Odczyt danych z plików Excel (`Zeszyt1.xlsx`, `Zeszyt2.xlsx`)
- Pobieranie opisów i nazw plików zdjęć dla listy destynacji
- Sortowanie destynacji według wyników

### 3.2 Moduł nie odpowiada za
- Obliczanie wyników
- Prezentację danych w UI

---

## 4. Struktura kodu modułu
website/
├── maps/
│ ├── dodanie_info.py # Funkcja pobierająca opisy i zdjęcia
│ └── dane/
│ ├── Zeszyt1.xlsx # Dane geograficzne i preferencje
│ └── Zeszyt2.xlsx # Opisy i zdjęcia

---

## 5. Interfejs modułu

| Funkcja | Parametry | Zwraca | Opis |
|---------|-----------|--------|------|
| `nazwy(results_popularity)` | Lista wyników dopasowania | Tuple (lista_nazw, lista_opisow, lista_zdjec) | Zwraca posortowane listy nazw, opisów i nazw plików zdjęć |

---

## 6. Zewnętrzne API wykorzystywane przez moduł

Moduł korzysta wyłącznie z danych wewnętrznych.

---

## 7. Model danych modułu

### 7.1 Encje bazodanowe

**Plik: Zeszyt2.xlsx**

| Kolumna | Nazwa | Opis |
|---------|-------|------|
| A | destination | Nazwa destynacji (klucz główny) |
| B | opis | Opis destynacji (tekst) |
| O | zdjecie | Nazwa pliku ze zdjęciem (np. "koryska.jpg") |

### 7.2 Obiekty domenowe

| Obiekt | Pola | Opis |
|--------|------|------|
| DestinationInfo | nazwa, opis, zdjecie | Pełne informacje o destynacji |

### 7.3 Relacje i przepływ danych

1. Funkcja otrzymuje listę `results_popularity`
2. Tworzy słownik `miasto -> punkt` dla wyników > 0
3. Sortuje słownik malejąco według punktów
4. Dla każdej destynacji w kolejności:
   - Szuka wiersza w `Zeszyt2.xlsx` z pasującą nazwą
   - Dodaje nazwę, opis i nazwę pliku do list wynikowych
5. Zwraca trzy listy (nazwy, opisy, zdjęcia) w tej samej kolejności

---

## 8. Przepływ danych w module

Scenariusz: Pobranie informacji o najlepszych destynacjach

1. Funkcja `nazwy()` otrzymuje listę wyników
2. Tworzy pusty słownik `słownik_punktów`
3. Iteruje przez `destination_list` i `results_popularity`:
   - Jeśli punkt > 0, dodaje do słownika
4. Sortuje słownik: `sorted(..., reverse=True)`
5. Iteruje przez posortowane destynacje:
   - Odczytuje plik `Zeszyt2.xlsx`
   - Szuka wiersza gdzie `destination == miasto`
   - Dodaje do list wynikowych
6. Zwraca tuple list

---
 ## 9. Ograniczenia, ryzyka, dalszy rozwój
Ograniczenia:
-Zależność od spójności danych między plikami Excel
-Brak obsługi brakujących opisów/zdjęć
-Pliki Excel muszą być ręcznie aktualizowane

Propozycje usprawnień:
-Migracja do bazy danych z relacjami
-Dodanie panelu administracyjnego do zarządzania danymi
-System tagowania destynacji
-Automatyczne pobieranie zdjęć z zewnętrznych API