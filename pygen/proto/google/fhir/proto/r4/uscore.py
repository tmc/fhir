# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.uscore
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class PatientUSCoreBirthSexExtension:
    id: String
    extension: Extension
    value_code: PatientUSCoreBirthSexExtension_ValueCode


@dataclass
class PatientUSCoreBirthSexExtension_ValueCode:
    value: BirthSexValueSet_Value
    id: String
    extension: Extension


@dataclass
class PatientUSCoreEthnicityExtension:
    id: String
    extension: Extension
    omb_category: PatientUSCoreEthnicityExtension_OmbCategoryCoding
    detailed: PatientUSCoreEthnicityExtension_DetailedCoding
    text: String


@dataclass
class PatientUSCoreEthnicityExtension_OmbCategoryCoding:
    id: String
    extension: Extension
    version: String
    code: PatientUSCoreEthnicityExtension_OmbCategoryCoding_BoundCode
    display: String
    user_selected: Boolean


@dataclass
class PatientUSCoreEthnicityExtension_OmbCategoryCoding_BoundCode:
    value: OmbEthnicityCategoriesValueSet_Value
    id: String
    extension: Extension


@dataclass
class PatientUSCoreEthnicityExtension_DetailedCoding:
    id: String
    extension: Extension
    version: String
    code: PatientUSCoreEthnicityExtension_DetailedCoding_BoundCode
    display: String
    user_selected: Boolean


@dataclass
class PatientUSCoreEthnicityExtension_DetailedCoding_BoundCode:
    value: DetailedEthnicityValueSet_Value
    id: String
    extension: Extension


@dataclass
class PatientUSCoreRaceExtension:
    id: String
    extension: Extension
    omb_category: PatientUSCoreRaceExtension_OmbCategoryCoding
    detailed: PatientUSCoreRaceExtension_DetailedCoding
    text: String


@dataclass
class PatientUSCoreRaceExtension_OmbCategoryCoding:
    id: String
    extension: Extension
    version: String
    code: PatientUSCoreRaceExtension_OmbCategoryCoding_BoundCode
    display: String
    user_selected: Boolean


@dataclass
class PatientUSCoreRaceExtension_OmbCategoryCoding_BoundCode:
    value: OmbRaceCategoriesValueSet_Value
    id: String
    extension: Extension


@dataclass
class PatientUSCoreRaceExtension_DetailedCoding:
    id: String
    extension: Extension
    version: String
    code: PatientUSCoreRaceExtension_DetailedCoding_BoundCode
    display: String
    user_selected: Boolean


@dataclass
class PatientUSCoreRaceExtension_DetailedCoding_BoundCode:
    value: DetailedRaceValueSet_Value
    id: String
    extension: Extension


@dataclass
class USCoreAllergyIntolerance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    clinical_status: CodeableConcept
    verification_status: CodeableConcept
    type: USCoreAllergyIntolerance_TypeCode
    category: USCoreAllergyIntolerance_CategoryCode
    criticality: USCoreAllergyIntolerance_CriticalityCode
    code: CodeableConcept
    patient: Reference
    encounter: Reference
    onset: USCoreAllergyIntolerance_OnsetX
    recorded_date: DateTime
    recorder: Reference
    asserter: Reference
    last_occurrence: DateTime
    note: Annotation
    reaction: USCoreAllergyIntolerance_Reaction


@dataclass
class USCoreAllergyIntolerance_TypeCode:
    value: AllergyIntoleranceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreAllergyIntolerance_CategoryCode:
    value: AllergyIntoleranceCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreAllergyIntolerance_CriticalityCode:
    value: AllergyIntoleranceCriticalityCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreAllergyIntolerance_OnsetX:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class USCoreAllergyIntolerance_Reaction:
    id: String
    extension: Extension
    modifier_extension: Extension
    substance: CodeableConcept
    manifestation: CodeableConcept
    description: String
    onset: DateTime
    severity: USCoreAllergyIntolerance_Reaction_SeverityCode
    exposure_route: CodeableConcept
    note: Annotation


