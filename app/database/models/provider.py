from sqlalchemy import Column, DateTime, Enum, String, UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.models import Base
from app.database.models.service_area import ServiceAreaEntity
from app.schemas import enums

class ProviderEntity(Base):
    __tablename__ = 'providers'

    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    language = Column(Enum(enums.LanguageEnum), nullable=False)
    currency = Column(Enum(enums.CurrencyEnum), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())
    
    service_areas = relationship(ServiceAreaEntity, cascade = "all,delete", backref = "provider")
