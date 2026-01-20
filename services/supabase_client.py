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