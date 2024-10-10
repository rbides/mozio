
from datetime import datetime
import logging
from typing import List, Optional
from uuid import UUID
import uuid

from pydantic import TypeAdapter

from app.repository.provider import ProviderRepository
from app.schemas.provider import CreateProviderRequest, Provider, UpdateProviderRequest
from app.database.models import provider as entities

repo = ProviderRepository()

def create_provider(provider: CreateProviderRequest):
    id = uuid.uuid4()
    repo.add(
        entities.ProviderEntity(
            id = id,
            name = provider.name,
            email = provider.email,
            phone = provider.phone,
            language = provider.language,
            currency = provider.currency,
        )
    )
    return id


def update_provider(provider_id: UUID, provider: UpdateProviderRequest):
    p = provider.model_dump(exclude_none=True, exclude_unset=True)
    if not p.items():
        return
    p["updated_at"] = datetime.now()
    repo.update(provider_id, p)


def get_providers() -> List[Provider]:
    ta = TypeAdapter(List[Provider])
    return ta.validate_python(repo.get())


def get_provider_by_id(provider_id: UUID) -> Optional[Provider]:
    return Provider.model_validate(repo.get_by_id(provider_id))


def delete_provider(provider_id: UUID):
    repo.delete(provider_id)