@dataclass
class USCoreAllergyIntolerance_Reaction_SeverityCode:
    value: AllergyIntoleranceSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreCarePlanProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    based_on: Reference
    replaces: Reference
    part_of: Reference
    status: USCoreCarePlanProfile_StatusCode
    intent: USCoreCarePlanProfile_IntentCode
    category: CodeableConcept
    title: String
    description: String
    subject: Reference
    encounter: Reference
    period: Period
    created: DateTime
    author: Reference
    contributor: Reference
    care_team: Reference
    addresses: Reference
    supporting_info: Reference
    goal: Reference
    activity: USCoreCarePlanProfile_Activity
    note: Annotation


@dataclass
class USCoreCarePlanProfile_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreCarePlanProfile_IntentCode:
    value: CarePlanIntentValueSet_Value
    id: String
    extension: Extension


@dataclass
class USCoreCarePlanProfile_Activity:
    id: String
    extension: Extension
    modifier_extension: Extension
    outcome_codeable_concept: CodeableConcept
    outcome_reference: Reference
    progress: Annotation
    reference: Reference
    detail: USCoreCarePlanProfile_Activity_Detail


@dataclass
class USCoreCarePlanProfile_Activity_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: USCoreCarePlanProfile_Activity_Detail_KindCode
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    code: CodeableConcept
    reason_code: CodeableConcept
    reason_reference: Reference
    goal: Reference
    status: USCoreCarePlanProfile_Activity_Detail_StatusCode
    status_reason: CodeableConcept
    do_not_perform: Boolean
    scheduled: USCoreCarePlanProfile_Activity_Detail_ScheduledX
    location: Reference
    performer: Reference
    product: USCoreCarePlanProfile_Activity_Detail_ProductX
    daily_amount: SimpleQuantity
    quantity: SimpleQuantity
    description: String


@dataclass
class USCoreCarePlanProfile_Activity_Detail_KindCode:
    value: CarePlanActivityKindValueSet_Value
    id: String
    extension: Extension


@dataclass
class USCoreCarePlanProfile_Activity_Detail_StatusCode:
    value: CarePlanActivityStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreCarePlanProfile_Activity_Detail_ScheduledX:
    timing: Timing
    period: Period
    string_value: String


@dataclass
class USCoreCarePlanProfile_Activity_Detail_ProductX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class USCoreCareTeam:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: USCoreCareTeam_StatusCode
    category: CodeableConcept
    name: String
    subject: Reference
    encounter: Reference
    period: Period
    participant: USCoreCareTeam_Participant
    reason_code: CodeableConcept
    reason_reference: Reference
    managing_organization: Reference
    telecom: ContactPoint
    note: Annotation


@dataclass
class USCoreCareTeam_StatusCode:
    value: CareTeamStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreCareTeam_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    member: Reference
    on_behalf_of: Reference
    period: Period


@dataclass
class USCoreDiagnosticReportProfileLaboratoryReporting:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    status: USCoreDiagnosticReportProfileLaboratoryReporting_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    effective: USCoreDiagnosticReportProfileLaboratoryReporting_EffectiveX
    issued: Instant
    performer: Reference
    results_interpreter: Reference
    specimen: Reference
    result: Reference
    imaging_study: Reference
    media: USCoreDiagnosticReportProfileLaboratoryReporting_Media
    conclusion: String
    conclusion_code: CodeableConcept
    presented_form: Attachment


@dataclass
class USCoreDiagnosticReportProfileLaboratoryReporting_StatusCode:
    value: DiagnosticReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreDiagnosticReportProfileLaboratoryReporting_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class USCoreDiagnosticReportProfileLaboratoryReporting_Media:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference


@dataclass
class USCoreDiagnosticReportProfileNoteExchange:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    status: USCoreDiagnosticReportProfileNoteExchange_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    effective: USCoreDiagnosticReportProfileNoteExchange_EffectiveX
    issued: Instant
    performer: Reference
    results_interpreter: Reference
    specimen: Reference
    result: Reference
    imaging_study: Reference
    media: USCoreDiagnosticReportProfileNoteExchange_Media
    conclusion: String
    conclusion_code: CodeableConcept
    presented_form: Attachment


@dataclass
class USCoreDiagnosticReportProfileNoteExchange_StatusCode:
    value: DiagnosticReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreDiagnosticReportProfileNoteExchange_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class USCoreDiagnosticReportProfileNoteExchange_Media:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference


