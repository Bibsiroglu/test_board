from core.database import db_client

class PropertyService:
    """
    İlan (Gayrimenkul) işlemlerini yöneten servis.
    """

    @staticmethod
    def add_property(user_id, title, price, location, customer_id):
        """
        Yeni bir ilan ekler ve bir müşteriye bağlar.
        """
        try:
            data = {
                "user_id": user_id,
                "title": title,
                "price": price,
                "location": location,
                "customer_id": customer_id, # <-- YENİ: İlanın sahibi kim?
                "status": "Satılık"
            }
            
            # Veritabanına ekle
            db_client.table("properties").insert(data).execute()
            
            return {"success": True, "message": "İlan başarıyla eklendi!"}
            
        except Exception as e:
            return {"success": False, "message": f"Hata: {str(e)}"}

    @staticmethod
    def get_properties_by_user(user_id):
        """
        Kullanıcının ilanlarını VE o ilanın sahibinin bilgilerini getirir.
        """
        try:
            # SİHİRLİ KISIM: select("*, customers(*)")
            # Bu kod şu demek: "İlanın her şeyini al (*), AYRICA bağlı olduğu customers tablosundaki bilgileri de al."
            response = db_client.table("properties").select("*, customers(*)").eq("user_id", user_id).execute()
            
            return {"success": True, "data": response.data}
            
        except Exception as e:
            return {"success": False, "message": str(e)}