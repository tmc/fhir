# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Base64Binary:
    value: bytes
    id: String
    extension: Extension


@dataclass
class Boolean:
    value: bool
    id: String
    extension: Extension


@dataclass
class Code:
    value: str
    id: String
    extension: Extension


@dataclass
class Date:
    value_us: int64
    timezone: str
    precision: Date_Precision
    id: String
    extension: Extension


@dataclass
class DateTime:
    value_us: int64
    timezone: str
    precision: DateTime_Precision
    id: String
    extension: Extension


@dataclass
class Decimal:
    value: str
    id: String
    extension: Extension


@dataclass
class Id:
    value: str
    id: String
    extension: Extension


@dataclass
class Instant:
    value_us: int64
    timezone: str
    precision: Instant_Precision
    id: String
    extension: Extension


@dataclass
class Integer:
    value: sint32
    id: String
    extension: Extension


@dataclass
class Markdown:
    value: str
    id: String
    extension: Extension


@dataclass
class Oid:
    value: str
    id: String
    extension: Extension


@dataclass
class PositiveInt:
    value: uint32
    id: String
    extension: Extension


@dataclass
class String:
    value: str
    id: String
    extension: Extension


@dataclass
class Time:
    value_us: int64
    precision: Time_Precision
    id: String
    extension: Extension


@dataclass
class UnsignedInt:
    value: uint32
    id: String
    extension: Extension


@dataclass
class Uri:
    value: str
    id: String
    extension: Extension


@dataclass
class Uuid:
    value: str
    id: String
    extension: Extension


@dataclass
class Xhtml:
    value: str
    id: String


@dataclass
class Address:
    id: String
    extension: Extension
    use: AddressUseCode
    type: AddressTypeCode
    text: String
    line: String
    city: String
    district: String
    state: String
    postal_code: String
    country: String
    period: Period


@dataclass
class Age:
    id: String
    extension: Extension
    value: Decimal
    comparator: QuantityComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Annotation:
    id: String
    extension: Extension
    author: Annotation_Author
    time: DateTime
    text: String


@dataclass
class Annotation_Author:
    reference: Reference
    string_value: String


@dataclass
class Attachment:
    id: String
    extension: Extension
    content_type: MimeTypeCode
    language: LanguageCode
    data: Base64Binary
    url: Uri
    size: UnsignedInt
    hash: Base64Binary
    title: String
    creation: DateTime


@dataclass
class CodeableConcept:
    id: String
    extension: Extension
    coding: Coding
    text: String


@dataclass
class Coding:
    id: String
    extension: Extension
    system: Uri
    version: String
    code: Code
    display: String
    user_selected: Boolean


@dataclass
class ContactPoint:
    id: String
    extension: Extension
    system: ContactPointSystemCode
    value: String
    use: ContactPointUseCode
    rank: PositiveInt
    period: Period


@dataclass
class Count:
    id: String
    extension: Extension
    value: Decimal
    comparator: QuantityComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Distance:
    id: String
    extension: Extension
    value: Decimal
    comparator: QuantityComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Dosage:
    id: String
    extension: Extension
    sequence: Integer
    text: String
    additional_instruction: CodeableConcept
    patient_instruction: String
    timing: Timing
    as_needed: Dosage_AsNeeded
    site: CodeableConcept
    route: CodeableConcept
    method: CodeableConcept
    dose: Dosage_Dose
    max_dose_per_period: Ratio
    max_dose_per_administration: SimpleQuantity
    max_dose_per_lifetime: SimpleQuantity
    rate: Dosage_Rate


@dataclass
class Dosage_AsNeeded:
    boolean: Boolean
    codeable_concept: CodeableConcept


@dataclass
class Dosage_Dose:
    range: Range
    quantity: SimpleQuantity


@dataclass
class Dosage_Rate:
    ratio: Ratio
    range: Range
    quantity: SimpleQuantity


@dataclass
class Duration:
    id: String
    extension: Extension
    value: Decimal
    comparator: QuantityComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class HumanName:
    id: String
    extension: Extension
    use: NameUseCode
    text: String
    family: String
    given: String
    prefix: String
    suffix: String
    period: Period


@dataclass
class Identifier:
    id: String
    extension: Extension
    use: IdentifierUseCode
    type: CodeableConcept
    system: Uri
    value: String
    period: Period
    assigner: Reference


@dataclass
class Meta:
    id: String
    extension: Extension
    version_id: Id
    last_updated: Instant
    profile: Uri
    security: Coding
    tag: Coding


@dataclass
class Money:
    id: String
    extension: Extension
    value: Decimal
    comparator: QuantityComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Period:
    id: String
    extension: Extension
    start: DateTime
    end: DateTime


