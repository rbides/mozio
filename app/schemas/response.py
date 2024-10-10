from uuid import UUID
from pydantic import BaseModel


class BaseResponse(BaseModel):
    details: str


class CreateProviderResponse(BaseResponse):
    provider_id: UUID


class CreateServiceAreaResponse(BaseResponse):
    area_id: UUID