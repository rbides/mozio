from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException

from app.schemas.provider import CreateProviderRequest, Provider, UpdateProviderRequest
from app.schemas.response import BaseResponse, CreateProviderResponse
from app.service import provider

router = APIRouter(
    prefix="/providers",
)

@router.post(
        "",
        status_code=201,
        response_model=CreateProviderResponse,
        summary="Create Provider",
        response_description="A success message and the id of the created provider"
    )
def create(request: CreateProviderRequest):
    """
    Create a provider entry in the database

    """
    provider_id = provider.create_provider(request)
    return {
        "details": "Provider Created",
        "provider_id": provider_id,
    }


@router.put(
        "/{provider_id}",
        status_code=200,
        response_model=BaseResponse,
        summary = "Update an existing Provider",
        response_description = "A success message",
    )
def update(provider_id: UUID, request: UpdateProviderRequest):
    provider.update_provider(provider_id, request)
    return {
        "details": "Provider Updated"
    }

@router.delete(
        "/{provider_id}",
        status_code=200,
        response_model=BaseResponse,
        summary = "Delete a Provider",
        response_description = "A success message",
    )
def delete(provider_id: UUID):
    try:
        provider.delete_provider(provider_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Service Area not found")
    return {
        "details": "Provider Deleted"
    }

@router.get(
        "",
        status_code=200,
        response_model=List[Provider],
        summary = "Get providers",
        response_description = "A list with all the existing Providers",
    )
def get():
    return provider.get_providers()
    

@router.get(
        "/{provider_id}",
        status_code=200,
        response_model=Provider,
        summary = "Get a specific provider by it's id",
        response_description = "A provider object",
    )
def get_by_id(provider_id: UUID):
    try:
        return provider.get_provider_by_id(provider_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Provider not found")
