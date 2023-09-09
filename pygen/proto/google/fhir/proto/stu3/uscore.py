# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.uscore
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class UsCoreAllergyintolerance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    clinical_status: AllergyIntoleranceClinicalStatusCode
    verification_status: AllergyIntoleranceVerificationStatusCode
    type: AllergyIntoleranceTypeCode
    category: AllergyIntoleranceCategoryCode
    criticality: AllergyIntoleranceCriticalityCode
    code: CodeableConcept
    patient: Reference
    onset: UsCoreAllergyintolerance_Onset
    asserted_date: DateTime
    recorder: Reference
    asserter: Reference
    last_occurrence: DateTime
    note: Annotation
    reaction: UsCoreAllergyintolerance_Reaction


@dataclass
class UsCoreAllergyintolerance_Onset:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class UsCoreAllergyintolerance_Reaction:
    id: String
    extension: Extension
    modifier_extension: Extension
    substance: CodeableConcept
    manifestation: CodeableConcept
    description: String
    onset: DateTime
    severity: AllergyIntoleranceSeverityCode
    exposure_route: CodeableConcept
    note: Annotation


@dataclass
class PatientUSCoreBirthSexExtension:
    id: String
    extension: Extension
    value_code: UsCoreBirthSexCode


@dataclass
class UsCoreCareplan:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition: Reference
    based_on: Reference
    replaces: Reference
    part_of: Reference
    status: CarePlanStatusCode
    intent: CarePlanIntentCode
    category: CodeableConcept
    title: String
    description: String
    subject: Reference
    context: Reference
    period: Period
    author: Reference
    care_team: Reference
    addresses: Reference
    supporting_info: Reference
    goal: Reference
    activity: UsCoreCareplan_Activity
    note: Annotation


@dataclass
class UsCoreCareplan_Activity:
    id: String
    extension: Extension
    modifier_extension: Extension
    outcome_codeable_concept: CodeableConcept
    outcome_reference: Reference
    progress: Annotation
    reference: Reference
    detail: UsCoreCareplan_Activity_Detail


@dataclass
class UsCoreCareplan_Activity_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    definition: Reference
    code: CodeableConcept
    reason_code: CodeableConcept
    reason_reference: Reference
    goal: Reference
    status: CarePlanActivityStatusCode
    status_reason: String
    prohibited: Boolean
    scheduled: UsCoreCareplan_Activity_Detail_Scheduled
    location: Reference
    performer: Reference
    product: UsCoreCareplan_Activity_Detail_Product
    daily_amount: SimpleQuantity
    quantity: SimpleQuantity
    description: String


@dataclass
class UsCoreCareplan_Activity_Detail_Scheduled:
    timing: Timing
    period: Period
    string_value: String


@dataclass
class UsCoreCareplan_Activity_Detail_Product:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class UsCoreCareteam:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: CareTeamStatusCode
    category: CodeableConcept
    name: String
    subject: Reference
    context: Reference
    period: Period
    participant: UsCoreCareteam_Participant
    reason_code: CodeableConcept
    reason_reference: Reference
    managing_organization: Reference
    note: Annotation


@dataclass
class UsCoreCareteam_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    member: Reference
    on_behalf_of: Reference
    period: Period


@dataclass
class UsCoreCondition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    clinical_status: ConditionClinicalStatusCodesCode
    verification_status: ConditionVerificationStatusCode
    category: CodeableConcept
    severity: CodeableConcept
    code: CodeableConcept
    body_site: CodeableConcept
    subject: Reference
    context: Reference
    onset: UsCoreCondition_Onset
    abatement: UsCoreCondition_Abatement
    asserted_date: DateTime
    asserter: Reference
    stage: UsCoreCondition_Stage
    evidence: UsCoreCondition_Evidence
    note: Annotation


@dataclass
class UsCoreCondition_Onset:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class UsCoreCondition_Abatement:
    date_time: DateTime
    age: Age
    boolean: Boolean
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


@dataclass
class UsCoreCondition_Evidence:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    detail: Reference


@dataclass
class UsCoreDevice:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    udi: UsCoreDevice_Udi
    status: FHIRDeviceStatusCode
    type: CodeableConcept
    lot_number: String
    manufacturer: String
    manufacture_date: DateTime
    expiration_date: DateTime
    model: String
    version: String
    patient: Reference
    owner: Reference
    contact: ContactPoint
    location: Reference
    url: Uri
    note: Annotation
    safety: CodeableConcept


@dataclass
class UsCoreDevice_Udi:
    id: String
    extension: Extension
    modifier_extension: Extension
    device_identifier: String
    name: String
    jurisdiction: Uri
    carrier_hrf: String
    carrier_aidc: Base64Binary
    issuer: Uri
    entry_type: UDIEntryTypeCode


