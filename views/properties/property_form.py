import flet as ft
from services.property_service import PropertyService
from services.customer_service import CustomerService

class PropertyForm(ft.Column):
    def __init__(self, page, user_id, on_save_success, on_cancel):
        super().__init__()
        self.page = page
        self.user_id = user_id
        self.on_save_success = on_save_success # Kayıt bitince ne yapayım? (Listeye dön)
        self.on_cancel = on_cancel # İptal edilirse ne yapayım? (Listeye dön)

        # Formun genişliğini kısıtlayalım ki çok yayılmasın
        self.width = 600
        self.spacing = 15

        # Formu oluştur
        self.build_form()

        def build_form(self):
            """Form elemanlarını oluşturur"""
            musteriler = CustomerService.get_customers(self.user_id)

            if not musteriler:
                self.controls = [
                    ft.Icon(ft.Icons.WARNING_AMBER, color="orange", size=50),
                    ft.Text("Dikkat: Hiç Kayıtlı Müşteri Yok!", size=20, weight="bold"),
                    ft.Text("İlan eklemeden önce en az bir müşteri eklemelisiniz."),
                    ft.Container(height=20),
                    ft.OutlinedButton("Geri Dön", on_click=on_cancel)
                ]
                return
            
            # 3. Müşterileri Dropdown formatına çevir
            # key=ID (Database için), text=İsim (Görünüm için)

            options = [
                ft.Dropdown.options(key=str(m['id']), text=m['full_name'])
                for m in musteriler
            ]

            # --- FORM ELEMANLARI ---

            self.dd_musteri = ft.Dropdown(
                label="Mülk Sahibi(Müşteri Seç)",
                options=options,
                border_radius=10,
                prefix_icon=ft.Icons.PERSON
            )

            self.txt_baslik = ft.TextField(
                label="İlan Başlığı (Örn: 3+1 Deniz Manzaralı)",
                border_radius=10,
                prefix_icon=ft.Icons.TITLE
            )

            self.txt_fiyat = ft.TextField(
                label="Fiyat (TL)",
                keyboard_type=ft.KeyboardType.NUMBER,
                border_radius=10,
                prefix_icon=ft.Icons.MONEY,
                suffix_text="₺"
            )

            self.txt_konum = ft.TextField(
                label="Konum",
                border_radius=10,
                prefix_icon=ft.Icons.LOCATION_ON
            )

            # Elemanları ekrana diz
            self.controls = [
                ft.Text("Yeni İlan Ekle", size=25, weight="bold"),
                ft.Divider(),

                self.dd_musteri,
                self.txt_baslik,
                self.txt_fiyat,
                self.txt_konum,

                ft.Container(height=20),

                ft.Row([
                    ft.ElevatedButton(
                        "Kaydet",
                        icon=ft.Icons.SAVE,
                        bgcolor="blue",
                        color="white",
                        on_click=self.save,
                        height=50
                    ),
                    ft.OutlinedButton(
                        "İptal",
                        on_click=self.on_cancel,
                        height=50
                    )
                ], spacing=20)
            ]

        def save(self, e):
            """Kaydet butonuna basılınca çalışır"""
            # Basit Validasyon (Boş mu?)
            if not self.dd_musteri.value:
                self.dd_musteri.error_text = "Lütfen bir müşteri seçin"
                self.dd_musteri.update()
                return
            if not self.txt_baslik.value:
                self.txt_baslik.error_text = "Başlık boş olamaz"
                self.txt.baslik.update()
                return
            
            # Servisi Çağır (Veritabanına Yaz)
            try:
                fiyat = int(self.txt_fiyat.value) # Sayıya çevir
            except:
                fiyat = 0 # Hatalı girerse 0 yap

            res = PropertyService.add_property(
                user_id=self.user_id,
                title=self.txt_baslik.value,
                price=fiyat,
                location=self.txt_konum.value,
                customer_id=int(self.dd_musteri.value)
            )

            if res["success"]:
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Text("İlan Başarıyla Eklendi! ✅"),
                    bgcolor="green"
                )
                self.snack_bar.open = True
                self.page.update()

                self.on_save_success()
            else:
                # Hata Mesajı
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"Hata: {res['message']}"), 
                    bgcolor="red"
                )
                self.page.snack_bar.open = True
                self.page.update()