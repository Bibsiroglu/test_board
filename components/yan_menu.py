import flet as ft

class YanMenu(ft.Container):
    def __init__(self):
        super().__init__()
        
        # Container ayarları
        self.width = 250
        self.bgcolor = ft.Colors.BLUE_GREY_900
        self.padding = 20
        self.height = 800 # Menünün boyunu uzatmak için (opsiyonel)
        
        # İçerik
        self.content = ft.Column([
            ft.Text("EMLAK CRM", size=25, weight="bold", color="white"),
            ft.Divider(color="white24"),
            ft.TextButton("Portföyüm", icon=ft.Icons.HOME, style=ft.ButtonStyle(color="white")),
            ft.TextButton("Müşteriler", icon=ft.Icons.PEOPLE, style=ft.ButtonStyle(color="white")),
            ft.TextButton("Raporlar", icon=ft.Icons.BAR_CHART, style=ft.ButtonStyle(color="white")),
            ft.Container(expand=True),
            ft.TextButton("Çıkış Yap", icon=ft.Icons.LOGOUT, style=ft.ButtonStyle(color="red"))
        ])