from functools import cached_property
from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String, UUID
from sqlalchemy.sql import func
from app.database.models import Base
import geoalchemy2


class ServiceAreaEntity(Base):
    __tablename__ = 'service_areas'

    id = Column(UUID, primary_key=True)
    provider_id = Column(UUID, ForeignKey("providers.id"), nullable=False)
    name = Column(String, nullable=False)
    price = Column(Numeric(5, 2), nullable=False)
    polygon = Column(geoalchemy2.Geometry('POLYGON'), nullable=False) # stores geojson information in json string
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())
    
    @cached_property
    def provider_name(self):
        return self.provider.name