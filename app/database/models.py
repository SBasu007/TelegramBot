
from sqlalchemy import Boolean, Column, Integer, String
from .db import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, index=True)
    name = Column(String)
    age = Column(Integer)
    sex = Column(String)
    phone_number = Column(String)
    profile_completed = Column(Boolean, default=False)

    
