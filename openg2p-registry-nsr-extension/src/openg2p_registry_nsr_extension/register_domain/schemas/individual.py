from typing import Optional, List, Dict
from datetime import date, datetime
import uuid
from openg2p_registry_core.schemas import (
    G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema,
    G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema
)
from pydantic import BaseModel
from ..models.enums import ( RecordStatusEnum, RelationshipToHeadEnum, ResidencyStatusEnum,
    PreferredContactMethodEnum, AgeMethodEnum, CitizenshipCategoryEnum, IdentityEvidenceTypeEnum,
    DisabilityStatusEnum, DisabilitySeverityEnum, DisplacementStatusEnum, PastoralistClassificationEnum,
    EmploymentStatusEnum, PaymentChannelPreferenceEnum, PaymentVerificationStatusEnum,
    ConsentMethodEnum, GrievanceTypeEnum, SubmissionChannelEnum, GrievanceStatusEnum, ResolutionCodeEnum
)


class G2PRegisterIndividualProgramSchema(BaseModel):
    program_id: Optional[uuid.UUID] = None
    internal_record_id: uuid.UUID
    program_name: Optional[str] = None
    program_start_date: Optional[date] = None
    program_exit_date: Optional[date] = None

    class Config:
        from_attributes = True


class G2PRegisterIndividualGrievanceSchema(BaseModel):
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


class G2PRegisterSchemaIndividual(G2PRegisterBaseSchema, G2PPersonSchema, G2PGeoSchema):
    full_name: Optional[str] = None
    legacy_program_ids: Optional[Dict] = None
    record_status: Optional[RecordStatusEnum] = None
    record_status_reason: Optional[str] = None

    relationship_to_head: Optional[RelationshipToHeadEnum] = None
    dependency_indicator: Optional[bool] = None
    residency_status: Optional[ResidencyStatusEnum] = None

    region_id: Optional[uuid.UUID] = None
    zone_id: Optional[uuid.UUID] = None
    woreda_id: Optional[uuid.UUID] = None
    ea_id: Optional[uuid.UUID] = None
    
    locality_ea_code: Optional[str] = None
    gps_accuracy: Optional[float] = None
    address_descriptor: Optional[str] = None
    primary_phone: Optional[str] = None
    alternate_phone: Optional[str] = None
    preferred_contact_method: Optional[PreferredContactMethodEnum] = None
    contact_person_name: Optional[str] = None

    alias_names: Optional[List[str]] = None
    estimated_age: Optional[int] = None
    age_method: Optional[AgeMethodEnum] = None
    citizenship_category: Optional[CitizenshipCategoryEnum] = None
    identity_evidence_type: Optional[IdentityEvidenceTypeEnum] = None

    disability_status: Optional[DisabilityStatusEnum] = None
    disability_domains: Optional[Dict] = None
    disability_severity: Optional[DisabilitySeverityEnum] = None
    plw_status: Optional[bool] = None
    orphanhood_flag: Optional[bool] = None
    chronic_illness_flag: Optional[bool] = None
    displacement_status: Optional[DisplacementStatusEnum] = None
    pastoralist_classification: Optional[PastoralistClassificationEnum] = None
    high_mobility_indicator: Optional[bool] = None

    land_access: Optional[bool] = None
    land_size_band: Optional[str] = None
    livestock_counts: Optional[Dict] = None
    productive_assets: Optional[List[str]] = None
    mobile_phone_type: Optional[str] = None
    household_assets: Optional[Dict] = None

    primary_livelihood: Optional[str] = None
    secondary_livelihood: Optional[str] = None
    employment_status: Optional[EmploymentStatusEnum] = None
    shocks_last_12m: Optional[List[str]] = None
    shock_dates: Optional[List[date]] = None
    coping_strategies_index: Optional[int] = None

    pmt_score: Optional[float] = None
    pmt_variables: Optional[Dict] = None
    pmt_calculation_date: Optional[date] = None
    pmt_model_version: Optional[str] = None

    payment_channel_preference: Optional[PaymentChannelPreferenceEnum] = None
    payment_account_token: Optional[str] = None
    payment_verification_status: Optional[PaymentVerificationStatusEnum] = None

    consent_captured: Optional[bool] = None
    consent_date: Optional[date] = None
    consent_scope: Optional[List[str]] = None
    consent_method: Optional[ConsentMethodEnum] = None
    consent_evidence_ref: Optional[str] = None
    data_sharing_restrictions: Optional[Dict] = None


class G2PRegisterHistorySchemaIndividual(G2PRegisterHistorySchema, G2PPersonHistorySchema, G2PGeoHistorySchema):

    legacy_program_ids: Optional[Dict] = None
    record_status: Optional[RecordStatusEnum] = None
    record_status_reason: Optional[str] = None
    relationship_to_head: Optional[RelationshipToHeadEnum] = None
    dependency_indicator: Optional[bool] = None
    residency_status: Optional[ResidencyStatusEnum] = None
    region_id: Optional[uuid.UUID] = None
    zone_id: Optional[uuid.UUID] = None
    woreda_id: Optional[uuid.UUID] = None
    ea_id: Optional[uuid.UUID] = None
    locality_ea_code: Optional[str] = None
    gps_accuracy: Optional[float] = None
    address_descriptor: Optional[str] = None
    primary_phone: Optional[str] = None
    alternate_phone: Optional[str] = None
    preferred_contact_method: Optional[PreferredContactMethodEnum] = None
    contact_person_name: Optional[str] = None
    alias_names: Optional[List[str]] = None
    estimated_age: Optional[int] = None
    age_method: Optional[AgeMethodEnum] = None
    citizenship_category: Optional[CitizenshipCategoryEnum] = None
    identity_evidence_type: Optional[IdentityEvidenceTypeEnum] = None
    disability_status: Optional[DisabilityStatusEnum] = None
    disability_domains: Optional[Dict] = None
    disability_severity: Optional[DisabilitySeverityEnum] = None
    plw_status: Optional[bool] = None
    orphanhood_flag: Optional[bool] = None
    chronic_illness_flag: Optional[bool] = None
    displacement_status: Optional[DisplacementStatusEnum] = None
    pastoralist_classification: Optional[PastoralistClassificationEnum] = None
    high_mobility_indicator: Optional[bool] = None
    land_access: Optional[bool] = None
    land_size_band: Optional[str] = None
    livestock_counts: Optional[Dict] = None
    productive_assets: Optional[List[str]] = None
    mobile_phone_type: Optional[str] = None
    household_assets: Optional[Dict] = None
    primary_livelihood: Optional[str] = None
    secondary_livelihood: Optional[str] = None
    employment_status: Optional[EmploymentStatusEnum] = None
    shocks_last_12m: Optional[List[str]] = None
    shock_dates: Optional[List[date]] = None
    coping_strategies_index: Optional[int] = None
    pmt_score: Optional[float] = None
    pmt_variables: Optional[Dict] = None
    pmt_calculation_date: Optional[date] = None
    pmt_model_version: Optional[str] = None
    payment_channel_preference: Optional[PaymentChannelPreferenceEnum] = None
    payment_account_token: Optional[str] = None
    payment_verification_status: Optional[PaymentVerificationStatusEnum] = None
    consent_captured: Optional[bool] = None
    consent_date: Optional[date] = None
    consent_scope: Optional[List[str]] = None
    consent_method: Optional[ConsentMethodEnum] = None
    consent_evidence_ref: Optional[str] = None
    data_sharing_restrictions: Optional[Dict] = None
