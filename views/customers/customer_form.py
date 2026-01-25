import flet as ft
from services.customer_service import CustomerService

class CustomerForm(ft.Column):
    def __init__(self, page, user_id, on_save_success, on_cancel):
        super().__init__()
        self.page = page
        self.user_id = user_id
        self.on_save_success = on_save_success
        self.on_cancel = on_cancel
        self.width = 600
        self.spacing = 20

        # Form Alanlarını Oluşturur
        self.build_form()

        def build_form(self):
            # 1. İsim Alanı
            self.name_box = ft.TextField(
                label="Müşteri Adı Soyadı",
                border_radius=10,
                prefix_icon=ft.Icons.PERSON
            )

            # 2. Telefon Alanı
            self.phone_box = ft.TextField(
                label="Telefon Numarası",
                border_radius=10,
                prefix_icon=ft.Icons.PHONE,
                keyboard_type=ft.KeyboardType.PHONE
            )

            # 3. Elemanları Ekrana Diz
            self.controls = [
                ft.Text("Yeni Müşteri Ekle", size=25, weight="bold"),
                ft.Divider(),

                self.name_box,
                self.phone_box,

                ft.Container(height=10),

                ft.Row([
                    ft.ElevatedButton(
                        "Kaydet",
                        icon=ft.Icons.SAVE,
                        bgcolor="orange",
                        color="white",
                        height=50,
                        on_click=self.save
                    ),

                    ft.OutlinedButton(
                        "İptal",
                        height=50,
                        on_click=self.on_cancel
                    )
                ], spacing=20)
            ]

        def save(self, e):
            """Kaydet Butonuna Basılınca"""
            # Boş mu kontrolü
            if not self.name_box.value:
                self.name_box.error_text = "İsim boş olamaz"
                self.name_box.update()
                return
            
            res = CustomerService.add_customer(
                self.user_id,
                self.name_box.value,
                self.phone_box.value
            )

            if res["success"]:
                # Başarılı Mesajı
                self.page.snack_bar = ft.SnackBar(ft.Text("Müşteri Kaydedildi! ✅"), bgcolor="green")
                self.page.snack_bar.open = True
                self.page.update()
                
                # Listeye Geri Dön
                self.on_save_success()
            else:
                # Hata Mesajı
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Hata: {res['message']}"), bgcolor="red")
                self.page.snack_bar.open = True
                self.page.update()