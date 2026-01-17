import flet as ft

# DİKKAT: Artık UserControl yerine ft.Container kullanıyoruz
class IlanKarti(ft.Container):
    def __init__(self, baslik, fiyat, konum, resim_url):
        super().__init__() # Container'ı başlatıyoruz
        self.baslik = baslik
        self.fiyat = fiyat
        self.konum = konum
        self.resim_url = resim_url

        # Container özelliklerini doğrudan self'e tanımlıyoruz
        self.width = 300
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 15
        self.padding = 15
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK)
        )
        
        # İçerik (build metodu yerine self.content kullanıyoruz)
        self.content = ft.Column([
            ft.Image(src=self.resim_url, width=300, height=150, fit='cover', border_radius=10),
            ft.Text(self.baslik, size=18, weight="bold", color="black"),
            ft.Row([
                ft.Icon(ft.Icons.LOCATION_ON, color="blue", size=16),
                ft.Text(self.konum, size=14, color="grey")
            ]),
            ft.Divider(),
            ft.Row([
                ft.Text(f"{self.fiyat} TL", size=20, weight="bold", color="green"),
                ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, icon_color="red")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ])