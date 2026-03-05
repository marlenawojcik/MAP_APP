
# Architektura modułu: Strona główna (Home)

## 1. Cel modułu

Moduł strony głównej odpowiada za prezentację formularza zbierającego preferencje użytkownika dotyczące wymarzonych wakacji. Moduł stanowi punkt wejścia do aplikacji i umożliwia przekazanie danych do modułu mapy i rekomendacji.

---

## 2. Zakres funkcjonalny (powiązanie z User Stories)

- **US-001** — Jako użytkownik chcę zobaczyć prosty formularz z pytaniami, aby móc określić swoje preferencje.
- **US-002** — Jako użytkownik chcę wybrać kontynent z listy, aby zawęzić wyszukiwanie.
- **US-003** — Jako użytkownik chcę wybrać klimat, który preferuję.
- **US-004** — Jako użytkownik chcę wybrać aktywności, które mnie interesują.
- **US-005** — Jako użytkownik chcę określić preferowaną popularność turystyczną miejsca.
- **US-006** — Jako użytkownik chcę wysłać formularz i przejść do widoku z rekomendacjami.

---

## 3. Granice modułu

### 3.1 Moduł odpowiada za
- Wyświetlenie formularza z pytaniami
- Walidację wymaganych pól (HTML5)
- Przekazanie danych do modułu mapy metodą POST

### 3.2 Moduł nie odpowiada za
- Przetwarzanie danych i generowanie rekomendacji
- Wyświetlanie mapy i kart destynacji
- Przechowywanie danych użytkownika

---

## 4. Struktura kodu modułu
website/
├── blueprints/
│ └── home_bp.py # Blueprint strony głównej
├── templates/
│ └── formularz.html # Szablon formularza
└── static/
└── css/
└── home.css # Style dla strony głównej

## 5. Zewnętrzne API wykorzystywane przez moduł

Moduł nie korzysta z zewnętrznych API.

## 6. Model danych modułu

### 6.1 Encje bazodanowe

Moduł nie posiada własnych encji bazodanowych.

### 6.2 Obiekty domenowe

| Obiekt | Pola | Opis |
|--------|------|------|
| FormData | preferencja1, preferencja2, preferencja3, preferencja4 | Dane z formularza przesyłane do `/map` |

### 6.3 Relacje i przepływ danych

Dane z formularza są przesyłane metodą POST do endpointu `/map` w module mapy.

## 7. Przepływ danych w module

Scenariusz: Użytkownik wypełnia formularz

1. Użytkownik otwiera stronę główną (`GET /`)
2. System renderuje szablon `formularz.html` z polami select
3. Użytkownik wybiera wartości z list rozwijanych
4. Użytkownik klika "Prześlij"
5. Przeglądarka wysyła dane metodą POST do `/map`

---
8. Ograniczenia, ryzyka, dalszy rozwój
Ograniczenia
Brak walidacji po stronie serwera (tylko HTML5)

Brak zapamiętywania ostatnich wyborów użytkownika

Propozycje usprawnień
Dodanie walidacji po stronie serwera

Implementacja sesji do zapamiętywania preferencji

Dodanie podpowiedzi i tooltipów dla pól formularza