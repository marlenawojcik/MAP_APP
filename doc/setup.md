# Konfiguracja i środowisko (setup.md)

## 1. Wymagania systemowe

- **Python:** wersja 3.10 lub wyższa
- **System operacyjny:** Windows / Linux / macOS
- **Przeglądarka:** Chrome / Firefox / Edge (współczesne wersje)
- **Połączenie z internetem:** wymagane do pobrania bibliotek Plotly z CDN

---

## 2. Instalacja lokalna

### 2.1 Sklonuj repozytorium
```bash
git clone https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/HoliAsk.git
cd HoliAsk
```
### 2.2 Utwórz i aktywuj środowisko wirtualne
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```
### 2.3 Zainstaluj zależności
```bash
pip install -r requirements.txt
```

### 2.4 Uruchom aplikację
```bash
python app.py
```

## 3. Struktura danych
Aplikacja wymaga dwóch plików Excel w katalogu website/maps/dane/:

Zeszyt1.xlsx – dane geograficzne i macierz preferencji

Zeszyt2.xlsx – opisy destynacji i nazwy plików zdjęć

Zdjęcia destynacji muszą znajdować się w katalogu website/static/images/.

## 4. 6. Typowe problemy i rozwiązania
Problem: ModuleNotFoundError: No module named 'plotly'
Rozwiązanie: Zainstaluj brakującą bibliotekę:

```bash
pip install plotly pandas
```
Problem: Błąd odczytu plików Excel
Rozwiązanie: Sprawdź czy pliki znajdują się w website/maps/dane/ i mają odpowiednie nazwy.

Problem: Mapa nie wyświetla się
Rozwiązanie: Sprawdź połączenie z internetem (Plotly ładuje skrypty z CDN).

Problem: Zdjęcia nie ładują się
Rozwiązanie: Sprawdź czy pliki znajdują się w website/static/images/ i czy nazwy w Zeszyt2.xlsx są poprawne.