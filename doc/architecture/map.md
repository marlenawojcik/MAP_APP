# Architektura modułu: Mapa (Map)

## 1. Cel modułu

Moduł mapy odpowiada za generowanie interaktywnej wizualizacji rekomendowanych miejsc na mapie świata. Wykorzystuje bibliotekę Plotly do tworzenia mapy z punktami, których rozmiar i kolor zależą od stopnia dopasowania do preferencji użytkownika.

---

## 2. Zakres funkcjonalny (powiązanie z User Stories)

- **US-007** — Jako użytkownik chcę zobaczyć mapę z zaznaczonymi rekomendowanymi miejscami.
- **US-008** — Jako użytkownik chcę, aby rozmiar punktów na mapie odzwierciedlał stopień dopasowania.
- **US-009** — Jako użytkownik chcę widzieć nazwy miejsc po najechaniu na punkt.

---

## 3. Granice modułu

### 3.1 Moduł odpowiada za
- Generowanie mapy Plotly na podstawie wyników dopasowania
- Skalowanie rozmiaru punktów według popularności
- Kolorowanie punktów gradientem (skala Pinkyl)
- Zwracanie kodu HTML mapy do osadzenia w szablonie

### 3.2 Moduł nie odpowiada za
- Obliczanie wyników dopasowania (to zadanie modułu rekomendacji)
- Wyświetlanie kart z opisami destynacji

---

## 4. Struktura kodu modułu
website/
├── maps/
│ ├── generate_map.py # Główna funkcja generująca mapę
│ └── dane/
│ └── Zeszyt1.xlsx # Dane geograficzne
└── templates/
└── mapa.html # Szablon z osadzoną mapą

---

## 5. Interfejs modułu

Moduł nie udostępnia bezpośrednich endpointów - jest wywoływany przez blueprint `mapa_bp`.

| Funkcja | Parametry | Zwraca | Opis |
|---------|-----------|--------|------|
| `generate_map(results_popularity)` | Lista wyników dopasowania | String (HTML) | Generuje mapę Plotly i zwraca kod HTML do osadzenia |

---

## 6. Zewnętrzne API wykorzystywane przez moduł

### 6.1 Plotly Express

Moduł korzysta z biblioteki Plotly Express do generowania map.

| Funkcja | Opis |
|---------|------|
| `px.scatter_geo()` | Tworzy rozrzut punktów na mapie świata |

### 6.2 Konfiguracja

Brak wymaganych zmiennych środowiskowych.

---

## 7. Model danych modułu

### 7.1 Encje bazodanowe

Moduł nie posiada własnych encji.


### 7.2 Relacje i przepływ danych

1. Funkcja otrzymuje listę `results_popularity` (długość = liczba destynacji)
2. Tworzy DataFrame z danymi z `Zeszyt1.xlsx` i wynikami
3. Przekazuje DataFrame do `px.scatter_geo`
4. Zwraca HTML wygenerowany przez Plotly

---

## 8. Przepływ danych w module

Scenariusz: Generowanie mapy dla wyników dopasowania

1. Funkcja `generate_map()` otrzymuje listę wyników
2. Odczytuje plik `Zeszyt1.xlsx` za pomocą Pandas
3. Tworzy DataFrame `vacation_df` z kolumnami:
   - destination, popularity, latitude, longitude
4. Wywołuje `px.scatter_geo()` z parametrami:
   - lat, lon, text, size, color
5. Ustawia wygląd mapy (kolorystyka Pinkyl, rozmiar max 30)
6. Konwertuje figurę do HTML: `fig.to_html()`
7. Zwraca kod HTML do osadzenia w szablonie

---


## 9. Ograniczenia, ryzyka, dalszy rozwój
Ograniczenia
Mapa Plotly wymaga połączenia z internetem (CDN)

Duża liczba punktów może spowolnić renderowanie

Propozycje usprawnień
Dodanie możliwości przybliżania/oddalania

Implementacja filtrów na mapie

Cache'owanie wygenerowanej mapy dla tych samych wyników