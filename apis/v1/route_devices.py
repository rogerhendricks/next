from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException, status
from typing import List
from db.session import get_db
from db.models.devices import Device
from schemas.devices import DeviceCreate, ShowDevice
from db.repository.device import create_new_device, retrieve_device, list_devices

router = APIRouter()


@router.post("/create-device/", response_model=ShowDevice)
def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    current_user = 1
    device = create_new_device(device=device, db=db, created_by=current_user)
    return device


@router.get("/get/{id}",response_model=ShowDevice) # if we keep just "{id}" . it would stat catching all routes
def read_device(id:int, db:Session = Depends(get_db)):
    device = retrieve_device(id=id, db=db)
    if not device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Device with this id {id} does not exist")
    return device


@router.get("/all", response_model=List[ShowDevice]) #new
def read_devices(db: Session = Depends(get_db)):
    devices = list_devices(db=db)
    return devices
