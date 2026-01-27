import flet as ft 

from views.login_view import LoginView
from views.dashboard_view import DashboardView

class Router:
    def __init__(self, page: ft.Page):

        self.page = page

        self.routes = {
            "login": self.view_login,
            "app": self.view_main_app
        }

        self.body = ft.Container(expand=True)

    def get_content(self):
        return self.body

    def go(self, route_key):

        if route_key in self.routes:
            self.routes[route_key]()
            self.page.update()

    def view_login(self):
        self.body.content = LoginView(
            self.page,
            on_success=lambda: self.go("app")
        )
    
    def view_main_app(self):
        self.body.content = DashboardView(
            self.page,
            on_logout=lambda: self.go("login")
        )