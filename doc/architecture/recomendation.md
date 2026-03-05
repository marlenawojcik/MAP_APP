# Architektura modułu: Rekomendacje (Recommendation)

## 1. Cel modułu

Moduł rekomendacji odpowiada za obliczanie stopnia dopasowania destynacji do preferencji użytkownika. Implementuje algorytm, który na podstawie wybranych opcji z formularza przydziela punkty każdej destynacji i sortuje wyniki.

---

## 2. Zakres funkcjonalny (powiązanie z User Stories)

- **US-010** — Jako użytkownik chcę, aby system dopasował miejsca do moich preferencji.
- **US-011** — Jako użytkownik chcę, aby miejsca niedostępne dla wybranych opcji były odrzucane.
- **US-012** — Jako użytkownik chcę widzieć miejsca posortowane według stopnia dopasowania.

---

## 3. Granice modułu

### 3.1 Moduł odpowiada za
- Obliczenie punktów dla każdej destynacji na podstawie macierzy preferencji
- Odrzucenie destynacji, które nie spełniają którejkolwiek z preferencji
- Zwrócenie listy wyników

### 3.2 Moduł nie odpowiada za
- Generowanie mapy
- Pobieranie opisów i zdjęć
- Prezentację wyników
---

## 4. Struktura kodu modułu
website/
├── maps/
│ ├── oblicz_dopasowanie.py # Algorytm obliczania punktów
│ └── dane/
│ └── Zeszyt1.xlsx # Macierz preferencji

## 5. Interfejs modułu

| Funkcja | Parametry | Zwraca | Opis |
|---------|-----------|--------|------|
| `oblicz_dopasowanie(answers)` | Lista 4 preferencji (string) | Lista int | Lista punktów dla wszystkich destynacji |

---

## 6. Zewnętrzne API wykorzystywane przez moduł

Moduł korzysta wyłącznie z danych wewnętrznych (plik Excel).

---

## 7. Model danych modułu

### 7.1 Encje bazodanowe

Moduł operuje na danych z pliku `Zeszyt1.xlsx`:

| Kolumna | Zakres | Opis |
|---------|--------|------|
| destination | A | Nazwa destynacji |
| latitude, longitude | B-C | Współrzędne geograficzne |
| Europa ... mniejsza popularność | D-AC | Wartości 0-100 dla poszczególnych preferencji |

### 7.2 Obiekty domenowe

| Obiekt | Pola | Opis |
|--------|------|------|
| DestinationScore | destination, score | Wynik dopasowania dla destynacji |

### 7.3 Relacje i przepływ danych

1. Funkcja otrzymuje listę `answers` (4 wartości z formularza)
2. Dla każdej destynacji odczytuje wartości dla wybranych preferencji
3. Jeśli któraś wartość = 0, wynik końcowy = 0
4. W przeciwnym razie sumuje wszystkie wartości
5. Zwraca listę wyników

---

## 8. Przepływ danych w module

Scenariusz: Obliczanie dopasowania dla preferencji ["Europa", "górski", "Trekking", "średnia popularność"]

1. Funkcja `oblicz_dopasowanie()` otrzymuje listę answers
2. Dla każdej destynacji i (0..n):
   - Inicjalizuje `b = 0`, `zero_found = False`
   - Dla każdej preferencji a:
     - Znajduje indeks kolumny odpowiadający a
     - Odczytuje wartość `s = df.iloc[i][indeks]`
     - Jeśli `s == 0`, ustawia `zero_found = True`
     - Dodaje `s` do `b`
   - Jeśli `zero_found`:
     - Dodaje 0 do listy wyników
   - W przeciwnym razie:
     - Dodaje `b` do listy wyników
3. Zwraca listę wyników

---

## 9. Ograniczenia, ryzyka, dalszy rozwój
Ograniczenia
Algorytm oparty wyłącznie na sumie punktów (brak wag)

Brak obsługi preferencji "obojętnie" (traktowane jak konkretna wartość)

Sztywne reguły - każda preferencja musi być dostępna

Propozycje usprawnień
Implementacja wag dla poszczególnych kategorii

Dodanie obsługi "obojętnie" jako brak filtra

Algorytm oparty na podobieństwie wektorów

Możliwość wyboru liczby wyników do wyświetlenia