@dataclass
class USCoreDocumentReferenceProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    master_identifier: Identifier
    identifier: Identifier
    status: USCoreDocumentReferenceProfile_StatusCode
    doc_status: USCoreDocumentReferenceProfile_DocStatusCode
    type: CodeableConcept
    category: CodeableConcept
    subject: Reference
    date: Instant
    author: Reference
    authenticator: Reference
    custodian: Reference
    relates_to: USCoreDocumentReferenceProfile_RelatesTo
    description: String
    security_label: CodeableConcept
    content: USCoreDocumentReferenceProfile_Content
    context: USCoreDocumentReferenceProfile_Context


@dataclass
class USCoreDocumentReferenceProfile_StatusCode:
    value: DocumentReferenceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreDocumentReferenceProfile_DocStatusCode:
    value: CompositionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreDocumentReferenceProfile_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: USCoreDocumentReferenceProfile_RelatesTo_CodeType
    target: Reference


@dataclass
class USCoreDocumentReferenceProfile_RelatesTo_CodeType:
    value: DocumentRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreDocumentReferenceProfile_Content:
    id: String
    extension: Extension
    modifier_extension: Extension
    attachment: Attachment
    format: Coding


@dataclass
class USCoreDocumentReferenceProfile_Context:
    id: String
    extension: Extension
    modifier_extension: Extension
    encounter: Reference
    event: CodeableConcept
    period: Period
    facility_type: CodeableConcept
    practice_setting: CodeableConcept
    source_patient_info: Reference
    related: Reference


@dataclass
class USCoreEncounterProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: USCoreEncounterProfile_StatusCode
    status_history: USCoreEncounterProfile_StatusHistory
    class_value: Coding
    class_history: USCoreEncounterProfile_ClassHistory
    type: CodeableConcept
    service_type: CodeableConcept
    priority: CodeableConcept
    subject: Reference
    episode_of_care: Reference
    based_on: Reference
    participant: USCoreEncounterProfile_Participant
    appointment: Reference
    period: Period
    length: Duration
    reason_code: CodeableConcept
    reason_reference: Reference
    diagnosis: USCoreEncounterProfile_Diagnosis
    account: Reference
    hospitalization: USCoreEncounterProfile_Hospitalization
    location: USCoreEncounterProfile_Location
    service_provider: Reference
    part_of: Reference


@dataclass
class USCoreEncounterProfile_StatusCode:
    value: EncounterStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreEncounterProfile_StatusHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: USCoreEncounterProfile_StatusHistory_StatusCode
    period: Period


@dataclass
class USCoreEncounterProfile_StatusHistory_StatusCode:
    value: EncounterStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreEncounterProfile_ClassHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    class_value: Coding
    period: Period


@dataclass
class USCoreEncounterProfile_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    period: Period
    individual: Reference


@dataclass
class USCoreEncounterProfile_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    condition: Reference
    use: CodeableConcept
    rank: PositiveInt


@dataclass
class USCoreEncounterProfile_Hospitalization:
    id: String
    extension: Extension
    modifier_extension: Extension
    pre_admission_identifier: Identifier
    origin: Reference
    admit_source: CodeableConcept
    re_admission: CodeableConcept
    diet_preference: CodeableConcept
    special_courtesy: CodeableConcept
    special_arrangement: CodeableConcept
    destination: Reference
    discharge_disposition: CodeableConcept


@dataclass
class USCoreEncounterProfile_Location:
    id: String
    extension: Extension
    modifier_extension: Extension
    location: Reference
    status: USCoreEncounterProfile_Location_StatusCode
    physical_type: CodeableConcept
    period: Period


@dataclass
class USCoreEncounterProfile_Location_StatusCode:
    value: EncounterLocationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreGoalProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    lifecycle_status: USCoreGoalProfile_LifecycleStatusCode
    achievement_status: CodeableConcept
    category: CodeableConcept
    priority: CodeableConcept
    description: CodeableConcept
    subject: Reference
    start: USCoreGoalProfile_StartX
    target: USCoreGoalProfile_Target
    status_date: Date
    status_reason: String
    expressed_by: Reference
    addresses: Reference
    note: Annotation
    outcome_code: CodeableConcept
    outcome_reference: Reference


