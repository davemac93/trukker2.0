import os
from dotenv import load_dotenv

load_dotenv()

class Config: 
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")

    FRONTEND_URL: str = os.getenv("FRONTEND_URL")

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    FREE_OFFER_LIMIT: int = 3
    FREE_OFFER_EXPIRED: int = 30

setting = Config()