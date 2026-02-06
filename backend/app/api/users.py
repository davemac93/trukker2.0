from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models import user
from app.schemas.user import DriverProfile, CompanyProfile
from app.models.user import Driver, User, UserRole, DrivingLicenseCategory, Employer
from app.api.deps import get_current_user_data



router = APIRouter(prefix="/users")



@router.post("/")
async def read_users(db: Session = Depends(get_db)):
    return db.query(user).all()

@router.post("/driver")
async def create_driver_profile(
    profile: DriverProfile, 
    db : Session = Depends(get_db), 
    user_data: dict = Depends(get_current_user_data)
    ):
    existing_user = db.query(User).filter(User.id == user_data.id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        id = user_data.id,
        email = user_data.email,
        role = UserRole.DRIVER
    )

    db.add(new_user)

    new_driver = Driver(
        user_id = user_data.id,
        first_name = profile.first_name,
        last_name = profile.last_name,
        phone = profile.phone,
    )


    db.add(new_driver)
    db.flush() 
    
    for category in profile.license:
        license_categories = DrivingLicenseCategory(
            driver_id = new_driver.id,
            category = category
        )
        db.add(license_categories)


    db.commit()
    db.refresh(new_driver)
    return new_driver

@router.post("/employer")
async def create_employer_profile(employer: CompanyProfile, db: Session = Depends(get_db), user_data: dict = Depends(get_current_user_data)):
    exisiting_user = db.query(User).filter(User.id == user_data.id).first()
    if exisiting_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        id = user_data.id,
        email = user_data.email,
        role = UserRole.EMPLOYER
    )

    db.add(new_user)

    new_employer = Employer(
        user_id = new_user.id,
        company_name = employer.company_name,
        phone = employer.phone
    )

    db.add(new_employer)    
    db.commit()
    db.refresh(new_employer)
    return new_employer

@router.get("/me")
async def get_my_data(user_data: dict = Depends(get_current_user_data)):
    return user_data


@router.get("/debug-me")
async def debug_me(user_data = Depends(get_current_user_data)):

    return {
        "raw_data": str(user_data),
        "extracted_id": getattr(user_data, "id", "Nie znaleziono ID"),
        "extracted_email": getattr(user_data, "email", "Nie znaleziono Email")
    }