@dataclass
class UsCoreDiagnosticreport:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    status: DiagnosticReportStatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    context: Reference
    effective: UsCoreDiagnosticreport_Effective
    issued: Instant
    performer: UsCoreDiagnosticreport_Performer
    specimen: Reference
    result: Reference
    imaging_study: Reference
    image: UsCoreDiagnosticreport_Image
    conclusion: String
    coded_diagnosis: CodeableConcept
    presented_form: Attachment


@dataclass
class UsCoreDiagnosticreport_Effective:
    date_time: DateTime
    period: Period


@dataclass
class UsCoreDiagnosticreport_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class UsCoreDiagnosticreport_Image:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference


@dataclass
class UsCoreDirectEmail:
    id: String
    extension: Extension
    value_boolean: Boolean


@dataclass
class UsCoreDocumentreference:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    master_identifier: Identifier
    identifier: Identifier
    status: DocumentReferenceStatusCode
    doc_status: CompositionStatusCode
    type: CodeableConcept
    class_value: CodeableConcept
    subject: Reference
    created: DateTime
    indexed: Instant
    author: Reference
    authenticator: Reference
    custodian: Reference
    relates_to: UsCoreDocumentreference_RelatesTo
    description: String
    security_label: CodeableConcept
    content: UsCoreDocumentreference_Content
    context: UsCoreDocumentreference_Context


@dataclass
class UsCoreDocumentreference_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: DocumentRelationshipTypeCode
    target: Reference


@dataclass
class UsCoreDocumentreference_Content:
    id: String
    extension: Extension
    modifier_extension: Extension
    attachment: Attachment
    format: Coding


@dataclass
class UsCoreDocumentreference_Context:
    id: String
    extension: Extension
    modifier_extension: Extension
    encounter: Reference
    event: CodeableConcept
    period: Period
    facility_type: CodeableConcept
    practice_setting: CodeableConcept
    source_patient_info: Reference
    related: UsCoreDocumentreference_Context_Related


@dataclass
class UsCoreDocumentreference_Context_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    ref: Reference


@dataclass
class UsCoreEncounter:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: EncounterStatusCode
    status_history: UsCoreEncounter_StatusHistory
    class_value: Coding
    class_history: UsCoreEncounter_ClassHistory
    type: CodeableConcept
    priority: CodeableConcept
    subject: Reference
    episode_of_care: Reference
    incoming_referral: Reference
    participant: UsCoreEncounter_Participant
    appointment: Reference
    period: Period
    length: Duration
    reason: CodeableConcept
    diagnosis: UsCoreEncounter_Diagnosis
    account: Reference
    hospitalization: UsCoreEncounter_Hospitalization
    location: UsCoreEncounter_Location
    service_provider: Reference
    part_of: Reference


@dataclass
class UsCoreEncounter_StatusHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: EncounterStatusCode
    period: Period


@dataclass
class UsCoreEncounter_ClassHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    class_value: Coding
    period: Period


@dataclass
class UsCoreEncounter_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    period: Period
    individual: Reference


@dataclass
class UsCoreEncounter_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    condition: Reference
    role: CodeableConcept
    rank: PositiveInt


@dataclass
class UsCoreEncounter_Hospitalization:
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
class UsCoreEncounter_Location:
    id: String
    extension: Extension
    modifier_extension: Extension
    location: Reference
    status: EncounterLocationStatusCode
    period: Period


@dataclass
class PatientUSCoreEthnicityExtension:
    id: String
    extension: Extension
    omb_category: Coding
    detailed: Coding
    text: String


@dataclass
class UsCoreGoal:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: GoalStatusCode
    category: CodeableConcept
    priority: CodeableConcept
    description: CodeableConcept
    subject: Reference
    start: UsCoreGoal_Start
    target: UsCoreGoal_Target
    status_date: Date
    status_reason: String
    expressed_by: Reference
    addresses: Reference
    note: Annotation
    outcome_code: CodeableConcept
    outcome_reference: Reference


@dataclass
class UsCoreGoal_Start:
    date: Date
    codeable_concept: CodeableConcept


@dataclass
class UsCoreGoal_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: UsCoreGoal_Target_Detail
    due: UsCoreGoal_Target_Due


@dataclass
class UsCoreGoal_Target_Detail:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept


@dataclass
class UsCoreGoal_Target_Due:
    date: Date
    duration: Duration


@dataclass
class UsCoreImmunization:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ImmunizationStatusCodesCode
    not_given: Boolean
    vaccine_code: CodeableConcept
    patient: Reference
    encounter: Reference
    date: DateTime
    primary_source: Boolean
    report_origin: CodeableConcept
    location: Reference
    manufacturer: Reference
    lot_number: String
    expiration_date: Date
    site: CodeableConcept
    route: CodeableConcept
    dose_quantity: SimpleQuantity
    practitioner: UsCoreImmunization_Practitioner
    note: Annotation
    explanation: UsCoreImmunization_Explanation
    reaction: UsCoreImmunization_Reaction
    vaccination_protocol: UsCoreImmunization_VaccinationProtocol


