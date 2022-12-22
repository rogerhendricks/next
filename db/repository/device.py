from sqlalchemy.orm import Session

from schemas.devices import DeviceCreate, ShowDevice
from db.models.devices import Device


def list_devices(db : Session):
    devices = db.query(Device).all()
    return devices


def create_new_device(device: DeviceCreate, db: Session):
    device_object = Device(**device.dict())
    db.add(device_object)
    db.commit()
    db.refresh(device_object)
    return device_object


def retrieve_device(id:int, db:Session):
    item = db.query(Device).filter(Device.id == id).first()
    return item


def delete_device_by_id(id: int, db: Session):
    existing_device = db.query(Device).filter(Device.id == id)
    if not existing_device.first():
        return 0
    existing_device.delete(synchronize_session=False)
    db.commit()
    return 1