@dataclass
class Quantity:
    id: String
    extension: Extension
    value: Decimal
    comparator: QuantityComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Range:
    id: String
    extension: Extension
    low: SimpleQuantity
    high: SimpleQuantity


@dataclass
class Ratio:
    id: String
    extension: Extension
    numerator: Quantity
    denominator: Quantity


@dataclass
class SampledData:
    id: String
    extension: Extension
    origin: SimpleQuantity
    period: Decimal
    factor: Decimal
    lower_limit: Decimal
    upper_limit: Decimal
    dimensions: PositiveInt
    data: String


@dataclass
class Signature:
    id: String
    extension: Extension
    type: Coding
    when: Instant
    who: Signature_Who
    on_behalf_of: Signature_OnBehalfOf
    content_type: MimeTypeCode
    blob: Base64Binary


@dataclass
class Signature_Who:
    uri: Uri
    reference: Reference


@dataclass
class Signature_OnBehalfOf:
    uri: Uri
    reference: Reference


@dataclass
class SimpleQuantity:
    id: String
    extension: Extension
    value: Decimal
    unit: String
    system: Uri
    code: Code


@dataclass
class Timing:
    id: String
    extension: Extension
    event: DateTime
    repeat: Timing_Repeat
    code: CodeableConcept


@dataclass
class Timing_Repeat:
    id: String
    extension: Extension
    bounds: Timing_Repeat_Bounds
    count: Integer
    count_max: Integer
    duration: Decimal
    duration_max: Decimal
    duration_unit: UnitsOfTimeCode
    frequency: Integer
    frequency_max: Integer
    period: Decimal
    period_max: Decimal
    period_unit: UnitsOfTimeCode
    day_of_week: DaysOfWeekCode
    time_of_day: Time
    when: EventTimingCode
    offset: UnsignedInt


@dataclass
class Timing_Repeat_Bounds:
    duration: Duration
    range: Range
    period: Period


@dataclass
class Extension:
    id: String
    url: Uri
    value: Extension_ValueX
    extension: Extension


@dataclass
class Extension_ValueX:
    base64_binary: Base64Binary
    boolean: Boolean
    code: Code
    date: Date
    date_time: DateTime
    decimal: Decimal
    id: Id
    instant: Instant
    integer: Integer
    markdown: Markdown
    oid: Oid
    positive_int: PositiveInt
    string_value: String
    time: Time
    unsigned_int: UnsignedInt
    uri: Uri
    address: Address
    age: Age
    annotation: Annotation
    attachment: Attachment
    codeable_concept: CodeableConcept
    coding: Coding
    contact_point: ContactPoint
    count: Count
    distance: Distance
    duration: Duration
    human_name: HumanName
    identifier: Identifier
    money: Money
    period: Period
    quantity: Quantity
    range: Range
    ratio: Ratio
    reference: Reference
    sampled_data: SampledData
    signature: Signature
    timing: Timing
    meta: Meta


@dataclass
class CodingWithFixedSystem:
    id: String
    extension: Extension
    version: String
    code: Code
    display: String
    user_selected: Boolean


@dataclass
class CodingWithFixedCode:
    id: String
    extension: Extension
    version: String
    display: String
    user_selected: Boolean