@dataclass
class UsCoreImmunization_Practitioner:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class UsCoreImmunization_Explanation:
    id: String
    extension: Extension
    modifier_extension: Extension
    reason: CodeableConcept
    reason_not_given: CodeableConcept


@dataclass
class UsCoreImmunization_Reaction:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: DateTime
    detail: Reference
    reported: Boolean


@dataclass
class UsCoreImmunization_VaccinationProtocol:
    id: String
    extension: Extension
    modifier_extension: Extension
    dose_sequence: PositiveInt
    description: String
    authority: Reference
    series: String
    series_doses: PositiveInt
    target_disease: CodeableConcept
    dose_status: CodeableConcept
    dose_status_reason: CodeableConcept


@dataclass
class UsCoreLocation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: LocationStatusCode
    operational_status: Coding
    name: String
    alias: String
    description: String
    mode: LocationModeCode
    type: CodeableConcept
    telecom: ContactPoint
    address: Address
    physical_type: CodeableConcept
    position: UsCoreLocation_Position
    managing_organization: Reference
    part_of: Reference
    endpoint: Reference


@dataclass
class UsCoreLocation_Position:
    id: String
    extension: Extension
    modifier_extension: Extension
    longitude: Decimal
    latitude: Decimal
    altitude: Decimal


@dataclass
class UsCoreMedication:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    status: MedicationStatusCode
    is_brand: Boolean
    is_over_the_counter: Boolean
    manufacturer: Reference
    form: CodeableConcept
    ingredient: UsCoreMedication_Ingredient
    package_value: UsCoreMedication_Package
    image: Attachment


@dataclass
class UsCoreMedication_Ingredient:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: UsCoreMedication_Ingredient_Item
    is_active: Boolean
    amount: Ratio


@dataclass
class UsCoreMedication_Ingredient_Item:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class UsCoreMedication_Package:
    id: String
    extension: Extension
    modifier_extension: Extension
    container: CodeableConcept
    content: UsCoreMedication_Package_Content
    batch: UsCoreMedication_Package_Batch


@dataclass
class UsCoreMedication_Package_Content:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: UsCoreMedication_Package_Content_Item
    amount: SimpleQuantity


@dataclass
class UsCoreMedication_Package_Content_Item:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class UsCoreMedication_Package_Batch:
    id: String
    extension: Extension
    modifier_extension: Extension
    lot_number: String
    expiration_date: DateTime


@dataclass
class UsCoreMedicationrequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition: Reference
    based_on: Reference
    group_identifier: Identifier
    status: MedicationRequestStatusCode
    intent: MedicationRequestIntentCode
    category: CodeableConcept
    priority: MedicationRequestPriorityCode
    medication: UsCoreMedicationrequest_Medication
    subject: Reference
    context: Reference
    supporting_information: Reference
    authored_on: DateTime
    requester: UsCoreMedicationrequest_Requester
    recorder: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    dosage_instruction: Dosage
    dispense_request: UsCoreMedicationrequest_DispenseRequest
    substitution: UsCoreMedicationrequest_Substitution
    prior_prescription: Reference
    detected_issue: Reference
    event_history: Reference


@dataclass
class UsCoreMedicationrequest_Medication:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class UsCoreMedicationrequest_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class UsCoreMedicationrequest_DispenseRequest:
    id: String
    extension: Extension
    modifier_extension: Extension
    validity_period: Period
    number_of_repeats_allowed: PositiveInt
    quantity: SimpleQuantity
    expected_supply_duration: Duration
    performer: Reference


@dataclass
class UsCoreMedicationrequest_Substitution:
    id: String
    extension: Extension
    modifier_extension: Extension
    allowed: Boolean
    reason: CodeableConcept


@dataclass
class UsCoreMedicationstatement:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    context: Reference
    status: MedicationStatementStatusCode
    category: CodeableConcept
    medication: UsCoreMedicationstatement_Medication
    effective: UsCoreMedicationstatement_Effective
    date_asserted: DateTime
    information_source: Reference
    subject: Reference
    derived_from: Reference
    taken: MedicationStatementTakenCode
    reason_not_taken: CodeableConcept
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    dosage: Dosage


@dataclass
class UsCoreMedicationstatement_Medication:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class UsCoreMedicationstatement_Effective:
    date_time: DateTime
    period: Period


@dataclass
class UsCoreObservationresults:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    status: ObservationStatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    context: Reference
    effective: UsCoreObservationresults_Effective
    issued: Instant
    performer: Reference
    value: UsCoreObservationresults_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: UsCoreObservationresults_ReferenceRange
    related: UsCoreObservationresults_Related
    component: UsCoreObservationresults_Component


