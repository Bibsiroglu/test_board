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

        self.email_kayit = ft.TextField(label="E-Posta Giriniz", width=300, border_radius=10, prefix_icon=ft.Icons.EMAIL)
        self.pass_kayit = ft.TextField(label="Şifre Giriniz", width=300, password=True, can_reveal_password=True, border_radius=10, prefix_icon=ft.Icons.LOCK)
        
        kayit_content = ft.Column([
            ft.Container(height=10),
            self.email_kayit,
            ft.Container(height=5),
            self.pass_kayit,
            ft.Container(height=20),
            ft.ElevatedButton("Kayıt Ol", on_click=self.handle_register, width=300, height=45, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        self.email_giris = ft.TextField(label="E-Posta", width=300, border_radius=10, prefix_icon=ft.Icons.EMAIL),
        self.pass_giris = ft.TextField(label="Şifre", password=True, can_reveal_password=True, width=300, border_radius=10, prefix_icon=ft.Icons.LOCK)

        giris_content = ft.Column([
            ft.Container(height=10),
            self.email_giris,
            ft.Container(height=5),
            self.pass_giris,
            ft.Container(height=20),
            ft.ElevatedButton("Giriş Yap", on_click=self.handle_login, width=300, height=45, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
        
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(text="Giriş Yap", icon=ft.Icons.LOGIN, content=giris_content),
                ft.Tab(text="Kayıt Ol", icon=ft.Icons.PERSON_ADD, content=kayit_content)
            ],
            width=350,
            height=350
        )

        self.content = ft.Card(
            elevation=10,
            content=ft.Container(
                padding=30,
                border_radius=15,
                bgcolor=ft.Colors.WHITE,
                content=ft.Column([
                    ft.Icon(ft.Icons.REAL_ESTATE_AGENT, size=60, color=ft.Colors.ORANGE_800),
                    ft.Text("EMLAK CRM", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900),
                    ft.Text("Profesyonel Yönetim Paneli", size=12, color=ft.Colors.GREY),
                    ft.Divider(),
                    self.tabs
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER))
            )
        

    def handle_register(self,e):
        """Kayıt butonuna basınca çalışır"""
        if not self.email_kayit.value or not self.pass_kayit.value:
            self.show_snack("Lütfen tüm alanları doldurun", ft.Colors.RED)
            return
        res = AuthService.logout_user(self.email_kayit.value, self.pass_kayit.value)

        if res["success"]:
            self.show_snack("Kayıt Başarılı! Lütfen Giriş Yapınız", ft.Colors.GREEN)
            self.tabs.selected_index = 0
            self.tabs.update()
        else:
            self.show_snack(res["message", ft.Colors.RED])
    
    def handle_login(self, e):
        if not self.email_giris.value or not self.pass_giris.value:
            self.show_snack("Lütfen tüm alanları doldurun.", ft.Colors.RED)

        res = AuthService.login_user(self.email_giris.value, self.pass_giris.value)

        if res["success"]:
            self.main_page.session.set("user_id", res["user"].id)
            self.show_snack("Giriş Başarılı! Yönlendiriliyorsunuz...", ft.Colors.GREEN)
            self.on_success()
        else:
            self.show_snack(res["message"], ft.Colors.RED)
    