@dataclass
class USCoreGoalProfile_LifecycleStatusCode:
    value: GoalLifecycleStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreGoalProfile_StartX:
    date: Date
    codeable_concept: CodeableConcept


@dataclass
class USCoreGoalProfile_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: USCoreGoalProfile_Target_DetailX
    due: USCoreGoalProfile_Target_DueX


@dataclass
class USCoreGoalProfile_Target_DetailX:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    ratio: Ratio


@dataclass
class USCoreGoalProfile_Target_DueX:
    date: Date


@dataclass
class USCoreImmunizationProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: USCoreImmunizationProfile_StatusCode
    status_reason: CodeableConcept
    vaccine_code: CodeableConcept
    patient: Reference
    encounter: Reference
    occurrence: USCoreImmunizationProfile_OccurrenceX
    recorded: DateTime
    primary_source: Boolean
    report_origin: CodeableConcept
    location: Reference
    manufacturer: Reference
    lot_number: String
    expiration_date: Date
    site: CodeableConcept
    route: CodeableConcept
    dose_quantity: SimpleQuantity
    performer: USCoreImmunizationProfile_Performer
    note: Annotation
    reason_code: CodeableConcept
    reason_reference: Reference
    is_subpotent: Boolean
    subpotent_reason: CodeableConcept
    education: USCoreImmunizationProfile_Education
    program_eligibility: CodeableConcept
    funding_source: CodeableConcept
    reaction: USCoreImmunizationProfile_Reaction
    protocol_applied: USCoreImmunizationProfile_ProtocolApplied


@dataclass
class USCoreImmunizationProfile_StatusCode:
    value: ImmunizationStatusCodesValueSet_Value
    id: String
    extension: Extension


@dataclass
class USCoreImmunizationProfile_OccurrenceX:
    date_time: DateTime
    string_value: String


@dataclass
class USCoreImmunizationProfile_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference


@dataclass
class USCoreImmunizationProfile_Education:
    id: String
    extension: Extension
    modifier_extension: Extension
    document_type: String
    reference: Uri
    publication_date: DateTime
    presentation_date: DateTime


@dataclass
class USCoreImmunizationProfile_Reaction:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: DateTime
    detail: Reference
    reported: Boolean


@dataclass
class USCoreImmunizationProfile_ProtocolApplied:
    id: String
    extension: Extension
    modifier_extension: Extension
    series: String
    authority: Reference
    target_disease: CodeableConcept
    dose_number: USCoreImmunizationProfile_ProtocolApplied_DoseNumberX
    series_doses: USCoreImmunizationProfile_ProtocolApplied_SeriesDosesX


@dataclass
class USCoreImmunizationProfile_ProtocolApplied_DoseNumberX:
    positive_int: PositiveInt
    string_value: String


@dataclass
class USCoreImmunizationProfile_ProtocolApplied_SeriesDosesX:
    positive_int: PositiveInt
    string_value: String


@dataclass
class USCoreImplantableDeviceProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition: Reference
    udi_carrier: USCoreImplantableDeviceProfile_UdiCarrier
    status: USCoreImplantableDeviceProfile_StatusCode
    status_reason: CodeableConcept
    distinct_identifier: String
    manufacturer: String
    manufacture_date: DateTime
    expiration_date: DateTime
    lot_number: String
    serial_number: String
    device_name: USCoreImplantableDeviceProfile_DeviceName
    model_number: String
    part_number: String
    type: CodeableConcept
    specialization: USCoreImplantableDeviceProfile_Specialization
    version: USCoreImplantableDeviceProfile_Version
    property: USCoreImplantableDeviceProfile_Property
    patient: Reference
    owner: Reference
    contact: ContactPoint
    location: Reference
    url: Uri
    note: Annotation
    safety: CodeableConcept
    parent: Reference


@dataclass
class USCoreImplantableDeviceProfile_UdiCarrier:
    id: String
    extension: Extension
    modifier_extension: Extension
    device_identifier: String
    issuer: Uri
    jurisdiction: Uri
    carrier_aidc: Base64Binary
    carrier_hrf: String
    entry_type: USCoreImplantableDeviceProfile_UdiCarrier_EntryTypeCode


