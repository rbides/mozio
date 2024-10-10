from uuid import UUID
from fastapi import APIRouter, HTTPException

from app.schemas.response import BaseResponse, CreateServiceAreaResponse
from app.schemas.service_area import CreateServiceAreaRequest, GetFromPointResponse, ServiceArea, UpdateServiceAreaRequest
from app.service import service_area


router = APIRouter(
    prefix="/areas",
)


@router.post(
        "",
        status_code=201,
        response_model=CreateServiceAreaResponse,
        summary = "Create Service Area",
        response_description = "A success message and the id of the created area",
    )
def create(request: CreateServiceAreaRequest):
    """Create a ServiceArea object in the database"""
    try:
        area_id = service_area.create_area(request)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=f"Provider {request.provider_id} does not exist")
    return {
        "details": "Service Area Created",
        "area_id": area_id
    }


@router.put(
        "/{area_id}",
        status_code=200,
        response_model=BaseResponse,
        summary = "Update a service area",
        response_description = "A success message",
    )
def update(area_id: UUID, request: UpdateServiceAreaRequest):
    try:
        service_area.update_area(area_id, request)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Provider {request.provider_id} does not exist")
    return {
        "details": "Service Area Updated"
    }

@router.delete(
        "/{area_id}",
        status_code=200,
        response_model=BaseResponse,
        summary = "Delete a service area",
        response_description = "A success message",
    )
def delete(area_id: UUID):
    try:
        service_area.delete_area(area_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Service Area not found")
    return {
        "details": "Service Area Deleted"
    }

@router.get(
        "/point",
        status_code=200,
        response_model=list[GetFromPointResponse],
        summary = "Get a point intersections",
        response_description = "A list of Service Areas that intersects with the point",
    )
def get_from_point(lat: float, lng: float):
    """
    Get a list of the Service Areas that intersects with a given point, built with (lat, lng)

        - **lat**: Latitude
        - **lng**: Longitude
    """
    return service_area.get_from_point(lat, lng)

@router.get(
        "",
        status_code=200,
        response_model=list[ServiceArea],
        summary = "Get all Service Areas",
        response_description = "A list with all the existing Service Areas",
    )
def get():
    try:
        return service_area.get_areas()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Could not get service areas")


@router.get(
        "/{area_id}",
        status_code=200,
        response_model=ServiceArea,
        summary = "Get a specific service area by it's id",
        response_description = "A Service area object",
    )
def get_by_id(area_id: UUID):
    try:
        return service_area.get_area_by_id(area_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Service Area not found")
