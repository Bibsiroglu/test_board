import flet as ft
from services.auth_service import AuthService

class LoginView(ft.Container):
    def __init__(self, page: ft.Page, on_success):
        super().__init__()
        self.main_page = page
        self.on_success = on_success
        self.expand = True
        self.alignment = ft.Alignment(0, 0) # Sayfanın tam ortası
        self.bgcolor = ft.Colors.BLUE_GREY_50 # Arka plan rengi

        # --- TEMİZLİK ZAMANI ---
        # Eğer kullanıcı Dashboard'dan çıkış yapıp buraya geldiyse,
        # Dashboard'a ait menüleri (Drawer, AppBar, FAB) siliyoruz.
        self.main_page.appbar = None
        self.main_page.drawer = None
        self.main_page.floating_action_button = None
        self.main_page.update()

    def show_snack(self, msg, color):
        """Alt tarafta çıkan bilgi kutucuğu"""
        self.main_page.snack_bar = ft.SnackBar(ft.Text(msg), bgcolor=color)
        self.main_page.snack_bar.open = True
        self.main_page.update()

    