from typing import Optional, List, Dict
from datetime import datetime, date
import uuid
from openg2p_registry_core.schemas import G2PRegisterBaseSchema, G2PRegisterHistorySchema
from pydantic import BaseModel
from ..models.enums import (
    RecordStatusEnum, HeadshipTypeEnum, DwellingTypeEnum, TenureStatusEnum,
    LightingSourceEnum, UpdateTriggerEnum, DataSourceEnum, VerificationStatusEnum,
    VerificationMethodEnum, GrievanceTypeEnum, SubmissionChannelEnum, GrievanceStatusEnum,
    ResolutionCodeEnum
)


class G2PRegisterHouseholdProgramSchema(BaseModel):
    program_id: Optional[uuid.UUID] = None
    internal_record_id: uuid.UUID
    program_name: Optional[str] = None
    program_start_date: Optional[date] = None
    program_exit_date: Optional[date] = None

    class Config:
        from_attributes = True


class G2PRegisterHouseholdGrievanceSchema(BaseModel):
    grievance_id: Optional[uuid.UUID] = None
    internal_record_id: uuid.UUID
    grievance_case_id: Optional[str] = None
    grievance_type: Optional[GrievanceTypeEnum] = None
    submission_channel: Optional[SubmissionChannelEnum] = None
    grievance_status: Optional[GrievanceStatusEnum] = None
    grievance_submission_date: Optional[date] = None
    grievance_resolution_date: Optional[date] = None
    resolution_code: Optional[ResolutionCodeEnum] = None
    resolution_rationale: Optional[str] = None
    protection_referral_flag: Optional[bool] = None

    class Config:
        from_attributes = True


class G2PRegisterSchemaHousehold(G2PRegisterBaseSchema):
    record_status: Optional[RecordStatusEnum] = None
    record_status_reason: Optional[str] = None

    household_size_total: Optional[int] = None
    household_size_adults: Optional[int] = None
    household_size_children_u5: Optional[int] = None
    household_size_school_age: Optional[int] = None
    household_size_elderly: Optional[int] = None
    household_head_person_id: Optional[str] = None
    headship_type: Optional[HeadshipTypeEnum] = None

    dwelling_type: Optional[DwellingTypeEnum] = None
    roof_material: Optional[str] = None
    wall_material: Optional[str] = None
    floor_material: Optional[str] = None
    tenure_status: Optional[TenureStatusEnum] = None
    water_source_type: Optional[str] = None
    water_distance_minutes: Optional[int] = None
    sanitation_type: Optional[str] = None
    lighting_source: Optional[LightingSourceEnum] = None
    cooking_fuel_type: Optional[str] = None
    rooms_count: Optional[int] = None
    overcrowding_indicator: Optional[float] = None

    elderly_member_present: Optional[bool] = None

    last_update_date: Optional[datetime] = None
    update_trigger: Optional[UpdateTriggerEnum] = None
    data_source: Optional[DataSourceEnum] = None
    enumerator_id: Optional[str] = None
    office_location_code: Optional[str] = None
    verification_status: Optional[VerificationStatusEnum] = None
    verification_method: Optional[VerificationMethodEnum] = None
    data_quality_flags: Optional[List[str]] = None


class G2PRegisterHistorySchemaHousehold(G2PRegisterHistorySchema):
    record_status: Optional[RecordStatusEnum] = None
    record_status_reason: Optional[str] = None
    household_size_total: Optional[int] = None
    household_size_adults: Optional[int] = None
    household_size_children_u5: Optional[int] = None
    household_size_school_age: Optional[int] = None
    household_size_elderly: Optional[int] = None
    household_head_person_id: Optional[str] = None
    headship_type: Optional[HeadshipTypeEnum] = None
    dwelling_type: Optional[DwellingTypeEnum] = None
    roof_material: Optional[str] = None
    wall_material: Optional[str] = None
    floor_material: Optional[str] = None
    tenure_status: Optional[TenureStatusEnum] = None
    water_source_type: Optional[str] = None
    water_distance_minutes: Optional[int] = None
    sanitation_type: Optional[str] = None
    lighting_source: Optional[LightingSourceEnum] = None
    cooking_fuel_type: Optional[str] = None
    rooms_count: Optional[int] = None
    overcrowding_indicator: Optional[float] = None
    elderly_member_present: Optional[bool] = None
    last_update_date: Optional[datetime] = None
    update_trigger: Optional[UpdateTriggerEnum] = None
    data_source: Optional[DataSourceEnum] = None
    enumerator_id: Optional[str] = None
    office_location_code: Optional[str] = None
    verification_status: Optional[VerificationStatusEnum] = None
    verification_method: Optional[VerificationMethodEnum] = None
    data_quality_flags: Optional[List[str]] = None
