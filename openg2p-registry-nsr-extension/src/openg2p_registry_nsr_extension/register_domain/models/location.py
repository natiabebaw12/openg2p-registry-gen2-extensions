from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from openg2p_fastapi_common.models import BaseORMModel
import uuid


class G2PLocationRegion(BaseORMModel):
    __tablename__ = "g2p_location_regions"

    region_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    iso_code: Mapped[str] = mapped_column(String, nullable=True)

    zones: Mapped[list["G2PLocationZone"]] = relationship(back_populates="region", cascade="all, delete-orphan")


class G2PLocationZone(BaseORMModel):
    __tablename__ = "g2p_location_zones"

    zone_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    region_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_location_regions.region_id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    iso_code: Mapped[str] = mapped_column(String, nullable=True)

    region: Mapped["G2PLocationRegion"] = relationship(back_populates="zones")
    woredas: Mapped[list["G2PLocationWoreda"]] = relationship(back_populates="zone", cascade="all, delete-orphan")


class G2PLocationWoreda(BaseORMModel):
    __tablename__ = "g2p_location_woredas"

    woreda_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    zone_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_location_zones.zone_id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    iso_code: Mapped[str] = mapped_column(String, nullable=True)

    zone: Mapped["G2PLocationZone"] = relationship(back_populates="woredas")
    eas: Mapped[list["G2PLocationEA"]] = relationship(back_populates="woreda", cascade="all, delete-orphan")


class G2PLocationEA(BaseORMModel):
    __tablename__ = "g2p_location_eas"

    ea_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    woreda_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_location_woredas.woreda_id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    iso_code: Mapped[str] = mapped_column(String, nullable=True)

    woreda: Mapped["G2PLocationWoreda"] = relationship(back_populates="eas")
