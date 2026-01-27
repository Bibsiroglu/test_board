import flet as ft
from core.navigation import Router
from core.theme import AppTheme

def main(page: ft.Page):
    # --- 1. SAYFA AYARLARI ---
    page.title = "NikoCRM"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT  # Aydınlık modda açılsın
    
    # --- 2. TEMAYI YÜKLE ---
    # Renkleri ve o özel 'Adigiana Toybox' fontunu yüklüyoruz
    AppTheme.apply_theme(page)

    # --- 3. NAVİGASYONU BAŞLAT ---
    app_router = Router(page)
    
    # Sayfaya router'ın kutusunu ekliyoruz
    page.add(app_router.get_content())

    # --- 4. İLK EKRANA GİT ---
    app_router.go("login")

if __name__ == "__main__":
    # Uygulamayı başlatıyoruz.
    # assets_dir="assets" -> Resim ve font klasörümüzü tanıtıyoruz.
    ft.app(
        target=main, 
        assets_dir="assets", 
        view=ft.AppView.WEB_BROWSER, 
        port=8080
    )