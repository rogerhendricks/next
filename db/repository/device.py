from sqlalchemy.orm import Session

from schemas.devices import DeviceCreate, ShowDevice
from db.models.devices import Device


def create_new_device(device: DeviceCreate, db: Session, owner_id: int):
    device_object = Device(**device.dict(), owner_id=owner_id)
    db.add(device_object)
    db.commit()
    db.refresh(device_object)
    return device_object


def retrieve_device(id:int, db:Session):
    item = db.query(Device).filter(Device.id == id).first()
    return item


def list_devices(db : Session):
    devices = db.query(Device).all()
    return devices


