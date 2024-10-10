from datetime import datetime
import json
import pickle
from typing import Any, List, Optional, Tuple
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator, field_serializer, model_validator

import shapely
from app.database.models.service_area import ServiceAreaEntity
from app.schemas import enums
from pydantic_extra_types.phone_numbers import PhoneNumber
from decimal import Decimal
from geoalchemy2.elements import WKBElement
from geoalchemy2 import functions

class ServiceArea(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    provider_id: UUID
    name: str
    price: Decimal = Field(decimal_places=2, ge=0)
    polygon: dict
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @field_validator('polygon', mode='before')
    def serialize_polygon(cls, v: WKBElement):
        value = shapely.to_geojson(
            shapely.from_wkb(str(v))
        )
        return json.loads(value)


class CreateServiceAreaRequest(BaseModel):
    provider_id: UUID
    name: str
    price: Decimal = Field(decimal_places=2, ge=0)
    polygon: list[tuple[float, float]] = Field(min_length=4)

class UpdateServiceAreaRequest(BaseModel):
    provider_id: Optional[UUID] = None
    name: Optional[str] = None
    price: Optional[Decimal] = Field(None, decimal_places=2, ge=0)


class GetFromPointResponse(BaseModel):
    name: str
    provider_name: str
    price: float


    @model_validator(mode='before')
    @classmethod
    def serialize_provider_name(cls, data: ServiceAreaEntity) -> dict:
        """Temporary workaround for getting the provider_name correctly"""
        return {
            "name": data.name,
            "provider_name": data.provider_name,
            "price": data.price
        }