@dataclass
class USCoreImplantableDeviceProfile_UdiCarrier_EntryTypeCode:
    value: UDIEntryTypeCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreImplantableDeviceProfile_StatusCode:
    value: FHIRDeviceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreImplantableDeviceProfile_DeviceName:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    type: USCoreImplantableDeviceProfile_DeviceName_TypeCode


@dataclass
class USCoreImplantableDeviceProfile_DeviceName_TypeCode:
    value: DeviceNameTypeCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreImplantableDeviceProfile_Specialization:
    id: String
    extension: Extension
    modifier_extension: Extension
    system_type: CodeableConcept
    version: String


@dataclass
class USCoreImplantableDeviceProfile_Version:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    component: Identifier
    value: String


@dataclass
class USCoreImplantableDeviceProfile_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value_quantity: Quantity
    value_code: CodeableConcept


@dataclass
class USCoreLaboratoryResultObservationProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: USCoreLaboratoryResultObservationProfile_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: USCoreLaboratoryResultObservationProfile_EffectiveX
    issued: Instant
    performer: Reference
    value: USCoreLaboratoryResultObservationProfile_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: USCoreLaboratoryResultObservationProfile_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: USCoreLaboratoryResultObservationProfile_Component


@dataclass
class USCoreLaboratoryResultObservationProfile_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreLaboratoryResultObservationProfile_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class USCoreLaboratoryResultObservationProfile_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class USCoreLaboratoryResultObservationProfile_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    low: SimpleQuantity
    high: SimpleQuantity
    type: CodeableConcept
    applies_to: CodeableConcept
    age: Range
    text: String


@dataclass
class USCoreLaboratoryResultObservationProfile_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: USCoreLaboratoryResultObservationProfile_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: USCoreLaboratoryResultObservationProfile_ReferenceRange


@dataclass
class USCoreLaboratoryResultObservationProfile_Component_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class USCoreLocation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: USCoreLocation_StatusCode
    operational_status: Coding
    name: String
    alias: String
    description: String
    mode: USCoreLocation_ModeCode
    type: CodeableConcept
    telecom: ContactPoint
    address: Address
    physical_type: CodeableConcept
    position: USCoreLocation_Position
    managing_organization: Reference
    part_of: Reference
    hours_of_operation: USCoreLocation_HoursOfOperation
    availability_exceptions: String
    endpoint: Reference


@dataclass
class USCoreLocation_StatusCode:
    value: LocationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreLocation_ModeCode:
    value: LocationModeCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreLocation_Position:
    id: String
    extension: Extension
    modifier_extension: Extension
    longitude: Decimal
    latitude: Decimal
    altitude: Decimal


@dataclass
class USCoreLocation_HoursOfOperation:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: USCoreLocation_HoursOfOperation_DaysOfWeekCode
    all_day: Boolean
    opening_time: Time
    closing_time: Time


@dataclass
class USCoreLocation_HoursOfOperation_DaysOfWeekCode:
    value: DaysOfWeekCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreMedicationProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    status: USCoreMedicationProfile_StatusCode
    manufacturer: Reference
    form: CodeableConcept
    amount: Ratio
    ingredient: USCoreMedicationProfile_Ingredient
    batch: USCoreMedicationProfile_Batch


@dataclass
class USCoreMedicationProfile_StatusCode:
    value: MedicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreMedicationProfile_Ingredient:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: USCoreMedicationProfile_Ingredient_ItemX
    is_active: Boolean
    strength: Ratio


@dataclass
class USCoreMedicationProfile_Ingredient_ItemX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class USCoreMedicationProfile_Batch:
    id: String
    extension: Extension
    modifier_extension: Extension
    lot_number: String
    expiration_date: DateTime


