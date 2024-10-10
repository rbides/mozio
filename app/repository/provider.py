from typing import List
from uuid import UUID

from sqlalchemy import delete, update
from app.database.models.provider import ProviderEntity
from app.database.session import Session

class ProviderRepository:

    def add(self, provider: ProviderEntity):
        with Session.begin() as session:
            session.add(provider)

    def update(self, provider_id: UUID, provider: dict):
        with Session.begin() as session:
            session.execute(
                update(ProviderEntity)
                    .where(ProviderEntity.id==provider_id)
                    .values(provider)
            )

    def get(self) -> List[ProviderEntity]:
        with Session() as session:
            providers = session.query(ProviderEntity).all()
        return providers
    
    def get_by_id(self, provider_id: UUID) -> ProviderEntity:
        with Session() as session:
            provider = session.query(ProviderEntity).get(provider_id)
        return provider

    def delete(self, provider_id: UUID):
        with Session.begin() as session:
            provider = session.query(ProviderEntity).get(provider_id)
            session.delete(provider)
