from typing import Optional
import uuid
from pydantic import BaseModel


class G2PLocationRegionSchema(BaseModel):
    region_id: Optional[uuid.UUID] = None
    name: str
    iso_code: Optional[str] = None

    class Config:
        from_attributes = True


class G2PLocationZoneSchema(BaseModel):
    zone_id: Optional[uuid.UUID] = None
    region_id: uuid.UUID
    name: str
    iso_code: Optional[str] = None

    class Config:
        from_attributes = True


class G2PLocationWoredaSchema(BaseModel):
    woreda_id: Optional[uuid.UUID] = None
    zone_id: uuid.UUID
    name: str
    iso_code: Optional[str] = None

    class Config:
        from_attributes = True


class G2PLocationEASchema(BaseModel):
    ea_id: Optional[uuid.UUID] = None
    woreda_id: uuid.UUID
    name: str
    iso_code: Optional[str] = None

    class Config:
        from_attributes = True