@dataclass
class USCoreMedicationRequestProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: USCoreMedicationRequestProfile_StatusCode
    status_reason: CodeableConcept
    intent: USCoreMedicationRequestProfile_IntentCode
    category: CodeableConcept
    priority: USCoreMedicationRequestProfile_PriorityCode
    do_not_perform: Boolean
    reported: USCoreMedicationRequestProfile_ReportedX
    medication: USCoreMedicationRequestProfile_MedicationX
    subject: Reference
    encounter: Reference
    supporting_information: Reference
    authored_on: DateTime
    requester: Reference
    performer: Reference
    performer_type: CodeableConcept
    recorder: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    based_on: Reference
    group_identifier: Identifier
    course_of_therapy_type: CodeableConcept
    insurance: Reference
    note: Annotation
    dosage_instruction: Dosage
    dispense_request: USCoreMedicationRequestProfile_DispenseRequest
    substitution: USCoreMedicationRequestProfile_Substitution
    prior_prescription: Reference
    detected_issue: Reference
    event_history: Reference


@dataclass
class USCoreMedicationRequestProfile_StatusCode:
    value: MedicationrequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreMedicationRequestProfile_IntentCode:
    value: MedicationRequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreMedicationRequestProfile_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreMedicationRequestProfile_ReportedX:
    boolean: Boolean
    reference: Reference


@dataclass
class USCoreMedicationRequestProfile_MedicationX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class USCoreMedicationRequestProfile_DispenseRequest:
    id: String
    extension: Extension
    modifier_extension: Extension
    initial_fill: USCoreMedicationRequestProfile_DispenseRequest_InitialFill
    dispense_interval: Duration
    validity_period: Period
    number_of_repeats_allowed: UnsignedInt
    quantity: SimpleQuantity
    expected_supply_duration: Duration
    performer: Reference


@dataclass
class USCoreMedicationRequestProfile_DispenseRequest_InitialFill:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: SimpleQuantity
    duration: Duration


@dataclass
class USCoreMedicationRequestProfile_Substitution:
    id: String
    extension: Extension
    modifier_extension: Extension
    allowed: USCoreMedicationRequestProfile_Substitution_AllowedX
    reason: CodeableConcept


@dataclass
class USCoreMedicationRequestProfile_Substitution_AllowedX:
    boolean: Boolean
    codeable_concept: CodeableConcept


@dataclass
class USCoreOrganizationProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    type: CodeableConcept
    name: String
    alias: String
    telecom: ContactPoint
    address: Address
    part_of: Reference
    contact: USCoreOrganizationProfile_Contact
    endpoint: Reference


@dataclass
class USCoreOrganizationProfile_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    purpose: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address


@dataclass
class USCorePatientProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    name: HumanName
    telecom: ContactPoint
    gender: USCorePatientProfile_GenderCode
    birth_date: Date
    deceased: USCorePatientProfile_DeceasedX
    address: Address
    marital_status: CodeableConcept
    multiple_birth: USCorePatientProfile_MultipleBirthX
    photo: Attachment
    contact: USCorePatientProfile_Contact
    communication: USCorePatientProfile_Communication
    general_practitioner: Reference
    managing_organization: Reference
    link: USCorePatientProfile_Link
    race: PatientUSCoreRaceExtension
    ethnicity: PatientUSCoreEthnicityExtension
    birthsex: PatientUSCoreBirthSexExtension_ValueCode


@dataclass
class USCorePatientProfile_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePatientProfile_DeceasedX:
    boolean: Boolean
    date_time: DateTime


@dataclass
class USCorePatientProfile_MultipleBirthX:
    boolean: Boolean
    integer: Integer


@dataclass
class USCorePatientProfile_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    relationship: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address
    gender: USCorePatientProfile_Contact_GenderCode
    organization: Reference
    period: Period


@dataclass
class USCorePatientProfile_Contact_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePatientProfile_Communication:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: CodeableConcept
    preferred: Boolean


@dataclass
class USCorePatientProfile_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    other: Reference
    type: USCorePatientProfile_Link_TypeCode


@dataclass
class USCorePatientProfile_Link_TypeCode:
    value: LinkTypeCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePediatricBMIforAgeObservationProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: USCorePediatricBMIforAgeObservationProfile_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: USCorePediatricBMIforAgeObservationProfile_EffectiveX
    issued: Instant
    performer: Reference
    value: USCorePediatricBMIforAgeObservationProfile_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: USCorePediatricBMIforAgeObservationProfile_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: USCorePediatricBMIforAgeObservationProfile_Component


