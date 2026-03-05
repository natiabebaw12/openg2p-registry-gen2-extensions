from sqlalchemy import String, Integer, Boolean, Numeric, DateTime, JSON, Date, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from openg2p_registry_core.models import G2PRegister, G2PRegisterHistory
from openg2p_fastapi_common.models import BaseORMModel
import uuid
from datetime import datetime, date
from .enums import (
    RecordStatusEnum, HeadshipTypeEnum, DwellingTypeEnum, TenureStatusEnum,
    LightingSourceEnum, UpdateTriggerEnum, DataSourceEnum, VerificationStatusEnum,
    VerificationMethodEnum, GrievanceTypeEnum, SubmissionChannelEnum, GrievanceStatusEnum,
    ResolutionCodeEnum
)


# All Register classes should have the prefix G2PRegister
class G2PRegisterHousehold(G2PRegister):
    __tablename__ = "g2p_register_households"

    # Registry Keys and Identifiers
    record_status: Mapped[RecordStatusEnum] = mapped_column(Enum(RecordStatusEnum), nullable=True)
    record_status_reason: Mapped[str] = mapped_column(String, nullable=True)

    # Household Roster and Relationships
    household_size_total: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_adults: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_children_u5: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_school_age: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_elderly: Mapped[int] = mapped_column(Integer, nullable=True)
    household_head_person_id: Mapped[str] = mapped_column(String, nullable=True)
    headship_type: Mapped[HeadshipTypeEnum] = mapped_column(Enum(HeadshipTypeEnum), nullable=True)

    # Housing and Services
    dwelling_type: Mapped[DwellingTypeEnum] = mapped_column(Enum(DwellingTypeEnum), nullable=True)
    roof_material: Mapped[str] = mapped_column(String, nullable=True)
    wall_material: Mapped[str] = mapped_column(String, nullable=True)
    floor_material: Mapped[str] = mapped_column(String, nullable=True)
    tenure_status: Mapped[TenureStatusEnum] = mapped_column(Enum(TenureStatusEnum), nullable=True)
    water_source_type: Mapped[str] = mapped_column(String, nullable=True)
    water_distance_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    sanitation_type: Mapped[str] = mapped_column(String, nullable=True)
    lighting_source: Mapped[LightingSourceEnum] = mapped_column(Enum(LightingSourceEnum), nullable=True)
    cooking_fuel_type: Mapped[str] = mapped_column(String, nullable=True)
    rooms_count: Mapped[int] = mapped_column(Integer, nullable=True)
    overcrowding_indicator: Mapped[float] = mapped_column(Numeric, nullable=True)

    # Vulnerability and Inclusion Markers
    elderly_member_present: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # Update History and Audit Trail
    last_update_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    update_trigger: Mapped[UpdateTriggerEnum] = mapped_column(Enum(UpdateTriggerEnum), nullable=True)
    data_source: Mapped[DataSourceEnum] = mapped_column(Enum(DataSourceEnum), nullable=True)
    enumerator_id: Mapped[str] = mapped_column(String, nullable=True)
    office_location_code: Mapped[str] = mapped_column(String, nullable=True)
    verification_status: Mapped[VerificationStatusEnum] = mapped_column(Enum(VerificationStatusEnum), nullable=True)
    verification_method: Mapped[VerificationMethodEnum] = mapped_column(Enum(VerificationMethodEnum), nullable=True)
    data_quality_flags: Mapped[list] = mapped_column(JSON, nullable=True)

    # Relationships
    programs: Mapped[list["G2PRegisterHouseholdProgram"]] = relationship(cascade="all, delete-orphan")
    grievances: Mapped[list["G2PRegisterHouseholdGrievance"]] = relationship(cascade="all, delete-orphan")

    def get_search_text_fields(self) -> list[str]:
        return [
            str(self.headship_type) or "",
            str(self.dwelling_type) or "",
            str(self.tenure_status) or "",
            self.water_source_type or "",
            self.sanitation_type or "",
            str(self.lighting_source) or "",
            self.cooking_fuel_type or "",
            str(self.data_source) or "",
            str(self.verification_status) or "",
        ]


class G2PRegisterHouseholdProgram(BaseORMModel):
    __tablename__ = "g2p_register_household_programs"

    program_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    internal_record_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_register_households.internal_record_id"), index=True, nullable=False)
    program_name: Mapped[str] = mapped_column(String, nullable=True)
    program_start_date: Mapped[date] = mapped_column(Date, nullable=True)
    program_exit_date: Mapped[date] = mapped_column(Date, nullable=True)


