import uuid
import enum

from app.core.database import Base

from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship


class UserRole(enum.Enum):
    DRIVER = "driver"
    EMPLOYER = "employer"


class User(Base):
    __tablename__: str = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    role = Column(Enum(UserRole))
    email = Column(String, nullable=False, unique=True)
    driver = relationship("Driver", back_populates="user", uselist=False)
    employer = relationship("Employer", back_populates="user", uselist=False)
    

    def __repr__(self):
        return f"User id: {self.id}, Email: {self.email}, Role: {self.role}"
    
class Driver(Base):
    __tablename__ = "driver"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(ForeignKey(User.id))
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    phone = Column(String, nullable= False) 

    user = relationship("User", back_populates="driver")
    license = relationship("DrivingLicenseCategory", back_populates='driver')

class DrivingLicenseCategory(Base):
    __tablename__ = "driving_license_category"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    driver_id = Column(ForeignKey(Driver.id))
    category = Column(String, nullable=False)

    driver = relationship("Driver", back_populates="license")


class Employer(Base):
    __tablename__ = "company"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(ForeignKey(User.id))
    company_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    user = relationship("User", back_populates="employer")