@dataclass
class Reference:
    id: String
    extension: Extension
    uri: String
    fragment: String
    account_id: ReferenceId
    activity_definition_id: ReferenceId
    adverse_event_id: ReferenceId
    allergy_intolerance_id: ReferenceId
    appointment_id: ReferenceId
    appointment_response_id: ReferenceId
    audit_event_id: ReferenceId
    basic_id: ReferenceId
    binary_id: ReferenceId
    body_site_id: ReferenceId
    bundle_id: ReferenceId
    capability_statement_id: ReferenceId
    care_plan_id: ReferenceId
    care_team_id: ReferenceId
    charge_item_id: ReferenceId
    claim_id: ReferenceId
    claim_response_id: ReferenceId
    clinical_impression_id: ReferenceId
    code_system_id: ReferenceId
    communication_id: ReferenceId
    communication_request_id: ReferenceId
    compartment_definition_id: ReferenceId
    composition_id: ReferenceId
    concept_map_id: ReferenceId
    condition_id: ReferenceId
    consent_id: ReferenceId
    contract_id: ReferenceId
    coverage_id: ReferenceId
    data_element_id: ReferenceId
    detected_issue_id: ReferenceId
    device_id: ReferenceId
    device_component_id: ReferenceId
    device_metric_id: ReferenceId
    device_request_id: ReferenceId
    device_use_statement_id: ReferenceId
    diagnostic_report_id: ReferenceId
    document_manifest_id: ReferenceId
    document_reference_id: ReferenceId
    eligibility_request_id: ReferenceId
    eligibility_response_id: ReferenceId
    encounter_id: ReferenceId
    endpoint_id: ReferenceId
    enrollment_request_id: ReferenceId
    enrollment_response_id: ReferenceId
    episode_of_care_id: ReferenceId
    expansion_profile_id: ReferenceId
    explanation_of_benefit_id: ReferenceId
    family_member_history_id: ReferenceId
    flag_id: ReferenceId
    goal_id: ReferenceId
    graph_definition_id: ReferenceId
    group_id: ReferenceId
    guidance_response_id: ReferenceId
    healthcare_service_id: ReferenceId
    imaging_manifest_id: ReferenceId
    imaging_study_id: ReferenceId
    immunization_id: ReferenceId
    immunization_recommendation_id: ReferenceId
    implementation_guide_id: ReferenceId
    library_id: ReferenceId
    linkage_id: ReferenceId
    list_id: ReferenceId
    location_id: ReferenceId
    measure_id: ReferenceId
    measure_report_id: ReferenceId
    media_id: ReferenceId
    medication_id: ReferenceId
    medication_administration_id: ReferenceId
    medication_dispense_id: ReferenceId
    medication_request_id: ReferenceId
    medication_statement_id: ReferenceId
    message_definition_id: ReferenceId
    message_header_id: ReferenceId
    naming_system_id: ReferenceId
    nutrition_order_id: ReferenceId
    observation_id: ReferenceId
    operation_definition_id: ReferenceId
    operation_outcome_id: ReferenceId
    organization_id: ReferenceId
    parameters_id: ReferenceId
    patient_id: ReferenceId
    payment_notice_id: ReferenceId
    payment_reconciliation_id: ReferenceId
    person_id: ReferenceId
    plan_definition_id: ReferenceId
    practitioner_id: ReferenceId
    practitioner_role_id: ReferenceId
    procedure_id: ReferenceId
    procedure_request_id: ReferenceId
    process_request_id: ReferenceId
    process_response_id: ReferenceId
    provenance_id: ReferenceId
    questionnaire_id: ReferenceId
    questionnaire_response_id: ReferenceId
    referral_request_id: ReferenceId
    related_person_id: ReferenceId
    request_group_id: ReferenceId
    research_study_id: ReferenceId
    research_subject_id: ReferenceId
    risk_assessment_id: ReferenceId
    schedule_id: ReferenceId
    search_parameter_id: ReferenceId
    sequence_id: ReferenceId
    service_definition_id: ReferenceId
    slot_id: ReferenceId
    specimen_id: ReferenceId
    structure_definition_id: ReferenceId
    structure_map_id: ReferenceId
    subscription_id: ReferenceId
    substance_id: ReferenceId
    supply_delivery_id: ReferenceId
    supply_request_id: ReferenceId
    task_id: ReferenceId
    test_report_id: ReferenceId
    test_script_id: ReferenceId
    value_set_id: ReferenceId
    vision_prescription_id: ReferenceId
    identifier: Identifier
    display: String


@dataclass
class ReferenceId:
    value: str
    history: Id
    id: String
    extension: Extension


@dataclass
class AddressTypeCode:
    value: AddressTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AddressUseCode:
    value: AddressUseCode_Value
    id: String
    extension: Extension


@dataclass
class ContactPointSystemCode:
    value: ContactPointSystemCode_Value
    id: String
    extension: Extension


@dataclass
class ContactPointUseCode:
    value: ContactPointUseCode_Value
    id: String
    extension: Extension


@dataclass
class DaysOfWeekCode:
    value: DaysOfWeekCode_Value
    id: String
    extension: Extension


@dataclass
class EventTimingCode:
    value: EventTimingCode_Value
    id: String
    extension: Extension


@dataclass
class IdentifierUseCode:
    value: IdentifierUseCode_Value
    id: String
    extension: Extension


@dataclass
class AllLanguageCode:
    value: str
    id: String
    extension: Extension


@dataclass
class LanguageCode:
    value: str
    id: String
    extension: Extension


@dataclass
class MimeTypeCode:
    value: str
    id: String
    extension: Extension


@dataclass
class NameUseCode:
    value: NameUseCode_Value
    id: String
    extension: Extension


@dataclass
class QuantityComparatorCode:
    value: QuantityComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class UnitsOfTimeCode:
    value: UnitsOfTimeCode_Value
    id: String
    extension: Extension

