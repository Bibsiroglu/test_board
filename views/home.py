import flet as ft
from components.ilan_karti import IlanKarti

def HomeView(page):
    # İlan verileri
    ilanlar_verisi = [
        {"baslik": "Lüks Daire", "fiyat": "4.5M", "konum": "Kadıköy", "url": "https://picsum.photos/300/150?1"},
        {"baslik": "Villa", "fiyat": "12M", "konum": "Bodrum", "url": "https://picsum.photos/300/150?2"},
        {"baslik": "Arsa", "fiyat": "2M", "konum": "Kastamonu", "url": "https://picsum.photos/300/150?3"},
        {"baslik": "Ofis", "fiyat": "8M", "konum": "Levent", "url": "https://picsum.photos/300/150?4"},
        {"baslik": "Yazlık", "fiyat": "6M", "konum": "Çeşme", "url": "https://picsum.photos/300/150?5"},
    ]

    kartlar = [
        IlanKarti(item["baslik"], item["fiyat"], item["konum"], item["url"]) 
        for item in ilanlar_verisi
    ]

    # Sayfa içeriğini döndürüyoruz
    return ft.View(
        "/", # Bu sayfanın adresi
        controls=[
             ft.Container(
                padding=20,
                content=ft.Column([
                    ft.Text("Aktif İlanlar", size=30, weight="bold", color=ft.Colors.BLUE_GREY_800),
                    ft.Divider(color="transparent"),
                    ft.GridView(
                        expand=True,
                        runs_count=5,
                        max_extent=320,
                        child_aspect_ratio=0.8,
                        spacing=20,
                        run_spacing=20,
                        controls=kartlar
                    )
                ])
            )
        ],
        bgcolor=ft.Colors.BLUE_GREY_50,
        padding=0
    )