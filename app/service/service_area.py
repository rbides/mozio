
from datetime import datetime
from typing import Optional
from uuid import UUID
import uuid

from pydantic import TypeAdapter

from app.database.models.service_area import ServiceAreaEntity
from app.repository.service_area import ServiceAreaRepository
from app.schemas.service_area import CreateServiceAreaRequest, GetFromPointResponse, ServiceArea, UpdateServiceAreaRequest
from shapely import Point, Polygon



repo = ServiceAreaRepository()

def create_area(area: CreateServiceAreaRequest):
    id = uuid.uuid4()
    repo.add(
        ServiceAreaEntity(
            id = id,
            provider_id = area.provider_id,
            name = area.name,
            price = area.price,
            polygon = Polygon(area.polygon).wkt
        )
    )
    return id


def update_area(area_id: UUID, area: UpdateServiceAreaRequest):
    a = area.model_dump(exclude_none=True, exclude_unset=True)
    if not a.items():
        return
    a["updated_at"] = datetime.now()
    repo.update(area_id, a)


def get_areas() -> list[ServiceArea]:
    ta = TypeAdapter(list[ServiceArea])
    return ta.validate_python(repo.get())


def get_area_by_id(area_id: UUID) -> Optional[ServiceArea]:
    return ServiceArea.model_validate(repo.get_by_id(area_id))


def delete_area(area_id: UUID):
    repo.delete(area_id)


def get_from_point(lat: float, lng: float) -> list[GetFromPointResponse]:
    point = Point(lat, lng)
    areas = repo.get_from_point(point)
    ta = TypeAdapter(list[GetFromPointResponse])
    return ta.validate_python(areas)
