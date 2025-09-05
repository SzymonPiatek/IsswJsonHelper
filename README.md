# 🎯 ISSW JSON HELPER

Wszechstronne narzędzie wspierające pracę z formularzami wniosków i raportów w systemie **ISSW**.

---

## ✨ Kluczowe funkcjonalności

### 🔧 FormBuilder
Twórz, modyfikuj i rozwijaj formularze w formacie JSON w sposób szybki i zautomatyzowany.  
Idealny do zarządzania powtarzalnymi sekcjami oraz budowy kosztorysów bez zbędnego klikania.

### 🖼 WebScraper
Przechwytuj pełne zrzuty ekranu każdej strony formularza – zarówno wniosku, jak i raportu.  
Działa w sposób zautomatyzowany, z zachowaniem kontekstu i pełnej treści strony.

### 🤖 Postman
Moduł odpowiedzialny za komunikację z systemem ISSW.  
Umożliwia automatyczną aktualizację zawartości formularzy (_autosave_) oraz generowanie i pobieranie ich wersji w formacie PDF.

### 🕵️ Analyzer
Analizuje pliki JSON w katalogach i wykrywa błędy strukturalne, takie jak zduplikowane `name`.  
Generuje raport w czytelnym formacie oraz w postaci pliku `.json`, wspierając kontrolę jakości danych.

---

## 🚀 Jak zacząć korzystać?

1. Skopiuj plik `.env.default` i zapisz go jako `.env`. Uzupełnij zmienne środowiskowe odpowiednimi wartościami.

2. Utwórz nowe środowisko wirtualne i aktywuj je:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate.bat  # Windows
   ```

3. Zainstaluj **Poetry**:

   ```bash
   pip install poetry
   ```

4. Zainstaluj zależności projektu:

   ```bash
   poetry install
   ```

5. Uruchom aplikację:

   ```bash
   python main.py
   ```

---

## 📝 Licencja

Projekt dostępny na zasadach licencji MIT.
