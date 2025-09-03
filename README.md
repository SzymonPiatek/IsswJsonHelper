<h1 style="text-align: center; margin-bottom: 2.5rem">ISSW JSON HELPER</h1>

---

<div style="width: 100%; display: flex; justify-content: center;">
    <h3 style="text-align: center; max-width: 500px; margin-bottom: 1.5rem">Wszechstronne narzędzie wspierające pracę z formularzami wniosków i raportów w systemie ISSW.</h3>
</div>

---

<div style="max-width: 1200px; margin: 0 auto;">
<h2 style="text-align: center; font-size: 2rem; margin-bottom: 3rem;">Kluczowe funkcjonalności</h2>

<div style="
display: grid;
grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
gap: 1.5rem;
">

<div style="border: 1px solid #ddd; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
  <h3 style="margin-top: 0;">🔧 FormBuilder</h3>
  <p style="font-size: 16px; line-height: 1.6;">
    Twórz, modyfikuj i rozwijaj formularze w formacie JSON w sposób szybki i zautomatyzowany.  
    Idealny do zarządzania powtarzalnymi sekcjami oraz budowy kosztorysów bez zbędnego klikania.
  </p>
</div>

<div style="border: 1px solid #ddd; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
  <h3 style="margin-top: 0;">🖼 WebScraper</h3>
  <p style="font-size: 16px; line-height: 1.6;">
    Przechwytuj pełne zrzuty ekranu każdej strony formularza – zarówno wniosku, jak i raportu.  
    Wszystko w sposób zautomatyzowany, z zachowaniem kontekstu i pełnej treści strony.
  </p>
</div>

<div style="border: 1px solid #ddd; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
  <h3 style="margin-top: 0;">🤖 Postman</h3>
  <p style="font-size: 16px; line-height: 1.6;">
    Moduł odpowiedzialny za komunikację z systemem ISSW.  
    Umożliwia automatyczną aktualizację zawartości formularzy (autosave) oraz generowanie i pobieranie ich wersji w formacie PDF.
  </p>
</div>

</div>
</div>

---

<div style="max-width: 800px; margin: 0 auto;">
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
</div>

