<h1 style="text-align: center;">ISSW JSON HELPER</h1>

---

<div style="width: 100%; display: flex; justify-content: center;">
    <h3 style="text-align: center; max-width: 500px;">Wszechstronne narzędzie wspierające pracę z formularzami wniosków i raportów w systemie ISSW.</h3>
</div>

---

<h2 style="text-align: center;">Kluczowe funkcjonalności</h2>

<h3>🔧 FormBuilder</h3>
<p style="font-size: 16px;">
Twórz, modyfikuj i rozwijaj formularze w formacie JSON w sposób szybki i zautomatyzowany.  
Idealny do zarządzania powtarzalnymi sekcjami oraz budowy kosztorysów bez zbędnego klikania.
</p>

<h3>🖼 WebScraper</h3>
<p style="font-size: 16px;">
Przechwytuj pełne zrzuty ekranu każdej strony formularza – zarówno wniosku, jak i raportu.  
Wszystko w sposób zautomatyzowany, z zachowaniem kontekstu i pełnej treści strony.
</p>

<h3>🤖 Postman</h3>
<p style="font-size: 16px;">
Moduł odpowiedzialny za komunikację z systemem ISSW.  
Umożliwia automatyczną aktualizację zawartości formularzy (autosave) oraz generowanie i pobieranie ich wersji w formacie PDF.
</p>

---

<h2 style="text-align: center;">Jak zacząć korzystać?</h2>

<p style="font-size: 16px;">
1. Skopiuj plik <code>.env.default</code> i zapisz go jako <code>.env</code>. Następnie uzupełnij zmienne środowiskowe odpowiednimi wartościami.
<br><br>
2. Utwórz nowe środowisko wirtualne (np. folder <code>venv</code>) i aktywuj je. Przykładowo:
</p>

<pre><code>python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate.bat  # Windows
</code></pre>

<p style="font-size: 16px;">
3. Zainstaluj <strong>Poetry</strong> za pomocą pip:
</p>

<pre><code>pip install poetry</code></pre>

<p style="font-size: 16px;">
4. Zainstaluj zależności projektu za pomocą Poetry:
</p>

<pre><code>poetry install</code></pre>

<p style="font-size: 16px;">
5. Uruchom aplikację poleceniem:
</p>

<pre><code>python main.py</code></pre>

