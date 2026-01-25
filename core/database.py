import os
from supabase import create_client, Client
from dotenv import load_dotenv

# 1. .env dosyasındaki değişkenleri yükle
load_dotenv()

# 2. Değişkenleri al
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# 3. Kontrol Mekanizması
if not url or not key:
    raise ValueError("HATA: .env dosyasında SUPABASE_URL veya SUPABASE_KEY eksik!")

# 4. İstemciyi oluştur
# DÜZELTME BURADA: Değişkenin adını 'supabase' yerine 'db_client' yaptık.
# Artık diğer dosyalar bunu bulabilecek.
db_client: Client = create_client(url, key)

if __name__ == "__main__":
    try:
        print("--- BAĞLANTI TESTİ BAŞLIYOR ---")
        print(f"Supabase URL: {url}")
        
        # Test ederken de artık db_client kullanıyoruz
        session = db_client.auth.get_session()
        print("Bağlantı Başarılı! Supabase ile iletişim kuruldu.")
        print("--- TEST TAMAMLANDI ---")
        
    except Exception as e:
        print(f"!!! BAĞLANTI HATASI !!!: {e}")