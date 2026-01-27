import flet as ft

class AppTheme:
    niko_blue = "#5ce1e6"
    niko_red = "#ff3131"
    niko_yellow = "#f6d636"
    niko_bgcolor = "#232323"

    font_family = "Adigiana Toybox"

    @staticmethod
    def apply_theme(page: ft.Page):
        page.fonts = {
            "Adigiana Toybox": "/fonts/AdigianaToyboxRegular.ttf"
        }
        
        page.theme = ft.Theme(
            color_scheme_seed=AppTheme.niko_blue,
            font_family=AppTheme.font_family,

            color_scheme=ft.ColorScheme(
                primary=AppTheme.niko_blue,
                on_primary="#ffffff",
                secondary=AppTheme.niko_red,
                tertiary=AppTheme.niko_yellow,
                background=ft.Colors.WHITE,
                surface=ft.Colors.GREY_50,
                error=AppTheme.niko_red
            ),

            use_material3=True
        )

        page.theme_mode = ft.ThemeMode.LIGHT