from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr

from app.schemas import enums
from pydantic_extra_types.phone_numbers import PhoneNumber


class Provider(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    email: str
    phone: str
    language: enums.LanguageEnum
    currency: enums.CurrencyEnum
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class CreateProviderRequest(BaseModel):
    name: str
    email: EmailStr
    phone: PhoneNumber
    language: enums.LanguageEnum
    currency: enums.CurrencyEnum


class UpdateProviderRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[PhoneNumber] = None
    language: Optional[enums.LanguageEnum] = None
    currency: Optional[enums.CurrencyEnum] = None
