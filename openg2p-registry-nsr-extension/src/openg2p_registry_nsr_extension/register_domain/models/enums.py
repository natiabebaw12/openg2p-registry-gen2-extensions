from enum import Enum




class RecordStatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class HeadshipTypeEnum(str, Enum):
    FEMALE_HEADED = "female-headed"
    CHILD_HEADED = "child-headed"
    ELDERLY_HEADED = "elderly-headed"
    DISABLED_HEADED = "disabled-headed"
    MALE_HEADED = "male-headed"


class RelationshipToHeadEnum(str, Enum):
    SPOUSE = "spouse"
    CHILD = "child"
    PARENT = "parent"
    OTHER = "other"


class ResidencyStatusEnum(str, Enum):
    USUAL_MEMBER = "Usual member"
    TEMPORARY = "temporary"
    ABSENT = "absent"


class PreferredContactMethodEnum(str, Enum):
    CALL = "Call"
    SMS = "SMS"
    THROUGH_KEBELE = "through kebele"


class AgeMethodEnum(str, Enum):
    DOCUMENTED = "documented"
    ESTIMATED = "estimated"


class CitizenshipCategoryEnum(str, Enum):
    CITIZEN = "Citizen"
    REFUGEE = "refugee"
    IDP = "IDP"
    RETURNEE = "returnee"
    RESIDENT = "resident"


class IdentityEvidenceTypeEnum(str, Enum):
    FAYDA_VERIFIED = "Fayda verified"
    DOCUMENT_TYPE = "document type"
    NONE = "none"
    EXCEPTION = "exception"


class DisabilityStatusEnum(str, Enum):
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


class DisabilitySeverityEnum(str, Enum):
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"
    PROFOUND = "profound"


class DisplacementStatusEnum(str, Enum):
    IDP = "IDP"
    RETURNEE = "returnee"
    REFUGEE = "refugee"
    HOST_COMMUNITY = "host community"


class PastoralistClassificationEnum(str, Enum):
    PASTORALIST = "Pastoralist"
    SEMI_PASTORALIST = "semi-pastoralist"
    SETTLED = "settled"


class DwellingTypeEnum(str, Enum):
    PERMANENT = "permanent"
    SEMI = "semi"
    TEMPORARY = "temporary"


class TenureStatusEnum(str, Enum):
    OWNED = "Owned"
    RENTED = "rented"
    HOSTED = "hosted"
    TEMPORARY = "temporary"


class LightingSourceEnum(str, Enum):
    GRID = "grid"
    SOLAR = "solar"
    KEROSENE = "kerosene"
    NONE = "none"


class EmploymentStatusEnum(str, Enum):
    EMPLOYED = "Employed"
    SELF_EMPLOYED = "self-employed"
    UNEMPLOYED = "unemployed"
    STUDENT = "student"
    OTHER = "other"


class PaymentChannelPreferenceEnum(str, Enum):
    BANK = "Bank"
    MOBILE_MONEY = "mobile money"
    CASH = "cash"
    OTHER = "other"


class PaymentVerificationStatusEnum(str, Enum):
    ACCOUNT_VERIFIED = "Account verified"
    PENDING = "pending"
    FAILED = "failed"


class ConsentMethodEnum(str, Enum):
    SIGNED = "Signed"
    VERBAL = "verbal"
    DIGITAL = "digital"
    BIOMETRIC = "biometric"


class GrievanceTypeEnum(str, Enum):
    EXCLUSION = "Exclusion"
    INCLUSION = "inclusion"
    DATA_ERROR = "data error"
    PAYMENT = "payment"
    PROTECTION = "protection"


class SubmissionChannelEnum(str, Enum):
    IN_PERSON = "In-person"
    PHONE = "phone"
    USSD = "USSD"
    COMMUNITY_COMMITTEE = "community committee"


class GrievanceStatusEnum(str, Enum):
    OPEN = "Open"
    UNDER_REVIEW = "under review"
    RESOLVED = "resolved"
    APPEALED = "appealed"


class ResolutionCodeEnum(str, Enum):
    ADDED = "Added"
    CORRECTED = "corrected"
    REFERRED = "referred"
    REJECTED = "rejected"


class UpdateTriggerEnum(str, Enum):
    ON_DEMAND = "On-demand"
    ANNUAL_RECERTIFICATION = "annual recertification"
    LIFE_EVENT = "life event"
    SHOCK = "shock"


class DataSourceEnum(str, Enum):
    SELF_REPORT = "Self-report"
    KEBELE_VERIFICATION = "kebele verification"
    PROGRAMME_MIS = "programme MIS"
    FAYDA = "Fayda"


class VerificationStatusEnum(str, Enum):
    UNVERIFIED = "Unverified"
    VERIFIED = "verified"
    SPOT_CHECKED = "spot-checked"


class VerificationMethodEnum(str, Enum):
    PHONE_CALL = "Phone call"
    FIELD_VISIT = "field visit"
    DOCUMENT_CHECK = "document check"
    API = "API"