@dataclass
class USCorePediatricBMIforAgeObservationProfile_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePediatricBMIforAgeObservationProfile_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class USCorePediatricBMIforAgeObservationProfile_ValueX:
    quantity: Quantity


@dataclass
class USCorePediatricBMIforAgeObservationProfile_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    low: SimpleQuantity
    high: SimpleQuantity
    type: CodeableConcept
    applies_to: CodeableConcept
    age: Range
    text: String


@dataclass
class USCorePediatricBMIforAgeObservationProfile_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: USCorePediatricBMIforAgeObservationProfile_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: USCorePediatricBMIforAgeObservationProfile_ReferenceRange


@dataclass
class USCorePediatricBMIforAgeObservationProfile_Component_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class USCorePediatricWeightForHeightObservationProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: USCorePediatricWeightForHeightObservationProfile_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: USCorePediatricWeightForHeightObservationProfile_EffectiveX
    issued: Instant
    performer: Reference
    value: USCorePediatricWeightForHeightObservationProfile_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: USCorePediatricWeightForHeightObservationProfile_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: USCorePediatricWeightForHeightObservationProfile_Component


@dataclass
class USCorePediatricWeightForHeightObservationProfile_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePediatricWeightForHeightObservationProfile_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class USCorePediatricWeightForHeightObservationProfile_ValueX:
    quantity: Quantity


@dataclass
class USCorePediatricWeightForHeightObservationProfile_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    low: SimpleQuantity
    high: SimpleQuantity
    type: CodeableConcept
    applies_to: CodeableConcept
    age: Range
    text: String


@dataclass
class USCorePediatricWeightForHeightObservationProfile_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: USCorePediatricWeightForHeightObservationProfile_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: USCorePediatricWeightForHeightObservationProfile_ReferenceRange


@dataclass
class USCorePediatricWeightForHeightObservationProfile_Component_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class USCorePractitionerProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    name: HumanName
    telecom: ContactPoint
    address: Address
    gender: USCorePractitionerProfile_GenderCode
    birth_date: Date
    photo: Attachment
    qualification: USCorePractitionerProfile_Qualification
    communication: CodeableConcept


@dataclass
class USCorePractitionerProfile_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePractitionerProfile_Qualification:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    period: Period
    issuer: Reference


@dataclass
class USCorePractitionerRoleProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    period: Period
    practitioner: Reference
    organization: Reference
    code: CodeableConcept
    specialty: CodeableConcept
    location: Reference
    healthcare_service: Reference
    telecom: ContactPoint
    available_time: USCorePractitionerRoleProfile_AvailableTime
    not_available: USCorePractitionerRoleProfile_NotAvailable
    availability_exceptions: String
    endpoint: Reference


@dataclass
class USCorePractitionerRoleProfile_AvailableTime:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: USCorePractitionerRoleProfile_AvailableTime_DaysOfWeekCode
    all_day: Boolean
    available_start_time: Time
    available_end_time: Time


@dataclass
class USCorePractitionerRoleProfile_AvailableTime_DaysOfWeekCode:
    value: DaysOfWeekCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePractitionerRoleProfile_NotAvailable:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    during: Period


@dataclass
class USCoreProcedureProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    based_on: Reference
    part_of: Reference
    status: USCoreProcedureProfile_StatusCode
    status_reason: CodeableConcept
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    performed: USCoreProcedureProfile_PerformedX
    recorder: Reference
    asserter: Reference
    performer: USCoreProcedureProfile_Performer
    location: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    body_site: CodeableConcept
    outcome: CodeableConcept
    report: Reference
    complication: CodeableConcept
    complication_detail: Reference
    follow_up: CodeableConcept
    note: Annotation
    focal_device: USCoreProcedureProfile_FocalDevice
    used_reference: Reference
    used_code: CodeableConcept


@dataclass
class USCoreProcedureProfile_StatusCode:
    value: EventStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCoreProcedureProfile_PerformedX:
    date_time: DateTime
    period: Period


@dataclass
class USCoreProcedureProfile_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference
    on_behalf_of: Reference


@dataclass
class USCoreProcedureProfile_FocalDevice:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: CodeableConcept
    manipulated: Reference


