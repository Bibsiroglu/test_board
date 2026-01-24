from core.database import db_client

class CustomerService:
    """
    Müşteri (Mülk Sahibi) işlemlerini yöneten servis.
    """

    @staticmethod
    def add_customer(user_id, full_name, phone, notes=""):
        """
        Yeni bir müşteri kaydeder.
        """
        try:
            # Supabase'e gidecek paket
            data = {
                "user_id": user_id,      # Müşteri kime ait? (Emlakçı ID)
                "full_name": full_name,  # Ad Soyad
                "phone": phone,          # Telefon
                "notes": notes           # Notlar (Opsiyonel)
            }
            
            # Veritabanına 'insert' (ekleme) yapıyoruz
            db_client.table("customers").insert(data).execute()
            
            return {"success": True, "message": "Müşteri başarıyla eklendi :)))."}
            
        except Exception as e:
            # Bir hata olursa (örn: veritabanı kapalıysa)
            print(f"HATA: {e}")
            return {"success": False, "message": "Kaydedilemedi!!!: " + str(e)}

    @staticmethod
    def get_customers(user_id):
        """
        Sadece giriş yapan kullanıcının müşterilerini getirir.
        """
        try:
            # 'select(*)' diyerek tüm sütunları çekiyoruz
            # 'eq' (equals) diyerek sadece benim eklediklerimi süzüyoruz
            res = db_client.table("customers").select("*").eq("user_id", user_id).execute()
            
            # Veriyi (listeyi) olduğu gibi dönüyoruz
            return res.data
            
        except Exception as e:
            print(f"HATA!!!: {e}")
            return []