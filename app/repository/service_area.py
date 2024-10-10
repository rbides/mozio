from uuid import UUID

from shapely import Point
from sqlalchemy import delete, select, update
from app.database.models.provider import ProviderEntity
from app.database.models.service_area import ServiceAreaEntity
from app.database.session import Session
from geoalchemy2 import functions


class ServiceAreaRepository:
    
    def add(self, area: ServiceAreaEntity):
        with Session.begin() as session:
            session.add(area)

    def update(self, area_id: UUID, area: dict):
        with Session.begin() as session:
            session.execute(
                update(ServiceAreaEntity)
                    .where(ServiceAreaEntity.id==area_id)
                    .values(area)
            )

    def get(self) -> list[ServiceAreaEntity]:
        with Session() as session:
            areas = session.query(ServiceAreaEntity).all()
        return areas
    
    def get_by_id(self, area_id: UUID) -> ServiceAreaEntity:
        with Session() as session:
            area = session.query(ServiceAreaEntity).get(area_id)
        return area

    def delete(self, area_id: UUID):
        with Session.begin() as session:
            area = session.query(ServiceAreaEntity).get(area_id)
            session.delete(area)


    def get_from_point(self, point: Point) -> list[ServiceAreaEntity]:
        with Session.begin() as session:
            areas = session.query(ServiceAreaEntity) \
                .join(ProviderEntity) \
                .filter( \
                    ServiceAreaEntity.polygon.intersects(point.wkt) \
                )
        # for a in areas:
            # print(a.provider_name)
        return areas