import os
from supabase import create_client, Client
from dotenv import load_dotenv

# 1. .env dosyasındaki değişkenleri yükle
load_dotenv()

# 2. Değişkenleri al
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# 3. Kontrol Mekanizması (Güvenlik Önlemi)
# Eğer anahtarlar bulunamazsa program çöker, böylece hatayı hemen fark ederiz.
if not url or not key:
    raise ValueError("HATA: .env dosyasında SUPABASE_URL veya SUPABASE_KEY eksik!")

# 4. İstemciyi (Client) oluştur
# Bu 'supabase' değişkenini diğer dosyalarda import ederek kullanacağız.
supabase: Client = create_client(url, key)

# ... (yukarıdaki kodlar aynen kalıyor)

if __name__ == "__main__":
    try:
        # Bağlantıyı test etmek için basit bir işlem yapalım
        # Auth servisi hazır mı diye kontrol ediyoruz
        print("--- BAĞLANTI TESTİ BAŞLIYOR ---")
        print(f"Supabase URL: {url}")
        
        # Eğer client oluştuysa ve auth servisine erişebiliyorsak bağlantı başarılıdır.
        # Henüz giriş yapmadığımız için session 'None' dönecektir, bu normal.
        session = supabase.auth.get_session()
        print("Bağlantı Başarılı! Supabase ile iletişim kuruldu.")
        print("--- TEST TAMAMLANDI ---")
        
    except Exception as e:
        print(f"!!! BAĞLANTI HATASI !!!: {e}")