class G2PRegisterHouseholdGrievance(BaseORMModel):
    __tablename__ = "g2p_register_household_grievances"

    grievance_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    internal_record_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_register_households.internal_record_id"), index=True, nullable=False)
    grievance_case_id: Mapped[str] = mapped_column(String, nullable=True)
    grievance_type: Mapped[GrievanceTypeEnum] = mapped_column(Enum(GrievanceTypeEnum), nullable=True)
    submission_channel: Mapped[SubmissionChannelEnum] = mapped_column(Enum(SubmissionChannelEnum), nullable=True)
    grievance_status: Mapped[GrievanceStatusEnum] = mapped_column(Enum(GrievanceStatusEnum), nullable=True)
    grievance_submission_date: Mapped[date] = mapped_column(Date, nullable=True)
    grievance_resolution_date: Mapped[date] = mapped_column(Date, nullable=True)
    resolution_code: Mapped[ResolutionCodeEnum] = mapped_column(Enum(ResolutionCodeEnum), nullable=True)
    resolution_rationale: Mapped[str] = mapped_column(String, nullable=True)
    protection_referral_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)


# All Register History classes should have the prefix G2PRegisterHistory
class G2PRegisterHistoryHousehold(G2PRegisterHistory):
    __tablename__ = "g2p_register_history_households"

    record_status: Mapped[RecordStatusEnum] = mapped_column(Enum(RecordStatusEnum), nullable=True)
    record_status_reason: Mapped[str] = mapped_column(String, nullable=True)

    household_size_total: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_adults: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_children_u5: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_school_age: Mapped[int] = mapped_column(Integer, nullable=True)
    household_size_elderly: Mapped[int] = mapped_column(Integer, nullable=True)
    household_head_person_id: Mapped[str] = mapped_column(String, nullable=True)
    headship_type: Mapped[HeadshipTypeEnum] = mapped_column(Enum(HeadshipTypeEnum), nullable=True)
    dwelling_type: Mapped[DwellingTypeEnum] = mapped_column(Enum(DwellingTypeEnum), nullable=True)
    roof_material: Mapped[str] = mapped_column(String, nullable=True)
    wall_material: Mapped[str] = mapped_column(String, nullable=True)
    floor_material: Mapped[str] = mapped_column(String, nullable=True)
    tenure_status: Mapped[TenureStatusEnum] = mapped_column(Enum(TenureStatusEnum), nullable=True)
    water_source_type: Mapped[str] = mapped_column(String, nullable=True)
    water_distance_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    sanitation_type: Mapped[str] = mapped_column(String, nullable=True)
    lighting_source: Mapped[LightingSourceEnum] = mapped_column(Enum(LightingSourceEnum), nullable=True)
    cooking_fuel_type: Mapped[str] = mapped_column(String, nullable=True)
    rooms_count: Mapped[int] = mapped_column(Integer, nullable=True)
    overcrowding_indicator: Mapped[float] = mapped_column(Numeric, nullable=True)
    elderly_member_present: Mapped[bool] = mapped_column(Boolean, nullable=True)
    last_update_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    update_trigger: Mapped[UpdateTriggerEnum] = mapped_column(Enum(UpdateTriggerEnum), nullable=True)
    data_source: Mapped[DataSourceEnum] = mapped_column(Enum(DataSourceEnum), nullable=True)
    enumerator_id: Mapped[str] = mapped_column(String, nullable=True)
    office_location_code: Mapped[str] = mapped_column(String, nullable=True)
    verification_status: Mapped[VerificationStatusEnum] = mapped_column(Enum(VerificationStatusEnum), nullable=True)
    verification_method: Mapped[VerificationMethodEnum] = mapped_column(Enum(VerificationMethodEnum), nullable=True)
    data_quality_flags: Mapped[list] = mapped_column(JSON, nullable=True)


class G2PRegisterHistoryHouseholdProgram(BaseORMModel):
    __tablename__ = "g2p_register_history_household_programs"

    program_history_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    program_id: Mapped[uuid.UUID] = mapped_column(index=True, nullable=False)
    internal_record_id: Mapped[uuid.UUID] = mapped_column(index=True, nullable=False)
    program_name: Mapped[str] = mapped_column(String, nullable=True)
    program_start_date: Mapped[date] = mapped_column(Date, nullable=True)
    program_exit_date: Mapped[date] = mapped_column(Date, nullable=True)


class G2PRegisterHistoryHouseholdGrievance(BaseORMModel):
    __tablename__ = "g2p_register_history_household_grievances"

    grievance_history_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    grievance_id: Mapped[uuid.UUID] = mapped_column(index=True, nullable=False)
    internal_record_id: Mapped[uuid.UUID] = mapped_column(index=True, nullable=False)
    grievance_case_id: Mapped[str] = mapped_column(String, nullable=True)
    grievance_type: Mapped[GrievanceTypeEnum] = mapped_column(Enum(GrievanceTypeEnum), nullable=True)
    submission_channel: Mapped[SubmissionChannelEnum] = mapped_column(Enum(SubmissionChannelEnum), nullable=True)
    grievance_status: Mapped[GrievanceStatusEnum] = mapped_column(Enum(GrievanceStatusEnum), nullable=True)
    grievance_submission_date: Mapped[date] = mapped_column(Date, nullable=True)
    grievance_resolution_date: Mapped[date] = mapped_column(Date, nullable=True)
    resolution_code: Mapped[ResolutionCodeEnum] = mapped_column(Enum(ResolutionCodeEnum), nullable=True)
    resolution_rationale: Mapped[str] = mapped_column(String, nullable=True)
    protection_referral_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
