import flet as ft
from core.theme import AppTheme

class NavBar(ft.NavigationDrawer):
    def __init__(self, on_change_function):
        super().__init__()
        self.on_change = on_change_function

        self.bgcolor = AppTheme.niko_bgcolor

        self.indicator_color = AppTheme.niko_red

        self.controls = [
            ft.Container(
                content=ft.CircleAvatar(
                    foreground_image_src="logo.png",
                    radius=70,
                    bgcolor=AppTheme.niko_bgcolor
                ),
                padding=ft.Padding.only(top=30, bottom=20),
                alignment=ft.Alignment.CENTER
            ),

            ft.Divider(color="grey"),

            ft.NavigationDrawerDestination(
                icon_content = ft.Icon(ft.Icons.HOME_OUTLINED, color=AppTheme.niko_blue),
                label="İlanlar",
                selected_icon=ft.Icons.HOME
            ),

            ft.NavigationDrawerDestination(
                icon_content = ft.Icon(ft.Icons.PEOPLE_OUTLINE, color=AppTheme.niko_blue),
                label="Müşteriler",
                selected_icon=ft.Icons.PEOPLE
            ),

            ft.Divider(color="grey"),

            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.Icons.LOGOUT, color=AppTheme.niko_red),
                label="Güvenli Çıkış",
            ),
        ]