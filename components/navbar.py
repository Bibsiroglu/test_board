import flet as ft

class NavBar(ft.NavigationDrawer):
    def __init__(self, on_change_function):
        super().__init__()
        # Tıklama olayını bağlıyoruz
        self.on_change = on_change_function
        self_selected_index = 0

        # Çekmece İçeriği
        self.controls = [
            # Menü Üstü (Header) - Logo vs. için
            ft.Container(
                height=150,
                bgcolor=ft.Colors.BLUE_GREY_900,
                alignment=ft.Alignment.CENTER,
                content=ft.Column([
                    ft.Icon(ft.Icons.REAL_ESTATE_AGENT, size=50, color=ft.Colors.AMBER_900),
                    ft.Text("EMLAK CRM", color=ft.Colors.WHITE, size=12),
                    ft.Text("Hoşgeldiniz", color=ft.Colors.WHITE_54, size=12),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ),

            ft.Divider(thickness=2),

            # Menü Elemanları
            ft.NavigationDrawerDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="İlanlar"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.PEOPLE_OUTLINE,
                selected_icon=ft.Icons.PEOPLE,
                label="Müşteriler"
            ),

            ft.Divider(thickness=2),

            ft.NavigationDrawerDestination(
                icon=ft.Icons.LOGOUT,
                label="Güvenli Çıkış"
            )
        ]