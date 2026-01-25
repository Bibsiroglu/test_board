import flet as ft
from services.property_service import PropertyService

class PropertyList(ft.Column):
    def __init__(self, user_id, on_add_click):
        super().__init__()
        self.user_id = user_id
        self.on_add_click = on_add_click
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO

        self.header = ft.Row(
            controls=[
                ft.Text("İlan Portföyüm", size=28, weight="bold", color=ft.Colors.BLUE_GREY_800),
                ft.IconButton(
                    icon=ft.Icons.ADD_CIRCLE,
                    icon_color="blue",
                    icon_size=40,
                    tooltip="Yeni İlan Ekle",
                    on_click=on_add_click
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.items_container =ft.Column(spacing=10)

        self.controls =  [
            self.header,
            ft.Divider(thickness=1, color="grey"),
            self.items_container
        ]

        self.load_data()

        res = PropertyService.get_properties_by_user(self.user_id)

        if res["success"]:
            ilanlar = res["data"]

            if not ilanlar:
                self.items_container.controls.append(
                    ft.Container(
                        content=ft.Text("Henüz hiç ilan eklemediniz.", size=16, color="grey"),
                        alignment=ft.Alignment.CENTER,
                        padding=20
                    )
                )
            else:
                for ilan in ilanlar:
                    sahibi = "Bilinmiyor"
                    if ilan.get("customers"):
                        sahibi = ilan["customers"].get("full_name", "Bilinmiyor")
            
            kart = ft.Card(
                elevation=2,
                content=ft.Container(
                    padding=10,
                    content=ft.ListTile(
                        leading=ft.Icon(ft.Icons.HOME_WORK, color="blue", size=30),
                        title=ft.Text(ilan["title"], weight="bold"),
                        subtitle=ft.Column(
                            [
                                ft.Text(f"📍 {ilan['location']}", size=12),
                                ft.Text(f"👤 Sahibi: {sahibi}", size=12, color="grey"),
                            ], spacing=2
                        ),
                        trailing=ft.Text(
                            f"{ilan['price']} ₺", 
                            color="green", 
                            weight="bold", 
                            size=16
                        ),
                    )
                )
            )
            self.items_container.controls.append(
                ft.Text(f"Hata oluştu: {res.get("message")}", color="red")
            )

            self.update()