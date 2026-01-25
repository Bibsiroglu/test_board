import flet as ft
from services.customer_service import CustomerService

class CustomerList(ft.Column):
    def __init__(self, user_id, on_add_click):
        super().__init__()
        self_user_id = user_id
        self.on_add_click = on_add_click
        self.expand = True
        self.scroll = ft.ScrollMode.AUTO

        self.header = ft.Row(
            controls=[
                ft.Text("Müiteri Listesi", size=28, weight="bold", color=ft.Colors.BLUE_GREY_800),
                ft.IconButton(
                    icon=ft.Icons.PERSON_ADD,
                    icon_color="orange",
                    icon_size=40,
                    tooltip="Yeni Müşteri Ekle",
                    on_click=self.on_add_click
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        # Müşterilerin dizileceği kutu
        self.items_container = ft.Column(spacing=10)

        self.controls = [
            self.header,
            ft.Divider(thickness=1, color="grey"),
            self.items_container
        ]

        # Verileri Yükle
        self.load_data()

    def load_data(self):
        """Veritabanından müşterileri çek"""
        self.items_container.clear()

        # Servisten Listeyi Al
        musteriler = CustomerService.get_customers(self.user_id)

        if not musteriler:
            # Liste boşsa
            self.items_container.controls.append(
                ft.Container(
                    content=ft.Text("Henüz kayıtlı müşteri yok", size=16, color="grey"),
                    alignment=ft.Alignment.CENTER,
                    padding=20
                )
            )
        else:
            # Müşterileri listele
            for m in musteriler:
                kart = ft.Card(
                    elevation=2,
                    content=ft.Container(
                        padding=5,
                        content=ft.ListTile(
                            leading=ft.Icon(ft.Icons.PERSON, color="orange", size=30),
                            title=ft.Text(m['full_name'], weight="bold"),
                            subtitle=ft.Text(f"📞 {m["phone"]}" if m["phone"] else "Telefon Yok"),
                            trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT, color="grey")
                        )
                    )
                )
                self.items_container.controls.append(kart)

        self.update()