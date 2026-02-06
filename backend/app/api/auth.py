from fastapi import APIRouter

from app.schemas.user import SignUp, SignIn
from app.core.supabase import supabase

router = APIRouter(prefix="/auth")

@router.post("/signup")
async def sign_up(user: SignUp):
    response = supabase.auth.sign_up(
        {
            "email": user.email,
            "password": user.password
        }
    )
    return response

@router.post("/signin")
async def sign_in(user: SignIn):
    response = supabase.auth.sign_in_with_password(
        {
            "email": user.email,
            "password": user.password
        }
    )
    return response