@dataclass
class USCoreProvenance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    target: Reference
    occurred: USCoreProvenance_OccurredX
    recorded: Instant
    policy: Uri
    location: Reference
    reason: CodeableConcept
    activity: CodeableConcept
    agent: USCoreProvenance_Agent
    entity: USCoreProvenance_Entity
    signature: Signature


@dataclass
class USCoreProvenance_OccurredX:
    period: Period
    date_time: DateTime


@dataclass
class USCoreProvenance_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    role: CodeableConcept
    who: Reference
    on_behalf_of: Reference


@dataclass
class USCoreProvenance_Entity:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: USCoreProvenance_Entity_RoleCode
    what: Reference
    agent: USCoreProvenance_Agent


@dataclass
class USCoreProvenance_Entity_RoleCode:
    value: ProvenanceEntityRoleCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePulseOximetryProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: USCorePulseOximetryProfile_StatusCode
    category: CodeableConcept
    code: USCorePulseOximetryProfile_CodeableConceptForCode
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: USCorePulseOximetryProfile_EffectiveX
    issued: Instant
    performer: Reference
    value: USCorePulseOximetryProfile_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: USCorePulseOximetryProfile_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: USCorePulseOximetryProfile_Component


@dataclass
class USCorePulseOximetryProfile_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class USCorePulseOximetryProfile_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    oxygen_sat_code: CodingWithFixedCode
    pulse_ox: CodingWithFixedCode


@dataclass
class USCorePulseOximetryProfile_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class USCorePulseOximetryProfile_ValueX:
    quantity: Quantity


@dataclass
class USCorePulseOximetryProfile_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    low: SimpleQuantity
    high: SimpleQuantity
    type: CodeableConcept
    applies_to: CodeableConcept
    age: Range
    text: String


@dataclass
class USCorePulseOximetryProfile_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: USCorePulseOximetryProfile_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: USCorePulseOximetryProfile_ReferenceRange


@dataclass
class USCorePulseOximetryProfile_Component_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class USCoreSmokingStatusProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: USCoreSmokingStatusProfile_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: USCoreSmokingStatusProfile_EffectiveX
    issued: Instant
    performer: Reference
    value: USCoreSmokingStatusProfile_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: USCoreSmokingStatusProfile_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: USCoreSmokingStatusProfile_Component


@dataclass
class USCoreSmokingStatusProfile_StatusCode:
    value: USCoreObservationSmokingStatusStatusValueSet_Value
    id: String
    extension: Extension


@dataclass
class USCoreSmokingStatusProfile_EffectiveX:
    date_time: DateTime
    period: Period
    timing: Timing
    instant: Instant


@dataclass
class USCoreSmokingStatusProfile_ValueX:
    codeable_concept: CodeableConcept


@dataclass
class USCoreSmokingStatusProfile_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    low: SimpleQuantity
    high: SimpleQuantity
    type: CodeableConcept
    applies_to: CodeableConcept
    age: Range
    text: String


@dataclass
class USCoreSmokingStatusProfile_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: USCoreSmokingStatusProfile_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: USCoreSmokingStatusProfile_ReferenceRange


@dataclass
class USCoreSmokingStatusProfile_Component_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class UsCoreCondition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    clinical_status: CodeableConcept
    verification_status: CodeableConcept
    category: CodeableConcept
    severity: CodeableConcept
    code: CodeableConcept
    body_site: CodeableConcept
    subject: Reference
    encounter: Reference
    onset: UsCoreCondition_OnsetX
    abatement: UsCoreCondition_AbatementX
    recorded_date: DateTime
    recorder: Reference
    asserter: Reference
    stage: UsCoreCondition_Stage
    evidence: UsCoreCondition_Evidence
    note: Annotation


@dataclass
class UsCoreCondition_OnsetX:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class UsCoreCondition_AbatementX:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class UsCoreCondition_Stage:
    id: String
    extension: Extension
    modifier_extension: Extension
    summary: CodeableConcept
    assessment: Reference
    type: CodeableConcept


@dataclass
class UsCoreCondition_Evidence:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    detail: Reference


@dataclass
class UsCoreDirectEmail:
    id: String
    extension: Extension
    value_boolean: Boolean

