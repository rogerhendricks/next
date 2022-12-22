from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


# shared properties
class DeviceBase(BaseModel):
    id: int
    company: str
    model: str
    device_type: str
    hazard: Optional[bool] = False
    mri: Optional[bool] = False
    created_at: Optional[date] = datetime.now().date()

    class Config:
        orm_mode = True


# this will be used to validate data while creating a Device
class DeviceCreate(DeviceBase):
    company: str
    model: str
    device_type: str
    hazard: Optional[bool] = False
    mri: Optional[bool] = False

    class Config:
        orm_mode = True


# this will be used to format the response to not to have id, etc.
class ShowDevice(DeviceBase):
    company: str
    model: str
    device_type: str
    hazard: Optional[bool] = False
    mri: Optional[bool] = False

    class Config:
        orm_mode = True

