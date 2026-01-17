import flet as ft

class YanMenu(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.width = 250
        self.bgcolor = ft.Colors.BLUE_GREY_900
        self.padding = 20
        self.height = 800 
        
        self.content = ft.Column([
            ft.Text("EMLAK CRM", size=25, weight="bold", color="white"),
            ft.Divider(color="white24"),
            
            # GÜNCELLEME: on_click olayları eklendi
            ft.TextButton(
                "Portföyüm", 
                icon=ft.Icons.HOME, 
                style=ft.ButtonStyle(color="white"),
                on_click=lambda e: e.page.go("/")  # Ana sayfaya git
            ),
            ft.TextButton(
                "Müşteriler", 
                icon=ft.Icons.PEOPLE, 
                style=ft.ButtonStyle(color="white"),
                on_click=lambda e: e.page.go("/musteriler") # Müşterilere git
            ),
            ft.TextButton("Raporlar", icon=ft.Icons.BAR_CHART, style=ft.ButtonStyle(color="white")),
            
            ft.Container(expand=True),
            ft.TextButton("Çıkış Yap", icon=ft.Icons.LOGOUT, style=ft.ButtonStyle(color="red"))
        ])