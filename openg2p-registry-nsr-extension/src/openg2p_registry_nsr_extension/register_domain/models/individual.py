from sqlalchemy import String, Integer, Boolean, Numeric, Date, JSON, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from openg2p_registry_core.models import (
    G2PRegister, G2PRegisterHistory, G2PPerson, G2PGeo,
    G2PPersonHistory, G2PGeoHistory
)
from openg2p_fastapi_common.models import BaseORMModel
from datetime import date, datetime
import uuid
from .enums import (
    RecordStatusEnum, RelationshipToHeadEnum, ResidencyStatusEnum,
    PreferredContactMethodEnum, AgeMethodEnum, CitizenshipCategoryEnum, IdentityEvidenceTypeEnum,
    DisabilityStatusEnum, DisabilitySeverityEnum, DisplacementStatusEnum, PastoralistClassificationEnum,
    EmploymentStatusEnum, PaymentChannelPreferenceEnum, PaymentVerificationStatusEnum,
    ConsentMethodEnum, GrievanceTypeEnum, SubmissionChannelEnum, GrievanceStatusEnum, ResolutionCodeEnum
)


# All Register classes should have the prefix G2PRegister
class G2PRegisterIndividual(G2PRegister, G2PPerson, G2PGeo):
    __tablename__ = "g2p_register_individuals"

    # Registry Keys and Identifiers
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    legacy_program_ids: Mapped[dict] = mapped_column(JSON, nullable=True)
    record_status: Mapped[RecordStatusEnum] = mapped_column(Enum(RecordStatusEnum), nullable=True)
    record_status_reason: Mapped[str] = mapped_column(String, nullable=True)

    # Household Roster and Relationships
    relationship_to_head: Mapped[RelationshipToHeadEnum] = mapped_column(Enum(RelationshipToHeadEnum), nullable=True)
    dependency_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)
    residency_status: Mapped[ResidencyStatusEnum] = mapped_column(Enum(ResidencyStatusEnum), nullable=True)

    # Location and Contact Information (Linking to Location Tables)
    region_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_location_regions.region_id"), nullable=True)
    zone_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_location_zones.zone_id"), nullable=True)
    woreda_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_location_woredas.woreda_id"), nullable=True)
    ea_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_location_eas.ea_id"), nullable=True)
    
    locality_ea_code: Mapped[str] = mapped_column(String, nullable=True)
    gps_accuracy: Mapped[float] = mapped_column(Numeric, nullable=True)
    address_descriptor: Mapped[str] = mapped_column(String, nullable=True)
    primary_phone: Mapped[str] = mapped_column(String, nullable=True)
    alternate_phone: Mapped[str] = mapped_column(String, nullable=True)
    preferred_contact_method: Mapped[PreferredContactMethodEnum] = mapped_column(Enum(PreferredContactMethodEnum), nullable=True)
    contact_person_name: Mapped[str] = mapped_column(String, nullable=True)

    # Demographics
    alias_names: Mapped[list] = mapped_column(JSON, nullable=True)
    estimated_age: Mapped[int] = mapped_column(Integer, nullable=True)
    age_method: Mapped[AgeMethodEnum] = mapped_column(Enum(AgeMethodEnum), nullable=True)
    citizenship_category: Mapped[CitizenshipCategoryEnum] = mapped_column(Enum(CitizenshipCategoryEnum), nullable=True)
    identity_evidence_type: Mapped[IdentityEvidenceTypeEnum] = mapped_column(Enum(IdentityEvidenceTypeEnum), nullable=True)

    # Vulnerability and Inclusion Markers
    disability_status: Mapped[DisabilityStatusEnum] = mapped_column(Enum(DisabilityStatusEnum), nullable=True)
    disability_domains: Mapped[dict] = mapped_column(JSON, nullable=True)
    disability_severity: Mapped[DisabilitySeverityEnum] = mapped_column(Enum(DisabilitySeverityEnum), nullable=True)
    plw_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
    orphanhood_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    chronic_illness_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    displacement_status: Mapped[DisplacementStatusEnum] = mapped_column(Enum(DisplacementStatusEnum), nullable=True)
    pastoralist_classification: Mapped[PastoralistClassificationEnum] = mapped_column(Enum(PastoralistClassificationEnum), nullable=True)
    high_mobility_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # Assets
    land_access: Mapped[bool] = mapped_column(Boolean, nullable=True)
    land_size_band: Mapped[str] = mapped_column(String, nullable=True)
    livestock_counts: Mapped[dict] = mapped_column(JSON, nullable=True)
    productive_assets: Mapped[list] = mapped_column(JSON, nullable=True)
    mobile_phone_type: Mapped[str] = mapped_column(String, nullable=True)
    household_assets: Mapped[dict] = mapped_column(JSON, nullable=True)

    # Livelihoods and Income Proxies
    primary_livelihood: Mapped[str] = mapped_column(String, nullable=True)
    secondary_livelihood: Mapped[str] = mapped_column(String, nullable=True)
    employment_status: Mapped[EmploymentStatusEnum] = mapped_column(Enum(EmploymentStatusEnum), nullable=True)
    shocks_last_12m: Mapped[list] = mapped_column(JSON, nullable=True)
    shock_dates: Mapped[list] = mapped_column(JSON, nullable=True)
    coping_strategies_index: Mapped[int] = mapped_column(Integer, nullable=True)

    # PMT Module Fields
    pmt_score: Mapped[float] = mapped_column(Numeric, nullable=True)
    pmt_variables: Mapped[dict] = mapped_column(JSON, nullable=True)
    pmt_calculation_date: Mapped[date] = mapped_column(Date, nullable=True)
    pmt_model_version: Mapped[str] = mapped_column(String, nullable=True)

    # Programme Participation and Delivery Linkage
    payment_channel_preference: Mapped[PaymentChannelPreferenceEnum] = mapped_column(Enum(PaymentChannelPreferenceEnum), nullable=True)
    payment_account_token: Mapped[str] = mapped_column(String, nullable=True)
    payment_verification_status: Mapped[PaymentVerificationStatusEnum] = mapped_column(Enum(PaymentVerificationStatusEnum), nullable=True)

    # Consent Management
    consent_captured: Mapped[bool] = mapped_column(Boolean, nullable=True)
    consent_date: Mapped[date] = mapped_column(Date, nullable=True)
    consent_scope: Mapped[list] = mapped_column(JSON, nullable=True)
    consent_method: Mapped[ConsentMethodEnum] = mapped_column(Enum(ConsentMethodEnum), nullable=True)
    consent_evidence_ref: Mapped[str] = mapped_column(String, nullable=True)
    data_sharing_restrictions: Mapped[dict] = mapped_column(JSON, nullable=True)

    # Relationships
    programs: Mapped[list["G2PRegisterIndividualProgram"]] = relationship(cascade="all, delete-orphan")
    grievances: Mapped[list["G2PRegisterIndividualGrievance"]] = relationship(cascade="all, delete-orphan")

    def get_search_text_fields(self) -> list[str]:
        return [
            self.full_name or "",
            self.primary_phone or "",
            str(self.relationship_to_head) or "",
            str(self.employment_status) or "",
            self.primary_livelihood or "",
        ]


