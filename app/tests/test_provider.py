import uuid
from pydantic import ValidationError
import pytest
from app.routers.provider import (
    create,
    update,
    delete,
    get,
    get_by_id,
)
from app.schemas.provider import CreateProviderRequest

def test_create_provider_success(valid_create_provider_request, db_session, mocker):
    mocker.patch("app.service.provider.repo.add", lambda x: True)
    resp = create(valid_create_provider_request)
    assert resp.get("details") == "Provider Created"
    assert type(resp.get("provider_id")) == uuid.UUID


@pytest.mark.xfail(raises=ValidationError)
def test_create_provider_failure(invalid_create_provider_request, db_session, mocker):
    create(invalid_create_provider_request)


#TODO