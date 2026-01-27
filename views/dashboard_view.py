import flet as ft
from components.navbar import NavBar
from core.database import db_client
from core.theme import AppTheme

from views.properties.property_list import PropertyList
from views.properties.property_form import PropertyForm
from views.customers.customer_list import CustomerList
from views.customers.customer_form import CustomerForm

class DashboardView(ft.Container):
    def __init__(self, page: ft.Page, on_logout):
        super().__init__()
        self.page = page
        self.on_logout = on_logout
        self.expand=True

        try:
            session = db_client.auth.get_session()
            self.user_id = session.user.id
        except:
            self.user_id = "test-user-id"
        
        self.page.appbar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.MENU,
                icon_color="white",
                on_click=lambda e: self.page.open_drawer()
            ),
            title=ft.Text("NikoCRM - Yönetim Paneli", color="white", weight="bold"),
            center_title=True,

            bgcolor=AppTheme.niko_blue,

            actions=[
                ft.IconButton(
                    ft.Icons.LOGOUT,
                    icon_color="white",
                    tooltip="Çıkış Yap",
                    on_click=lambda e:self.logout()
                )
            ]
        )

        self.nav_drawer = NavBar(on_change_function=self.handle_menu_change)
        self.page.drawer = self.nav_drawer

        self.content_area = ft.Container(padding=20, expand=True)

        self.show_property_list()

        self.content = self.content_area

    def show_property_list(self):
        self.content_area.content = PropertyList(
            user_id=self.user_id,
            on_add_click=self.show_property_form
        )
        self.content_area.update()

    def show_property_form(self, e=None):
        self.content_area.content = PropertyForm(
            page=self.page,
            user_id=self.user_id,
            on_save_success=self.show_property_list,
            on_cancel=self.show_property_list
        )
        self.content_area.update()
    
    def show_customer_list(self):
        self.content_area.content = CustomerList(
            user_id=self.user_id,
            on_add_click=self.show_customer_form
        )
        self.content_area.update()
    
    def show_customer_form(self, e=None):
        self.content_area.content = CustomerForm(
            page=self.page,
            user_id=self.user_id,
            on_save_success=self.show_customer_list,
            on_cancel=self.show_customer_list
        )
        self.content_area.update()
    
    def handle_menu_change(self, e):
        self.page.close_drawer()

        secilen_index = e.control.selected_index

        if secilen_index == 0:
            self.show_property_list()
        elif secilen_index == 1:
            self.show_customer_list()
        elif secilen_index == 2:
            self.logout()
            
    def logout(self):
        """Sistemden Çıkış Yap"""
        # 1. Supabase oturumunu kapat
        db_client.auth.sign_out()
        
        # 2. AppBar ve Menüyü temizle (Login ekranında görünmemeli)
        self.page.appbar = None 
        self.page.drawer = None 
        self.page.update()
        
        # 3. Navigation'a haber ver: "Beni Login ekranına at"
        self.on_logout()