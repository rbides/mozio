from fastapi import FastAPI

from app.routers import health_check, provider, service_area


app = FastAPI(
    title="Mozio Assessment Task API Documentation",
    description="This is a FastAPI based application for Mozio Assessment Task",
)

app.include_router(health_check.router)
app.include_router(provider.router)
app.include_router(service_area.router)