@dataclass
class UsCoreObservationresults_Effective:
    date_time: DateTime
    period: Period


@dataclass
class UsCoreObservationresults_Value:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    attachment: Attachment
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class UsCoreObservationresults_ReferenceRange:
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
class UsCoreObservationresults_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class UsCoreObservationresults_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: UsCoreObservationresults_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: UsCoreObservationresults_ReferenceRange


@dataclass
class UsCoreObservationresults_Component_Value:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    attachment: Attachment
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class UsCoreOrganization:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
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
    contact: UsCoreOrganization_Contact
    endpoint: Reference


@dataclass
class UsCoreOrganization_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    purpose: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address


@dataclass
class UsCorePatient:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    name: HumanName
    telecom: ContactPoint
    gender: AdministrativeGenderCode
    birth_date: Date
    deceased: UsCorePatient_Deceased
    address: Address
    marital_status: CodeableConcept
    multiple_birth: UsCorePatient_MultipleBirth
    photo: Attachment
    contact: UsCorePatient_Contact
    communication: UsCorePatient_Communication
    general_practitioner: Reference
    managing_organization: Reference
    link: UsCorePatient_Link
    race: PatientUSCoreRaceExtension
    ethnicity: PatientUSCoreEthnicityExtension
    birthsex: UsCoreBirthSexCode


@dataclass
class UsCorePatient_Deceased:
    boolean: Boolean
    date_time: DateTime


@dataclass
class UsCorePatient_MultipleBirth:
    boolean: Boolean
    integer: Integer


@dataclass
class UsCorePatient_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    relationship: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address
    gender: AdministrativeGenderCode
    organization: Reference
    period: Period


@dataclass
class UsCorePatient_Communication:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: CodeableConcept
    preferred: Boolean


@dataclass
class UsCorePatient_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    other: Reference
    type: LinkTypeCode


@dataclass
class UsCorePractitioner:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    name: HumanName
    telecom: ContactPoint
    address: Address
    gender: AdministrativeGenderCode
    birth_date: Date
    photo: Attachment
    qualification: UsCorePractitioner_Qualification
    communication: CodeableConcept


@dataclass
class UsCorePractitioner_Qualification:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    period: Period
    issuer: Reference


@dataclass
class UsCorePractitionerrole:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
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
    available_time: UsCorePractitionerrole_AvailableTime
    not_available: UsCorePractitionerrole_NotAvailable
    availability_exceptions: String
    endpoint: Reference


@dataclass
class UsCorePractitionerrole_AvailableTime:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: DaysOfWeekCode
    all_day: Boolean
    available_start_time: Time
    available_end_time: Time


@dataclass
class UsCorePractitionerrole_NotAvailable:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    during: Period


@dataclass
class UsCoreProcedure:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition: Reference
    based_on: Reference
    part_of: Reference
    status: EventStatusCode
    not_done: Boolean
    not_done_reason: CodeableConcept
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    context: Reference
    performed: UsCoreProcedure_Performed
    performer: UsCoreProcedure_Performer
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
    focal_device: UsCoreProcedure_FocalDevice
    used_reference: Reference
    used_code: CodeableConcept


@dataclass
class UsCoreProcedure_Performed:
    date_time: DateTime
    period: Period


@dataclass
class UsCoreProcedure_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference
    on_behalf_of: Reference


@dataclass
class UsCoreProcedure_FocalDevice:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: CodeableConcept
    manipulated: Reference


@dataclass
class CapabilityStatementProfileResourceAssociationExtension:
    id: String
    extension: Extension
    value_code: ResourceTypeCode


@dataclass
class PatientUSCoreRaceExtension:
    id: String
    extension: Extension
    omb_category: Coding
    detailed: Coding
    text: String


@dataclass
class UsCoreSmokingstatus:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    status: ObservationStatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    context: Reference
    effective: UsCoreSmokingstatus_Effective
    issued: Instant
    performer: Reference
    value: UsCoreSmokingstatus_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: UsCoreSmokingstatus_ReferenceRange
    related: UsCoreSmokingstatus_Related
    component: UsCoreSmokingstatus_Component


@dataclass
class UsCoreSmokingstatus_Effective:
    date_time: DateTime
    period: Period


@dataclass
class UsCoreSmokingstatus_Value:
    codeable_concept: CodeableConcept


@dataclass
class UsCoreSmokingstatus_ReferenceRange:
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
class UsCoreSmokingstatus_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class UsCoreSmokingstatus_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: UsCoreSmokingstatus_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: UsCoreSmokingstatus_ReferenceRange


@dataclass
class UsCoreSmokingstatus_Component_Value:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    attachment: Attachment
    time: Time
    date_time: DateTime
    period: Period