class G2PRegisterIndividualProgram(BaseORMModel):
    __tablename__ = "g2p_register_individual_programs"

    program_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    internal_record_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_register_individuals.internal_record_id"), index=True, nullable=False)
    program_name: Mapped[str] = mapped_column(String, nullable=True)
    program_start_date: Mapped[date] = mapped_column(Date, nullable=True)
    program_exit_date: Mapped[date] = mapped_column(Date, nullable=True)


class G2PRegisterIndividualGrievance(BaseORMModel):
    __tablename__ = "g2p_register_individual_grievances"

    grievance_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    internal_record_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("g2p_register_individuals.internal_record_id"), index=True, nullable=False)
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
class G2PRegisterHistoryIndividual(G2PRegisterHistory, G2PPersonHistory, G2PGeoHistory):
    __tablename__ = "g2p_register_history_individuals"

    full_name: Mapped[str] = mapped_column(String, nullable=True)
    legacy_program_ids: Mapped[dict] = mapped_column(JSON, nullable=True)
    record_status: Mapped[RecordStatusEnum] = mapped_column(Enum(RecordStatusEnum), nullable=True)
    record_status_reason: Mapped[str] = mapped_column(String, nullable=True)

    relationship_to_head: Mapped[RelationshipToHeadEnum] = mapped_column(Enum(RelationshipToHeadEnum), nullable=True)
    dependency_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)
    residency_status: Mapped[ResidencyStatusEnum] = mapped_column(Enum(ResidencyStatusEnum), nullable=True)

    region_id: Mapped[uuid.UUID] = mapped_column(uuid.UUID, nullable=True)
    zone_id: Mapped[uuid.UUID] = mapped_column(uuid.UUID, nullable=True)
    woreda_id: Mapped[uuid.UUID] = mapped_column(uuid.UUID, nullable=True)
    ea_id: Mapped[uuid.UUID] = mapped_column(uuid.UUID, nullable=True)

    locality_ea_code: Mapped[str] = mapped_column(String, nullable=True)
    gps_accuracy: Mapped[float] = mapped_column(Numeric, nullable=True)
    address_descriptor: Mapped[str] = mapped_column(String, nullable=True)
    primary_phone: Mapped[str] = mapped_column(String, nullable=True)
    alternate_phone: Mapped[str] = mapped_column(String, nullable=True)
    preferred_contact_method: Mapped[PreferredContactMethodEnum] = mapped_column(Enum(PreferredContactMethodEnum), nullable=True)
    contact_person_name: Mapped[str] = mapped_column(String, nullable=True)
    alias_names: Mapped[list] = mapped_column(JSON, nullable=True)
    estimated_age: Mapped[int] = mapped_column(Integer, nullable=True)
    age_method: Mapped[AgeMethodEnum] = mapped_column(Enum(AgeMethodEnum), nullable=True)
    citizenship_category: Mapped[CitizenshipCategoryEnum] = mapped_column(Enum(CitizenshipCategoryEnum), nullable=True)
    identity_evidence_type: Mapped[IdentityEvidenceTypeEnum] = mapped_column(Enum(IdentityEvidenceTypeEnum), nullable=True)
    disability_status: Mapped[DisabilityStatusEnum] = mapped_column(Enum(DisabilityStatusEnum), nullable=True)
    disability_domains: Mapped[dict] = mapped_column(JSON, nullable=True)
    disability_severity: Mapped[DisabilitySeverityEnum] = mapped_column(Enum(DisabilitySeverityEnum), nullable=True)
    plw_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
    orphanhood_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    chronic_illness_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    displacement_status: Mapped[DisplacementStatusEnum] = mapped_column(Enum(DisplacementStatusEnum), nullable=True)
    pastoralist_classification: Mapped[PastoralistClassificationEnum] = mapped_column(Enum(PastoralistClassificationEnum), nullable=True)
    high_mobility_indicator: Mapped[bool] = mapped_column(Boolean, nullable=True)
    land_access: Mapped[bool] = mapped_column(Boolean, nullable=True)
    land_size_band: Mapped[str] = mapped_column(String, nullable=True)
    livestock_counts: Mapped[dict] = mapped_column(JSON, nullable=True)
    productive_assets: Mapped[list] = mapped_column(JSON, nullable=True)
    mobile_phone_type: Mapped[str] = mapped_column(String, nullable=True)
    household_assets: Mapped[dict] = mapped_column(JSON, nullable=True)
    primary_livelihood: Mapped[str] = mapped_column(String, nullable=True)
    secondary_livelihood: Mapped[str] = mapped_column(String, nullable=True)
    employment_status: Mapped[EmploymentStatusEnum] = mapped_column(Enum(EmploymentStatusEnum), nullable=True)
    shocks_last_12m: Mapped[list] = mapped_column(JSON, nullable=True)
    shock_dates: Mapped[list] = mapped_column(JSON, nullable=True)
    coping_strategies_index: Mapped[int] = mapped_column(Integer, nullable=True)
    pmt_score: Mapped[float] = mapped_column(Numeric, nullable=True)
    pmt_variables: Mapped[dict] = mapped_column(JSON, nullable=True)
    pmt_calculation_date: Mapped[date] = mapped_column(Date, nullable=True)
    pmt_model_version: Mapped[str] = mapped_column(String, nullable=True)
    payment_channel_preference: Mapped[PaymentChannelPreferenceEnum] = mapped_column(Enum(PaymentChannelPreferenceEnum), nullable=True)
    payment_account_token: Mapped[str] = mapped_column(String, nullable=True)
    payment_verification_status: Mapped[PaymentVerificationStatusEnum] = mapped_column(Enum(PaymentVerificationStatusEnum), nullable=True)
    consent_captured: Mapped[bool] = mapped_column(Boolean, nullable=True)
    consent_date: Mapped[date] = mapped_column(Date, nullable=True)
    consent_scope: Mapped[list] = mapped_column(JSON, nullable=True)
    consent_method: Mapped[ConsentMethodEnum] = mapped_column(Enum(ConsentMethodEnum), nullable=True)
    consent_evidence_ref: Mapped[str] = mapped_column(String, nullable=True)
    data_sharing_restrictions: Mapped[dict] = mapped_column(JSON, nullable=True)


class G2PRegisterHistoryIndividualProgram(BaseORMModel):
    __tablename__ = "g2p_register_history_individual_programs"

    program_history_id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    program_id: Mapped[uuid.UUID] = mapped_column(index=True, nullable=False)
    internal_record_id: Mapped[uuid.UUID] = mapped_column(index=True, nullable=False)
    program_name: Mapped[str] = mapped_column(String, nullable=True)
    program_start_date: Mapped[date] = mapped_column(Date, nullable=True)
    program_exit_date: Mapped[date] = mapped_column(Date, nullable=True)


class G2PRegisterHistoryIndividualGrievance(BaseORMModel):
    __tablename__ = "g2p_register_history_individual_grievances"

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
