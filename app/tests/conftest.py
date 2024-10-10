import pytest

from app.schemas.provider import CreateProviderRequest
from app.database.session import Session

@pytest.fixture()
def db_session():
    session = Session()
    yield session
    session.rollback()
    session.close()

@pytest.fixture()
def valid_create_provider_request():
    return CreateProviderRequest(
        name= "test1",
        email= "test1@email.com",
        phone= "+447911123456",
        language= "PT",
        currency= "BRL",
    )

@pytest.fixture()
def invalid_create_provider_request():
    return CreateProviderRequest(
        name= "test1",
        email= "test1@email.com",
        phone= "+447911123456",
        language= "PTqweqwe",
        currency= "BRL",
    )