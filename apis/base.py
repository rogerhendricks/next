from fastapi import APIRouter
from apis.v1 import route_general
from apis.v1 import route_users
from apis.v1 import route_devices


api_router = APIRouter()
api_router.include_router(route_general.general_pages_router, prefix="", tags=["general_pages"])
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_devices.router, prefix="/devices", tags=["devices"])

