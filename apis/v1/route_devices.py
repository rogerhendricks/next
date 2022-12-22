from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException, status
from typing import List
from db.session import get_db
from db.models.devices import Device
from schemas.devices import DeviceCreate, ShowDevice
from db.repository.device import create_new_device, retrieve_device, list_devices, delete_device_by_id

router = APIRouter()

@router.get("/all", response_model=List[ShowDevice])
def read_devices(db: Session = Depends(get_db)):
    devices = list_devices(db=db)
    return devices


@router.post("/create-device/", response_model=ShowDevice)
def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    device = create_new_device(device=device, db=db)
    return device


@router.get("/get/{id}",response_model=ShowDevice) # if we keep just "{id}" . it would stat catching all routes
def read_device(id:int, db:Session = Depends(get_db)):
    device = retrieve_device(id=id, db=db)
    if not device:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Device with this id {id} does not exist")
    return device


@router.delete("/delete/{id}")
def delete_device(id: int, db: Session = Depends(get_db)):
    message = delete_device_by_id(id=id, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Device with id {id} not found")
    return {"msg": "Successfully deleted."}

# TO ADD AUTHORIZATION TO DELETE
# @router.delete("/delete/{id}")
# def delete_job(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
#     job = retreive_job(id =id,db=db)
#     if not job:
#         return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with {id} does not exist")
#     print(job.owner_id,current_user.id,current_user.is_superuser)
#     if job.owner_id == current_user.id or current_user.is_superuser:
#         delete_job_by_id(id=id,db=db,owner_id=current_user.id)
#         return {"msg":"Successfully deleted."}
#     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail=f"You are not permitted!!!!")