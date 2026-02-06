from app.core.config import setting
from supabase import create_client, Client


url: str = setting.SUPABASE_URL
key: str = setting.SUPABASE_KEY

try:
    supabase: Client = create_client(url, key)
    print("Supabase connected")
except Exception as e: 
    print(f"Failed to connect to Supabase {e}")
