# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Account:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: AccountStatusCode
    type: CodeableConcept
    name: String
    subject: Reference
    period: Period
    active: Period
    balance: Money
    coverage: Account_Coverage
    owner: Reference
    description: String
    guarantor: Account_Guarantor


@dataclass
class Account_Coverage:
    id: String
    extension: Extension
    modifier_extension: Extension
    coverage: Reference
    priority: PositiveInt


@dataclass
class Account_Guarantor:
    id: String
    extension: Extension
    modifier_extension: Extension
    party: Reference
    on_hold: Boolean
    period: Period


@dataclass
class ActivityDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    description: Markdown
    purpose: Markdown
    usage: String
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    use_context: UsageContext
    jurisdiction: CodeableConcept
    topic: CodeableConcept
    contributor: Contributor
    contact: ContactDetail
    copyright: Markdown
    related_artifact: RelatedArtifact
    library: Reference
    kind: ResourceTypeCode
    code: CodeableConcept
    timing: ActivityDefinition_TimingType
    location: Reference
    participant: ActivityDefinition_Participant
    product: ActivityDefinition_Product
    quantity: SimpleQuantity
    dosage: Dosage
    body_site: CodeableConcept
    transform: Reference
    dynamic_value: ActivityDefinition_DynamicValue


@dataclass
class ActivityDefinition_TimingType:
    timing_value: Timing
    date_time: DateTime
    period: Period
    range: Range


@dataclass
class ActivityDefinition_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ActionParticipantTypeCode
    role: CodeableConcept


@dataclass
class ActivityDefinition_Product:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class ActivityDefinition_DynamicValue:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    path: String
    language: String
    expression: String


@dataclass
class AdverseEvent:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    category: AdverseEventCategoryCode
    type: CodeableConcept
    subject: Reference
    date: DateTime
    reaction: Reference
    location: Reference
    seriousness: CodeableConcept
    outcome: CodeableConcept
    recorder: Reference
    event_participant: Reference
    description: String
    suspect_entity: AdverseEvent_SuspectEntity
    subject_medical_history: Reference
    reference_document: Reference
    study: Reference


@dataclass
class AdverseEvent_SuspectEntity:
    id: String
    extension: Extension
    modifier_extension: Extension
    instance: Reference
    causality: AdverseEventCausalityCode
    causality_assessment: CodeableConcept
    causality_product_relatedness: String
    causality_method: CodeableConcept
    causality_author: Reference
    causality_result: CodeableConcept


@dataclass
class AllergyIntolerance:
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
    onset: AllergyIntolerance_Onset
    asserted_date: DateTime
    recorder: Reference
    asserter: Reference
    last_occurrence: DateTime
    note: Annotation
    reaction: AllergyIntolerance_Reaction


@dataclass
class AllergyIntolerance_Onset:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class AllergyIntolerance_Reaction:
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
class Appointment:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: AppointmentStatusCode
    service_category: CodeableConcept
    service_type: CodeableConcept
    specialty: CodeableConcept
    appointment_type: CodeableConcept
    reason: CodeableConcept
    indication: Reference
    priority: UnsignedInt
    description: String
    supporting_information: Reference
    start: Instant
    end: Instant
    minutes_duration: PositiveInt
    slot: Reference
    created: DateTime
    comment: String
    incoming_referral: Reference
    participant: Appointment_Participant
    requested_period: Period


@dataclass
class Appointment_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    actor: Reference
    required: ParticipantRequiredCode
    status: ParticipationStatusCode


@dataclass
class AppointmentResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    appointment: Reference
    start: Instant
    end: Instant
    participant_type: CodeableConcept
    actor: Reference
    participant_status: ParticipationStatusCode
    comment: String


@dataclass
class AuditEvent:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    type: Coding
    subtype: Coding
    action: AuditEventActionCode
    recorded: Instant
    outcome: AuditEventOutcomeCode
    outcome_desc: String
    purpose_of_event: CodeableConcept
    agent: AuditEvent_Agent
    source: AuditEvent_Source
    entity: AuditEvent_Entity


@dataclass
class AuditEvent_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    reference: Reference
    user_id: Identifier
    alt_id: String
    name: String
    requestor: Boolean
    location: Reference
    policy: Uri
    media: Coding
    network: AuditEvent_Agent_Network
    purpose_of_use: CodeableConcept


@dataclass
class AuditEvent_Agent_Network:
    id: String
    extension: Extension
    modifier_extension: Extension
    address: String
    type: AuditEventAgentNetworkTypeCode


@dataclass
class AuditEvent_Source:
    id: String
    extension: Extension
    modifier_extension: Extension
    site: String
    identifier: Identifier
    type: Coding


@dataclass
class AuditEvent_Entity:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    reference: Reference
    type: Coding
    role: Coding
    lifecycle: Coding
    security_label: Coding
    name: String
    description: String
    query: Base64Binary
    detail: AuditEvent_Entity_Detail


@dataclass
class AuditEvent_Entity_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: String
    value: Base64Binary


@dataclass
class Basic:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    subject: Reference
    created: Date
    author: Reference


@dataclass
class Binary:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    content_type: MimeTypeCode
    security_context: Reference
    content: Base64Binary


@dataclass
class BodySite:
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
    code: CodeableConcept
    qualifier: CodeableConcept
    description: String
    image: Attachment
    patient: Reference


@dataclass
class Bundle:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    identifier: Identifier
    type: BundleTypeCode
    total: UnsignedInt
    link: Bundle_Link
    entry: Bundle_Entry
    signature: Signature


@dataclass
class Bundle_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    relation: String
    url: Uri


@dataclass
class Bundle_Entry:
    id: String
    extension: Extension
    modifier_extension: Extension
    link: Bundle_Link
    full_url: Uri
    resource: ContainedResource
    search: Bundle_Entry_Search
    request: Bundle_Entry_Request
    response: Bundle_Entry_Response


@dataclass
class Bundle_Entry_Search:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: SearchEntryModeCode
    score: Decimal


@dataclass
class Bundle_Entry_Request:
    id: String
    extension: Extension
    modifier_extension: Extension
    method: HTTPVerbCode
    url: Uri
    if_none_match: String
    if_modified_since: Instant
    if_match: String
    if_none_exist: String


@dataclass
class Bundle_Entry_Response:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: String
    location: Uri
    etag: String
    last_modified: Instant
    outcome: ContainedResource


@dataclass
class CapabilityStatement:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    kind: CapabilityStatementKindCode
    instantiates: Uri
    software: CapabilityStatement_Software
    implementation: CapabilityStatement_Implementation
    fhir_version: Id
    accept_unknown: UnknownContentCodeCode
    format: MimeTypeCode
    patch_format: MimeTypeCode
    implementation_guide: Uri
    profile: Reference
    rest: CapabilityStatement_Rest
    messaging: CapabilityStatement_Messaging
    document: CapabilityStatement_Document


@dataclass
class CapabilityStatement_Software:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    version: String
    release_date: DateTime


@dataclass
class CapabilityStatement_Implementation:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    url: Uri


@dataclass
class CapabilityStatement_Rest:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: RestfulCapabilityModeCode
    documentation: String
    security: CapabilityStatement_Rest_Security
    resource: CapabilityStatement_Rest_Resource
    interaction: CapabilityStatement_Rest_SystemInteraction
    search_param: CapabilityStatement_Rest_Resource_SearchParam
    operation: CapabilityStatement_Rest_Operation
    compartment: Uri


@dataclass
class CapabilityStatement_Rest_Security:
    id: String
    extension: Extension
    modifier_extension: Extension
    cors: Boolean
    service: CodeableConcept
    description: String
    certificate: CapabilityStatement_Rest_Security_Certificate


@dataclass
class CapabilityStatement_Rest_Security_Certificate:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: MimeTypeCode
    blob: Base64Binary


@dataclass
class CapabilityStatement_Rest_Resource:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ResourceTypeCode
    profile: Reference
    documentation: Markdown
    interaction: CapabilityStatement_Rest_Resource_ResourceInteraction
    versioning: ResourceVersionPolicyCode
    read_history: Boolean
    update_create: Boolean
    conditional_create: Boolean
    conditional_read: ConditionalReadStatusCode
    conditional_update: Boolean
    conditional_delete: ConditionalDeleteStatusCode
    reference_policy: ReferenceHandlingPolicyCode
    search_include: String
    search_rev_include: String
    search_param: CapabilityStatement_Rest_Resource_SearchParam


@dataclass
class CapabilityStatement_Rest_Resource_ResourceInteraction:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: TypeRestfulInteractionCode
    documentation: String


@dataclass
class CapabilityStatement_Rest_Resource_SearchParam:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    definition: Uri
    type: SearchParamTypeCode
    documentation: String


@dataclass
class CapabilityStatement_Rest_SystemInteraction:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: SystemRestfulInteractionCode
    documentation: String


@dataclass
class CapabilityStatement_Rest_Operation:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    definition: Reference


@dataclass
class CapabilityStatement_Messaging:
    id: String
    extension: Extension
    modifier_extension: Extension
    endpoint: CapabilityStatement_Messaging_Endpoint
    reliable_cache: UnsignedInt
    documentation: String
    supported_message: CapabilityStatement_Messaging_SupportedMessage
    event: CapabilityStatement_Messaging_Event


@dataclass
class CapabilityStatement_Messaging_Endpoint:
    id: String
    extension: Extension
    modifier_extension: Extension
    protocol: Coding
    address: Uri


@dataclass
class CapabilityStatement_Messaging_SupportedMessage:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: EventCapabilityModeCode
    definition: Reference


@dataclass
class CapabilityStatement_Messaging_Event:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Coding
    category: MessageSignificanceCategoryCode
    mode: EventCapabilityModeCode
    focus: ResourceTypeCode
    request: Reference
    response: Reference
    documentation: String


@dataclass
class CapabilityStatement_Document:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: DocumentModeCode
    documentation: String
    profile: Reference


@dataclass
class CarePlan:
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
    activity: CarePlan_Activity
    note: Annotation


@dataclass
class CarePlan_Activity:
    id: String
    extension: Extension
    modifier_extension: Extension
    outcome_codeable_concept: CodeableConcept
    outcome_reference: Reference
    progress: Annotation
    reference: Reference
    detail: CarePlan_Activity_Detail


@dataclass
class CarePlan_Activity_Detail:
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
    scheduled: CarePlan_Activity_Detail_Scheduled
    location: Reference
    performer: Reference
    product: CarePlan_Activity_Detail_Product
    daily_amount: SimpleQuantity
    quantity: SimpleQuantity
    description: String


@dataclass
class CarePlan_Activity_Detail_Scheduled:
    timing: Timing
    period: Period
    string_value: String


@dataclass
class CarePlan_Activity_Detail_Product:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class CareTeam:
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
    participant: CareTeam_Participant
    reason_code: CodeableConcept
    reason_reference: Reference
    managing_organization: Reference
    note: Annotation


@dataclass
class CareTeam_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    member: Reference
    on_behalf_of: Reference
    period: Period


@dataclass
class ChargeItem:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition: Uri
    status: ChargeItemStatusCode
    part_of: Reference
    code: CodeableConcept
    subject: Reference
    context: Reference
    occurrence: ChargeItem_Occurrence
    participant: ChargeItem_Participant
    performing_organization: Reference
    requesting_organization: Reference
    quantity: Quantity
    bodysite: CodeableConcept
    factor_override: Decimal
    price_override: Money
    override_reason: String
    enterer: Reference
    entered_date: DateTime
    reason: CodeableConcept
    service: Reference
    account: Reference
    note: Annotation
    supporting_information: Reference


@dataclass
class ChargeItem_Occurrence:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class ChargeItem_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class Claim:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    type: CodeableConcept
    sub_type: CodeableConcept
    use: UseCode
    patient: Reference
    billable_period: Period
    created: DateTime
    enterer: Reference
    insurer: Reference
    provider: Reference
    organization: Reference
    priority: CodeableConcept
    funds_reserve: CodeableConcept
    related: Claim_RelatedClaim
    prescription: Reference
    original_prescription: Reference
    payee: Claim_Payee
    referral: Reference
    facility: Reference
    care_team: Claim_CareTeam
    information: Claim_SpecialCondition
    diagnosis: Claim_Diagnosis
    procedure: Claim_Procedure
    insurance: Claim_Insurance
    accident: Claim_Accident
    employment_impacted: Period
    hospitalization: Period
    item: Claim_Item
    total: Money


@dataclass
class Claim_RelatedClaim:
    id: String
    extension: Extension
    modifier_extension: Extension
    claim: Reference
    relationship: CodeableConcept
    reference: Identifier


@dataclass
class Claim_Payee:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    resource_type: Coding
    party: Reference


@dataclass
class Claim_CareTeam:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    provider: Reference
    responsible: Boolean
    role: CodeableConcept
    qualification: CodeableConcept


@dataclass
class Claim_SpecialCondition:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    category: CodeableConcept
    code: CodeableConcept
    timing: Claim_SpecialCondition_TimingType
    value: Claim_SpecialCondition_Value
    reason: CodeableConcept


@dataclass
class Claim_SpecialCondition_TimingType:
    date: Date
    period: Period


@dataclass
class Claim_SpecialCondition_Value:
    string_value: String
    quantity: Quantity
    attachment: Attachment
    reference: Reference


@dataclass
class Claim_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    diagnosis: Claim_Diagnosis_DiagnosisType
    type: CodeableConcept
    package_code: CodeableConcept


@dataclass
class Claim_Diagnosis_DiagnosisType:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Claim_Procedure:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    date: DateTime
    procedure: Claim_Procedure_ProcedureType


@dataclass
class Claim_Procedure_ProcedureType:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Claim_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    focal: Boolean
    coverage: Reference
    business_arrangement: String
    pre_auth_ref: String
    claim_response: Reference


@dataclass
class Claim_Accident:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: Date
    type: CodeableConcept
    location: Claim_Accident_Location


@dataclass
class Claim_Accident_Location:
    address: Address
    reference: Reference


@dataclass
class Claim_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    care_team_link_id: PositiveInt
    diagnosis_link_id: PositiveInt
    procedure_link_id: PositiveInt
    information_link_id: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    serviced: Claim_Item_Serviced
    location: Claim_Item_Location
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    body_site: CodeableConcept
    sub_site: CodeableConcept
    encounter: Reference
    detail: Claim_Item_Detail


@dataclass
class Claim_Item_Serviced:
    date: Date
    period: Period


@dataclass
class Claim_Item_Location:
    codeable_concept: CodeableConcept
    address: Address
    reference: Reference


@dataclass
class Claim_Item_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    sub_detail: Claim_Item_Detail_SubDetail


@dataclass
class Claim_Item_Detail_SubDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference


@dataclass
class ClaimResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    patient: Reference
    created: DateTime
    insurer: Reference
    request_provider: Reference
    request_organization: Reference
    request: Reference
    outcome: CodeableConcept
    disposition: String
    payee_type: CodeableConcept
    item: ClaimResponse_Item
    add_item: ClaimResponse_AddedItem
    error: ClaimResponse_Error
    total_cost: Money
    unalloc_deductable: Money
    total_benefit: Money
    payment: ClaimResponse_Payment
    reserved: Coding
    form: CodeableConcept
    process_note: ClaimResponse_Note
    communication_request: Reference
    insurance: ClaimResponse_Insurance


@dataclass
class ClaimResponse_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence_link_id: PositiveInt
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication
    detail: ClaimResponse_Item_ItemDetail


@dataclass
class ClaimResponse_Item_Adjudication:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    reason: CodeableConcept
    amount: Money
    value: Decimal


@dataclass
class ClaimResponse_Item_ItemDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence_link_id: PositiveInt
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication
    sub_detail: ClaimResponse_Item_ItemDetail_SubDetail


@dataclass
class ClaimResponse_Item_ItemDetail_SubDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence_link_id: PositiveInt
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication


@dataclass
class ClaimResponse_AddedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence_link_id: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    fee: Money
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication
    detail: ClaimResponse_AddedItem_AddedItemsDetail


@dataclass
class ClaimResponse_AddedItem_AddedItemsDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    fee: Money
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication


@dataclass
class ClaimResponse_Error:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence_link_id: PositiveInt
    detail_sequence_link_id: PositiveInt
    subdetail_sequence_link_id: PositiveInt
    code: CodeableConcept


@dataclass
class ClaimResponse_Payment:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    adjustment: Money
    adjustment_reason: CodeableConcept
    date: Date
    amount: Money
    identifier: Identifier


@dataclass
class ClaimResponse_Note:
    id: String
    extension: Extension
    modifier_extension: Extension
    number: PositiveInt
    type: CodeableConcept
    text: String
    language: CodeableConcept


@dataclass
class ClaimResponse_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    focal: Boolean
    coverage: Reference
    business_arrangement: String
    pre_auth_ref: String
    claim_response: Reference


@dataclass
class ClinicalImpression:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ClinicalImpressionStatusCode
    code: CodeableConcept
    description: String
    subject: Reference
    context: Reference
    effective: ClinicalImpression_Effective
    date: DateTime
    assessor: Reference
    previous: Reference
    problem: Reference
    investigation: ClinicalImpression_Investigation
    protocol: Uri
    summary: String
    finding: ClinicalImpression_Finding
    prognosis_codeable_concept: CodeableConcept
    prognosis_reference: Reference
    action: Reference
    note: Annotation


@dataclass
class ClinicalImpression_Effective:
    date_time: DateTime
    period: Period


@dataclass
class ClinicalImpression_Investigation:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    item: Reference


@dataclass
class ClinicalImpression_Finding:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: ClinicalImpression_Finding_Item
    basis: String


@dataclass
class ClinicalImpression_Finding_Item:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class CodeSystem:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    case_sensitive: Boolean
    value_set: Uri
    hierarchy_meaning: CodeSystemHierarchyMeaningCode
    compositional: Boolean
    version_needed: Boolean
    content: CodeSystemContentModeCode
    count: UnsignedInt
    filter: CodeSystem_Filter
    property: CodeSystem_Property
    concept: CodeSystem_ConceptDefinition


@dataclass
class CodeSystem_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    description: String
    operator: FilterOperatorCode
    value: String


@dataclass
class CodeSystem_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    uri: Uri
    description: String
    type: PropertyTypeCode


@dataclass
class CodeSystem_ConceptDefinition:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    definition: String
    designation: CodeSystem_ConceptDefinition_Designation
    property: CodeSystem_ConceptDefinition_ConceptProperty
    concept: CodeSystem_ConceptDefinition


@dataclass
class CodeSystem_ConceptDefinition_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: LanguageCode
    use: Coding
    value: String


@dataclass
class CodeSystem_ConceptDefinition_ConceptProperty:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    value: CodeSystem_ConceptDefinition_ConceptProperty_Value


@dataclass
class CodeSystem_ConceptDefinition_ConceptProperty_Value:
    code: Code
    coding: Coding
    string_value: String
    integer: Integer
    boolean: Boolean
    date_time: DateTime


@dataclass
class Communication:
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
    medium: CodeableConcept
    subject: Reference
    recipient: Reference
    topic: Reference
    context: Reference
    sent: DateTime
    received: DateTime
    sender: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    payload: Communication_Payload
    note: Annotation


@dataclass
class Communication_Payload:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Communication_Payload_Content


@dataclass
class Communication_Payload_Content:
    string_value: String
    attachment: Attachment
    reference: Reference


@dataclass
class CommunicationRequest:
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
    replaces: Reference
    group_identifier: Identifier
    status: RequestStatusCode
    category: CodeableConcept
    priority: RequestPriorityCode
    medium: CodeableConcept
    subject: Reference
    recipient: Reference
    topic: Reference
    context: Reference
    payload: CommunicationRequest_Payload
    occurrence: CommunicationRequest_Occurrence
    authored_on: DateTime
    sender: Reference
    requester: CommunicationRequest_Requester
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation


@dataclass
class CommunicationRequest_Payload:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: CommunicationRequest_Payload_Content


@dataclass
class CommunicationRequest_Payload_Content:
    string_value: String
    attachment: Attachment
    reference: Reference


@dataclass
class CommunicationRequest_Occurrence:
    date_time: DateTime
    period: Period


@dataclass
class CommunicationRequest_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class CompartmentDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    purpose: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    code: CompartmentTypeCode
    search: Boolean
    resource: CompartmentDefinition_Resource


@dataclass
class CompartmentDefinition_Resource:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: ResourceTypeCode
    param: String
    documentation: String


@dataclass
class Composition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: CompositionStatusCode
    type: CodeableConcept
    class_value: CodeableConcept
    subject: Reference
    encounter: Reference
    date: DateTime
    author: Reference
    title: String
    confidentiality: ConfidentialityClassificationCode
    attester: Composition_Attester
    custodian: Reference
    relates_to: Composition_RelatesTo
    event: Composition_Event
    section: Composition_Section


@dataclass
class Composition_Attester:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: CompositionAttestationModeCode
    time: DateTime
    party: Reference


@dataclass
class Composition_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: DocumentRelationshipTypeCode
    target: Composition_RelatesTo_Target


@dataclass
class Composition_RelatesTo_Target:
    identifier: Identifier
    reference: Reference


@dataclass
class Composition_Event:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    period: Period
    detail: Reference


@dataclass
class Composition_Section:
    id: String
    extension: Extension
    modifier_extension: Extension
    title: String
    code: CodeableConcept
    text: Narrative
    mode: ListModeCode
    ordered_by: CodeableConcept
    entry: Reference
    empty_reason: CodeableConcept
    section: Composition_Section


@dataclass
class ConceptMap:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    source: ConceptMap_Source
    target: ConceptMap_Target
    group: ConceptMap_Group


@dataclass
class ConceptMap_Source:
    uri: Uri
    reference: Reference


@dataclass
class ConceptMap_Target:
    uri: Uri
    reference: Reference


@dataclass
class ConceptMap_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    source: Uri
    source_version: String
    target: Uri
    target_version: String
    element: ConceptMap_Group_SourceElement
    unmapped: ConceptMap_Group_Unmapped


@dataclass
class ConceptMap_Group_SourceElement:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    target: ConceptMap_Group_SourceElement_TargetElement


@dataclass
class ConceptMap_Group_SourceElement_TargetElement:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    equivalence: ConceptMapEquivalenceCode
    comment: String
    depends_on: ConceptMap_Group_SourceElement_TargetElement_OtherElement
    product: ConceptMap_Group_SourceElement_TargetElement_OtherElement


@dataclass
class ConceptMap_Group_SourceElement_TargetElement_OtherElement:
    id: String
    extension: Extension
    modifier_extension: Extension
    property: Uri
    system: Uri
    code: String
    display: String


@dataclass
class ConceptMap_Group_Unmapped:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: ConceptMapGroupUnmappedModeCode
    code: Code
    display: String
    url: Uri


@dataclass
class Condition:
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
    onset: Condition_Onset
    abatement: Condition_Abatement
    asserted_date: DateTime
    asserter: Reference
    stage: Condition_Stage
    evidence: Condition_Evidence
    note: Annotation


@dataclass
class Condition_Onset:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class Condition_Abatement:
    date_time: DateTime
    age: Age
    boolean: Boolean
    period: Period
    range: Range
    string_value: String


@dataclass
class Condition_Stage:
    id: String
    extension: Extension
    modifier_extension: Extension
    summary: CodeableConcept
    assessment: Reference


@dataclass
class Condition_Evidence:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    detail: Reference


@dataclass
class Consent:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ConsentStateCode
    category: CodeableConcept
    patient: Reference
    period: Period
    date_time: DateTime
    consenting_party: Reference
    actor: Consent_Actor
    action: CodeableConcept
    organization: Reference
    source: Consent_Source
    policy: Consent_Policy
    policy_rule: Uri
    security_label: Coding
    purpose: Coding
    data_period: Period
    data: Consent_Data
    except: Consent_Except


@dataclass
class Consent_Actor:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    reference: Reference


@dataclass
class Consent_Source:
    attachment: Attachment
    identifier: Identifier
    reference: Reference


@dataclass
class Consent_Policy:
    id: String
    extension: Extension
    modifier_extension: Extension
    authority: Uri
    uri: Uri


@dataclass
class Consent_Data:
    id: String
    extension: Extension
    modifier_extension: Extension
    meaning: ConsentDataMeaningCode
    reference: Reference


@dataclass
class Consent_Except:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ConsentExceptTypeCode
    period: Period
    actor: Consent_Except_ExceptActor
    action: CodeableConcept
    security_label: Coding
    purpose: Coding
    class_value: Coding
    code: Coding
    data_period: Period
    data: Consent_Except_ExceptData


@dataclass
class Consent_Except_ExceptActor:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    reference: Reference


@dataclass
class Consent_Except_ExceptData:
    id: String
    extension: Extension
    modifier_extension: Extension
    meaning: ConsentDataMeaningCode
    reference: Reference


@dataclass
class Contract:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ContractResourceStatusCode
    issued: DateTime
    applies: Period
    subject: Reference
    topic: Reference
    authority: Reference
    domain: Reference
    type: CodeableConcept
    sub_type: CodeableConcept
    action: CodeableConcept
    action_reason: CodeableConcept
    decision_type: CodeableConcept
    content_derivative: CodeableConcept
    security_label: Coding
    agent: Contract_Agent
    signer: Contract_Signatory
    valued_item: Contract_ValuedItem
    term: Contract_Term
    binding: Contract_Binding
    friendly: Contract_FriendlyLanguage
    legal: Contract_LegalLanguage
    rule: Contract_ComputableLanguage


@dataclass
class Contract_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    actor: Reference
    role: CodeableConcept


@dataclass
class Contract_Signatory:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Coding
    party: Reference
    signature: Signature


@dataclass
class Contract_ValuedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    entity: Contract_ValuedItem_Entity
    identifier: Identifier
    effective_time: DateTime
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    points: Decimal
    net: Money


@dataclass
class Contract_ValuedItem_Entity:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Contract_Term:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    issued: DateTime
    applies: Period
    type: CodeableConcept
    sub_type: CodeableConcept
    topic: Reference
    action: CodeableConcept
    action_reason: CodeableConcept
    security_label: Coding
    agent: Contract_Term_TermAgent
    text: String
    valued_item: Contract_Term_TermValuedItem
    group: Contract_Term


@dataclass
class Contract_Term_TermAgent:
    id: String
    extension: Extension
    modifier_extension: Extension
    actor: Reference
    role: CodeableConcept


@dataclass
class Contract_Term_TermValuedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    entity: Contract_Term_TermValuedItem_Entity
    identifier: Identifier
    effective_time: DateTime
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    points: Decimal
    net: Money


@dataclass
class Contract_Term_TermValuedItem_Entity:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Contract_Binding:
    attachment: Attachment
    reference: Reference


@dataclass
class Contract_FriendlyLanguage:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Contract_FriendlyLanguage_Content


@dataclass
class Contract_FriendlyLanguage_Content:
    attachment: Attachment
    reference: Reference


@dataclass
class Contract_LegalLanguage:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Contract_LegalLanguage_Content


@dataclass
class Contract_LegalLanguage_Content:
    attachment: Attachment
    reference: Reference


@dataclass
class Contract_ComputableLanguage:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Contract_ComputableLanguage_Content


@dataclass
class Contract_ComputableLanguage_Content:
    attachment: Attachment
    reference: Reference


@dataclass
class Coverage:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    type: CodeableConcept
    policy_holder: Reference
    subscriber: Reference
    subscriber_id: String
    beneficiary: Reference
    relationship: CodeableConcept
    period: Period
    payor: Reference
    grouping: Coverage_Group
    dependent: String
    sequence: String
    order: PositiveInt
    network: String
    contract: Reference


@dataclass
class Coverage_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    group: String
    group_display: String
    sub_group: String
    sub_group_display: String
    plan: String
    plan_display: String
    sub_plan: String
    sub_plan_display: String
    class_value: String
    class_display: String
    sub_class: String
    sub_class_display: String


@dataclass
class DataElement:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    name: String
    title: String
    contact: ContactDetail
    use_context: UsageContext
    jurisdiction: CodeableConcept
    copyright: Markdown
    stringency: DataElementStringencyCode
    mapping: DataElement_Mapping
    element: ElementDefinition


@dataclass
class DataElement_Mapping:
    id: String
    extension: Extension
    modifier_extension: Extension
    identity: Id
    uri: Uri
    name: String
    comment: String


@dataclass
class DetectedIssue:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ObservationStatusCode
    category: CodeableConcept
    severity: DetectedIssueSeverityCode
    patient: Reference
    date: DateTime
    author: Reference
    implicated: Reference
    detail: String
    reference: Uri
    mitigation: DetectedIssue_Mitigation


@dataclass
class DetectedIssue_Mitigation:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: CodeableConcept
    date: DateTime
    author: Reference


@dataclass
class Device:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    udi: Device_Udi
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
class Device_Udi:
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
class DeviceComponent:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    last_system_change: Instant
    source: Reference
    parent: Reference
    operational_status: CodeableConcept
    parameter_group: CodeableConcept
    measurement_principle: MeasmntPrincipleCode
    production_specification: DeviceComponent_ProductionSpecification
    language_code: CodeableConcept


@dataclass
class DeviceComponent_ProductionSpecification:
    id: String
    extension: Extension
    modifier_extension: Extension
    spec_type: CodeableConcept
    component_id: Identifier
    production_spec: String


@dataclass
class DeviceMetric:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    unit: CodeableConcept
    source: Reference
    parent: Reference
    operational_status: DeviceMetricOperationalStatusCode
    color: DeviceMetricColorCode
    category: DeviceMetricCategoryCode
    measurement_period: Timing
    calibration: DeviceMetric_Calibration


@dataclass
class DeviceMetric_Calibration:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: DeviceMetricCalibrationTypeCode
    state: DeviceMetricCalibrationStateCode
    time: Instant


@dataclass
class DeviceRequest:
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
    prior_request: Reference
    group_identifier: Identifier
    status: RequestStatusCode
    intent: CodeableConcept
    priority: RequestPriorityCode
    code: DeviceRequest_Code
    subject: Reference
    context: Reference
    occurrence: DeviceRequest_Occurrence
    authored_on: DateTime
    requester: DeviceRequest_Requester
    performer_type: CodeableConcept
    performer: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    supporting_info: Reference
    note: Annotation
    relevant_history: Reference


@dataclass
class DeviceRequest_Code:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class DeviceRequest_Occurrence:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class DeviceRequest_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class DeviceUseStatement:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: DeviceUseStatementStatusCode
    subject: Reference
    when_used: Period
    timing: DeviceUseStatement_TimingType
    recorded_on: DateTime
    source: Reference
    device: Reference
    indication: CodeableConcept
    body_site: CodeableConcept
    note: Annotation


@dataclass
class DeviceUseStatement_TimingType:
    timing_value: Timing
    period: Period
    date_time: DateTime


@dataclass
class DiagnosticReport:
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
    effective: DiagnosticReport_Effective
    issued: Instant
    performer: DiagnosticReport_Performer
    specimen: Reference
    result: Reference
    imaging_study: Reference
    image: DiagnosticReport_Image
    conclusion: String
    coded_diagnosis: CodeableConcept
    presented_form: Attachment


@dataclass
class DiagnosticReport_Effective:
    date_time: DateTime
    period: Period


@dataclass
class DiagnosticReport_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class DiagnosticReport_Image:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference


@dataclass
class DocumentManifest:
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
    type: CodeableConcept
    subject: Reference
    created: DateTime
    author: Reference
    recipient: Reference
    source: Uri
    description: String
    content: DocumentManifest_Content
    related: DocumentManifest_Related


@dataclass
class DocumentManifest_Content:
    id: String
    extension: Extension
    modifier_extension: Extension
    p: DocumentManifest_Content_P


@dataclass
class DocumentManifest_Content_P:
    attachment: Attachment
    reference: Reference


@dataclass
class DocumentManifest_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    ref: Reference


@dataclass
class DocumentReference:
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
    relates_to: DocumentReference_RelatesTo
    description: String
    security_label: CodeableConcept
    content: DocumentReference_Content
    context: DocumentReference_Context


@dataclass
class DocumentReference_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: DocumentRelationshipTypeCode
    target: Reference


@dataclass
class DocumentReference_Content:
    id: String
    extension: Extension
    modifier_extension: Extension
    attachment: Attachment
    format: Coding


@dataclass
class DocumentReference_Context:
    id: String
    extension: Extension
    modifier_extension: Extension
    encounter: Reference
    event: CodeableConcept
    period: Period
    facility_type: CodeableConcept
    practice_setting: CodeableConcept
    source_patient_info: Reference
    related: DocumentReference_Context_Related


@dataclass
class DocumentReference_Context_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    ref: Reference


@dataclass
class EligibilityRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    priority: CodeableConcept
    patient: Reference
    serviced: EligibilityRequest_Serviced
    created: DateTime
    enterer: Reference
    provider: Reference
    organization: Reference
    insurer: Reference
    facility: Reference
    coverage: Reference
    business_arrangement: String
    benefit_category: CodeableConcept
    benefit_sub_category: CodeableConcept


@dataclass
class EligibilityRequest_Serviced:
    date: Date
    period: Period


@dataclass
class EligibilityResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    created: DateTime
    request_provider: Reference
    request_organization: Reference
    request: Reference
    outcome: CodeableConcept
    disposition: String
    insurer: Reference
    inforce: Boolean
    insurance: EligibilityResponse_Insurance
    form: CodeableConcept
    error: EligibilityResponse_Errors


@dataclass
class EligibilityResponse_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    coverage: Reference
    contract: Reference
    benefit_balance: EligibilityResponse_Insurance_Benefits


@dataclass
class EligibilityResponse_Insurance_Benefits:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    sub_category: CodeableConcept
    excluded: Boolean
    name: String
    description: String
    network: CodeableConcept
    unit: CodeableConcept
    term: CodeableConcept
    financial: EligibilityResponse_Insurance_Benefits_Benefit


@dataclass
class EligibilityResponse_Insurance_Benefits_Benefit:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    allowed: EligibilityResponse_Insurance_Benefits_Benefit_Allowed
    used: EligibilityResponse_Insurance_Benefits_Benefit_Used


@dataclass
class EligibilityResponse_Insurance_Benefits_Benefit_Allowed:
    unsigned_int: UnsignedInt
    string_value: String
    money: Money


@dataclass
class EligibilityResponse_Insurance_Benefits_Benefit_Used:
    unsigned_int: UnsignedInt
    money: Money


@dataclass
class EligibilityResponse_Errors:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept


@dataclass
class Encounter:
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
    status_history: Encounter_StatusHistory
    class_value: Coding
    class_history: Encounter_ClassHistory
    type: CodeableConcept
    priority: CodeableConcept
    subject: Reference
    episode_of_care: Reference
    incoming_referral: Reference
    participant: Encounter_Participant
    appointment: Reference
    period: Period
    length: Duration
    reason: CodeableConcept
    diagnosis: Encounter_Diagnosis
    account: Reference
    hospitalization: Encounter_Hospitalization
    location: Encounter_Location
    service_provider: Reference
    part_of: Reference


@dataclass
class Encounter_StatusHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: EncounterStatusCode
    period: Period


@dataclass
class Encounter_ClassHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    class_value: Coding
    period: Period


@dataclass
class Encounter_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    period: Period
    individual: Reference


@dataclass
class Encounter_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    condition: Reference
    role: CodeableConcept
    rank: PositiveInt


@dataclass
class Encounter_Hospitalization:
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
class Encounter_Location:
    id: String
    extension: Extension
    modifier_extension: Extension
    location: Reference
    status: EncounterLocationStatusCode
    period: Period


@dataclass
class Endpoint:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: EndpointStatusCode
    connection_type: Coding
    name: String
    managing_organization: Reference
    contact: ContactPoint
    period: Period
    payload_type: CodeableConcept
    payload_mime_type: MimeTypeCode
    address: Uri
    header: String


@dataclass
class EnrollmentRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    created: DateTime
    insurer: Reference
    provider: Reference
    organization: Reference
    subject: Reference
    coverage: Reference


@dataclass
class EnrollmentResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    request: Reference
    outcome: CodeableConcept
    disposition: String
    created: DateTime
    organization: Reference
    request_provider: Reference
    request_organization: Reference


@dataclass
class EpisodeOfCare:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: EpisodeOfCareStatusCode
    status_history: EpisodeOfCare_StatusHistory
    type: CodeableConcept
    diagnosis: EpisodeOfCare_Diagnosis
    patient: Reference
    managing_organization: Reference
    period: Period
    referral_request: Reference
    care_manager: Reference
    team: Reference
    account: Reference


@dataclass
class EpisodeOfCare_StatusHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: EpisodeOfCareStatusCode
    period: Period


@dataclass
class EpisodeOfCare_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    condition: Reference
    role: CodeableConcept
    rank: PositiveInt


@dataclass
class ExpansionProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    fixed_version: ExpansionProfile_FixedVersion
    excluded_system: ExpansionProfile_ExcludedSystem
    include_designations: Boolean
    designation: ExpansionProfile_Designation
    include_definition: Boolean
    active_only: Boolean
    exclude_nested: Boolean
    exclude_not_for_ui: Boolean
    exclude_post_coordinated: Boolean
    display_language: LanguageCode
    limited_expansion: Boolean


@dataclass
class ExpansionProfile_FixedVersion:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    version: String
    mode: SystemVersionProcessingModeCode


@dataclass
class ExpansionProfile_ExcludedSystem:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    version: String


@dataclass
class ExpansionProfile_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    include: ExpansionProfile_Designation_DesignationInclude
    exclude: ExpansionProfile_Designation_DesignationExclude


@dataclass
class ExpansionProfile_Designation_DesignationInclude:
    id: String
    extension: Extension
    modifier_extension: Extension
    designation: ExpansionProfile_Designation_DesignationInclude_DesignationIncludeDesignation


@dataclass
class ExpansionProfile_Designation_DesignationInclude_DesignationIncludeDesignation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: LanguageCode
    use: Coding


@dataclass
class ExpansionProfile_Designation_DesignationExclude:
    id: String
    extension: Extension
    modifier_extension: Extension
    designation: ExpansionProfile_Designation_DesignationExclude_DesignationExcludeDesignation


@dataclass
class ExpansionProfile_Designation_DesignationExclude_DesignationExcludeDesignation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: LanguageCode
    use: Coding


@dataclass
class ExplanationOfBenefit:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ExplanationOfBenefitStatusCode
    type: CodeableConcept
    sub_type: CodeableConcept
    patient: Reference
    billable_period: Period
    created: DateTime
    enterer: Reference
    insurer: Reference
    provider: Reference
    organization: Reference
    referral: Reference
    facility: Reference
    claim: Reference
    claim_response: Reference
    outcome: CodeableConcept
    disposition: String
    related: ExplanationOfBenefit_RelatedClaim
    prescription: Reference
    original_prescription: Reference
    payee: ExplanationOfBenefit_Payee
    information: ExplanationOfBenefit_SupportingInformation
    care_team: ExplanationOfBenefit_CareTeam
    diagnosis: ExplanationOfBenefit_Diagnosis
    procedure: ExplanationOfBenefit_Procedure
    precedence: PositiveInt
    insurance: ExplanationOfBenefit_Insurance
    accident: ExplanationOfBenefit_Accident
    employment_impacted: Period
    hospitalization: Period
    item: ExplanationOfBenefit_Item
    add_item: ExplanationOfBenefit_AddedItem
    total_cost: Money
    unalloc_deductable: Money
    total_benefit: Money
    payment: ExplanationOfBenefit_Payment
    form: CodeableConcept
    process_note: ExplanationOfBenefit_Note
    benefit_balance: ExplanationOfBenefit_BenefitBalance


@dataclass
class ExplanationOfBenefit_RelatedClaim:
    id: String
    extension: Extension
    modifier_extension: Extension
    claim: Reference
    relationship: CodeableConcept
    reference: Identifier


@dataclass
class ExplanationOfBenefit_Payee:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    resource_type: CodeableConcept
    party: Reference


@dataclass
class ExplanationOfBenefit_SupportingInformation:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    category: CodeableConcept
    code: CodeableConcept
    timing: ExplanationOfBenefit_SupportingInformation_TimingType
    value: ExplanationOfBenefit_SupportingInformation_Value
    reason: Coding


@dataclass
class ExplanationOfBenefit_SupportingInformation_TimingType:
    date: Date
    period: Period


@dataclass
class ExplanationOfBenefit_SupportingInformation_Value:
    string_value: String
    quantity: Quantity
    attachment: Attachment
    reference: Reference


@dataclass
class ExplanationOfBenefit_CareTeam:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    provider: Reference
    responsible: Boolean
    role: CodeableConcept
    qualification: CodeableConcept


@dataclass
class ExplanationOfBenefit_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    diagnosis: ExplanationOfBenefit_Diagnosis_DiagnosisType
    type: CodeableConcept
    package_code: CodeableConcept


@dataclass
class ExplanationOfBenefit_Diagnosis_DiagnosisType:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ExplanationOfBenefit_Procedure:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    date: DateTime
    procedure: ExplanationOfBenefit_Procedure_ProcedureType


@dataclass
class ExplanationOfBenefit_Procedure_ProcedureType:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ExplanationOfBenefit_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    coverage: Reference
    pre_auth_ref: String


@dataclass
class ExplanationOfBenefit_Accident:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: Date
    type: CodeableConcept
    location: ExplanationOfBenefit_Accident_Location


@dataclass
class ExplanationOfBenefit_Accident_Location:
    address: Address
    reference: Reference


@dataclass
class ExplanationOfBenefit_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    care_team_link_id: PositiveInt
    diagnosis_link_id: PositiveInt
    procedure_link_id: PositiveInt
    information_link_id: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    serviced: ExplanationOfBenefit_Item_Serviced
    location: ExplanationOfBenefit_Item_Location
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    body_site: CodeableConcept
    sub_site: CodeableConcept
    encounter: Reference
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication
    detail: ExplanationOfBenefit_Item_Detail


@dataclass
class ExplanationOfBenefit_Item_Serviced:
    date: Date
    period: Period


@dataclass
class ExplanationOfBenefit_Item_Location:
    codeable_concept: CodeableConcept
    address: Address
    reference: Reference


@dataclass
class ExplanationOfBenefit_Item_Adjudication:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    reason: CodeableConcept
    amount: Money
    value: Decimal


@dataclass
class ExplanationOfBenefit_Item_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    type: CodeableConcept
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication
    sub_detail: ExplanationOfBenefit_Item_Detail_SubDetail


@dataclass
class ExplanationOfBenefit_Item_Detail_SubDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    type: CodeableConcept
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication


@dataclass
class ExplanationOfBenefit_AddedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence_link_id: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    fee: Money
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication
    detail: ExplanationOfBenefit_AddedItem_AddedItemsDetail


@dataclass
class ExplanationOfBenefit_AddedItem_AddedItemsDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    revenue: CodeableConcept
    category: CodeableConcept
    service: CodeableConcept
    modifier: CodeableConcept
    fee: Money
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication


@dataclass
class ExplanationOfBenefit_Payment:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    adjustment: Money
    adjustment_reason: CodeableConcept
    date: Date
    amount: Money
    identifier: Identifier


@dataclass
class ExplanationOfBenefit_Note:
    id: String
    extension: Extension
    modifier_extension: Extension
    number: PositiveInt
    type: CodeableConcept
    text: String
    language: CodeableConcept


@dataclass
class ExplanationOfBenefit_BenefitBalance:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    sub_category: CodeableConcept
    excluded: Boolean
    name: String
    description: String
    network: CodeableConcept
    unit: CodeableConcept
    term: CodeableConcept
    financial: ExplanationOfBenefit_BenefitBalance_Benefit


@dataclass
class ExplanationOfBenefit_BenefitBalance_Benefit:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    allowed: ExplanationOfBenefit_BenefitBalance_Benefit_Allowed
    used: ExplanationOfBenefit_BenefitBalance_Benefit_Used


@dataclass
class ExplanationOfBenefit_BenefitBalance_Benefit_Allowed:
    unsigned_int: UnsignedInt
    string_value: String
    money: Money


@dataclass
class ExplanationOfBenefit_BenefitBalance_Benefit_Used:
    unsigned_int: UnsignedInt
    money: Money


@dataclass
class FamilyMemberHistory:
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
    status: FamilyHistoryStatusCode
    not_done: Boolean
    not_done_reason: CodeableConcept
    patient: Reference
    date: DateTime
    name: String
    relationship: CodeableConcept
    gender: AdministrativeGenderCode
    born: FamilyMemberHistory_Born
    age: FamilyMemberHistory_AgeType
    estimated_age: Boolean
    deceased: FamilyMemberHistory_Deceased
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    condition: FamilyMemberHistory_Condition


@dataclass
class FamilyMemberHistory_Born:
    period: Period
    date: Date
    string_value: String


@dataclass
class FamilyMemberHistory_AgeType:
    age_value: Age
    range: Range
    string_value: String


@dataclass
class FamilyMemberHistory_Deceased:
    boolean: Boolean
    age: Age
    range: Range
    date: Date
    string_value: String


@dataclass
class FamilyMemberHistory_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    outcome: CodeableConcept
    onset: FamilyMemberHistory_Condition_Onset
    note: Annotation


@dataclass
class FamilyMemberHistory_Condition_Onset:
    age: Age
    range: Range
    period: Period
    string_value: String


@dataclass
class Flag:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FlagStatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    period: Period
    encounter: Reference
    author: Reference


@dataclass
class Goal:
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
    start: Goal_Start
    target: Goal_Target
    status_date: Date
    status_reason: String
    expressed_by: Reference
    addresses: Reference
    note: Annotation
    outcome_code: CodeableConcept
    outcome_reference: Reference


@dataclass
class Goal_Start:
    date: Date
    codeable_concept: CodeableConcept


@dataclass
class Goal_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: Goal_Target_Detail
    due: Goal_Target_Due


@dataclass
class Goal_Target_Detail:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept


@dataclass
class Goal_Target_Due:
    date: Date
    duration: Duration


@dataclass
class GraphDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    version: String
    name: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    start: ResourceTypeCode
    profile: Uri
    link: GraphDefinition_Link


@dataclass
class GraphDefinition_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    slice_name: String
    min: Integer
    max: String
    description: String
    target: GraphDefinition_Link_Target


@dataclass
class GraphDefinition_Link_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ResourceTypeCode
    profile: Uri
    compartment: GraphDefinition_Link_Target_Compartment
    link: GraphDefinition_Link


@dataclass
class GraphDefinition_Link_Target_Compartment:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CompartmentTypeCode
    rule: GraphCompartmentRuleCode
    expression: String
    description: String


@dataclass
class Group:
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
    type: GroupTypeCode
    actual: Boolean
    code: CodeableConcept
    name: String
    quantity: UnsignedInt
    characteristic: Group_Characteristic
    member: Group_Member


@dataclass
class Group_Characteristic:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Group_Characteristic_Value
    exclude: Boolean
    period: Period


@dataclass
class Group_Characteristic_Value:
    codeable_concept: CodeableConcept
    boolean: Boolean
    quantity: Quantity
    range: Range


@dataclass
class Group_Member:
    id: String
    extension: Extension
    modifier_extension: Extension
    entity: Reference
    period: Period
    inactive: Boolean


@dataclass
class GuidanceResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    request_id: Id
    identifier: Identifier
    module: Reference
    status: GuidanceResponseStatusCode
    subject: Reference
    context: Reference
    occurrence_date_time: DateTime
    performer: Reference
    reason: GuidanceResponse_Reason
    note: Annotation
    evaluation_message: Reference
    output_parameters: Reference
    result: Reference
    data_requirement: DataRequirement


@dataclass
class GuidanceResponse_Reason:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class HealthcareService:
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
    provided_by: Reference
    category: CodeableConcept
    type: CodeableConcept
    specialty: CodeableConcept
    location: Reference
    name: String
    comment: String
    extra_details: String
    photo: Attachment
    telecom: ContactPoint
    coverage_area: Reference
    service_provision_code: CodeableConcept
    eligibility: CodeableConcept
    eligibility_note: String
    program_name: String
    characteristic: CodeableConcept
    referral_method: CodeableConcept
    appointment_required: Boolean
    available_time: HealthcareService_AvailableTime
    not_available: HealthcareService_NotAvailable
    availability_exceptions: String
    endpoint: Reference


@dataclass
class HealthcareService_AvailableTime:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: DaysOfWeekCode
    all_day: Boolean
    available_start_time: Time
    available_end_time: Time


@dataclass
class HealthcareService_NotAvailable:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    during: Period


@dataclass
class ImagingManifest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    patient: Reference
    authoring_time: DateTime
    author: Reference
    description: String
    study: ImagingManifest_Study


@dataclass
class ImagingManifest_Study:
    id: String
    extension: Extension
    modifier_extension: Extension
    uid: Oid
    imaging_study: Reference
    endpoint: Reference
    series: ImagingManifest_Study_Series


@dataclass
class ImagingManifest_Study_Series:
    id: String
    extension: Extension
    modifier_extension: Extension
    uid: Oid
    endpoint: Reference
    instance: ImagingManifest_Study_Series_Instance


@dataclass
class ImagingManifest_Study_Series_Instance:
    id: String
    extension: Extension
    modifier_extension: Extension
    sop_class: Oid
    uid: Oid


@dataclass
class ImagingStudy:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    uid: Oid
    accession: Identifier
    identifier: Identifier
    availability: InstanceAvailabilityCode
    modality_list: Coding
    patient: Reference
    context: Reference
    started: DateTime
    based_on: Reference
    referrer: Reference
    interpreter: Reference
    endpoint: Reference
    number_of_series: UnsignedInt
    number_of_instances: UnsignedInt
    procedure_reference: Reference
    procedure_code: CodeableConcept
    reason: CodeableConcept
    description: String
    series: ImagingStudy_Series


@dataclass
class ImagingStudy_Series:
    id: String
    extension: Extension
    modifier_extension: Extension
    uid: Oid
    number: UnsignedInt
    modality: Coding
    description: String
    number_of_instances: UnsignedInt
    availability: InstanceAvailabilityCode
    endpoint: Reference
    body_site: Coding
    laterality: Coding
    started: DateTime
    performer: Reference
    instance: ImagingStudy_Series_Instance


@dataclass
class ImagingStudy_Series_Instance:
    id: String
    extension: Extension
    modifier_extension: Extension
    uid: Oid
    number: UnsignedInt
    sop_class: Oid
    title: String


@dataclass
class Immunization:
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
    practitioner: Immunization_Practitioner
    note: Annotation
    explanation: Immunization_Explanation
    reaction: Immunization_Reaction
    vaccination_protocol: Immunization_VaccinationProtocol


@dataclass
class Immunization_Practitioner:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class Immunization_Explanation:
    id: String
    extension: Extension
    modifier_extension: Extension
    reason: CodeableConcept
    reason_not_given: CodeableConcept


@dataclass
class Immunization_Reaction:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: DateTime
    detail: Reference
    reported: Boolean


@dataclass
class Immunization_VaccinationProtocol:
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
class ImmunizationRecommendation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    patient: Reference
    recommendation: ImmunizationRecommendation_Recommendation


@dataclass
class ImmunizationRecommendation_Recommendation:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: DateTime
    vaccine_code: CodeableConcept
    target_disease: CodeableConcept
    dose_number: PositiveInt
    forecast_status: CodeableConcept
    date_criterion: ImmunizationRecommendation_Recommendation_DateCriterion
    protocol: ImmunizationRecommendation_Recommendation_Protocol
    supporting_immunization: Reference
    supporting_patient_information: Reference


@dataclass
class ImmunizationRecommendation_Recommendation_DateCriterion:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: DateTime


@dataclass
class ImmunizationRecommendation_Recommendation_Protocol:
    id: String
    extension: Extension
    modifier_extension: Extension
    dose_sequence: PositiveInt
    description: String
    authority: Reference
    series: String


@dataclass
class ImplementationGuide:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    version: String
    name: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    copyright: Markdown
    fhir_version: Id
    dependency: ImplementationGuide_Dependency
    package_value: ImplementationGuide_Package
    global: ImplementationGuide_Global
    binary: Uri
    page: ImplementationGuide_Page


@dataclass
class ImplementationGuide_Dependency:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: GuideDependencyTypeCode
    uri: Uri


@dataclass
class ImplementationGuide_Package:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    description: String
    resource: ImplementationGuide_Package_Resource


@dataclass
class ImplementationGuide_Package_Resource:
    id: String
    extension: Extension
    modifier_extension: Extension
    example: Boolean
    name: String
    description: String
    acronym: String
    source: ImplementationGuide_Package_Resource_Source
    example_for: Reference


@dataclass
class ImplementationGuide_Package_Resource_Source:
    uri: Uri
    reference: Reference


@dataclass
class ImplementationGuide_Global:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ResourceTypeCode
    profile: Reference


@dataclass
class ImplementationGuide_Page:
    id: String
    extension: Extension
    modifier_extension: Extension
    source: Uri
    title: String
    kind: GuidePageKindCode
    type: ResourceTypeCode
    package_value: String
    format: MimeTypeCode
    page: ImplementationGuide_Page


@dataclass
class Library:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    type: CodeableConcept
    date: DateTime
    publisher: String
    description: Markdown
    purpose: Markdown
    usage: String
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    use_context: UsageContext
    jurisdiction: CodeableConcept
    topic: CodeableConcept
    contributor: Contributor
    contact: ContactDetail
    copyright: Markdown
    related_artifact: RelatedArtifact
    parameter: ParameterDefinition
    data_requirement: DataRequirement
    content: Attachment


@dataclass
class Linkage:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    active: Boolean
    author: Reference
    item: Linkage_Item


@dataclass
class Linkage_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: LinkageTypeCode
    resource: Reference


@dataclass
class List:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ListStatusCode
    mode: ListModeCode
    title: String
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    date: DateTime
    source: Reference
    ordered_by: CodeableConcept
    note: Annotation
    entry: List_Entry
    empty_reason: CodeableConcept


@dataclass
class List_Entry:
    id: String
    extension: Extension
    modifier_extension: Extension
    flag: CodeableConcept
    deleted: Boolean
    date: DateTime
    item: Reference


@dataclass
class Location:
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
    position: Location_Position
    managing_organization: Reference
    part_of: Reference
    endpoint: Reference


@dataclass
class Location_Position:
    id: String
    extension: Extension
    modifier_extension: Extension
    longitude: Decimal
    latitude: Decimal
    altitude: Decimal


@dataclass
class Measure:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    description: Markdown
    purpose: Markdown
    usage: String
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    use_context: UsageContext
    jurisdiction: CodeableConcept
    topic: CodeableConcept
    contributor: Contributor
    contact: ContactDetail
    copyright: Markdown
    related_artifact: RelatedArtifact
    library: Reference
    disclaimer: Markdown
    scoring: CodeableConcept
    composite_scoring: CodeableConcept
    type: CodeableConcept
    risk_adjustment: String
    rate_aggregation: String
    rationale: Markdown
    clinical_recommendation_statement: Markdown
    improvement_notation: String
    definition: Markdown
    guidance: Markdown
    set: String
    group: Measure_Group
    supplemental_data: Measure_SupplementalData


@dataclass
class Measure_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    name: String
    description: String
    population: Measure_Group_Population
    stratifier: Measure_Group_Stratifier


@dataclass
class Measure_Group_Population:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    name: String
    description: String
    criteria: String


@dataclass
class Measure_Group_Stratifier:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    criteria: String
    path: String


@dataclass
class Measure_SupplementalData:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    usage: CodeableConcept
    criteria: String
    path: String


@dataclass
class MeasureReport:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: MeasureReportStatusCode
    type: MeasureReportTypeCode
    measure: Reference
    patient: Reference
    date: DateTime
    reporting_organization: Reference
    period: Period
    group: MeasureReport_Group
    evaluated_resources: Reference


@dataclass
class MeasureReport_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    population: MeasureReport_Group_Population
    measure_score: Decimal
    stratifier: MeasureReport_Group_Stratifier


@dataclass
class MeasureReport_Group_Population:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    count: Integer
    patients: Reference


@dataclass
class MeasureReport_Group_Stratifier:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    stratum: MeasureReport_Group_Stratifier_StratifierGroup


@dataclass
class MeasureReport_Group_Stratifier_StratifierGroup:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: String
    population: MeasureReport_Group_Stratifier_StratifierGroup_StratifierGroupPopulation
    measure_score: Decimal


@dataclass
class MeasureReport_Group_Stratifier_StratifierGroup_StratifierGroupPopulation:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    count: Integer
    patients: Reference


@dataclass
class Media:
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
    type: DigitalMediaTypeCode
    subtype: CodeableConcept
    view: CodeableConcept
    subject: Reference
    context: Reference
    occurrence: Media_Occurrence
    operator: Reference
    reason_code: CodeableConcept
    body_site: CodeableConcept
    device: Reference
    height: PositiveInt
    width: PositiveInt
    frames: PositiveInt
    duration: UnsignedInt
    content: Attachment
    note: Annotation


@dataclass
class Media_Occurrence:
    date_time: DateTime
    period: Period


@dataclass
class Medication:
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
    ingredient: Medication_Ingredient
    package_value: Medication_Package
    image: Attachment


@dataclass
class Medication_Ingredient:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: Medication_Ingredient_Item
    is_active: Boolean
    amount: Ratio


@dataclass
class Medication_Ingredient_Item:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Medication_Package:
    id: String
    extension: Extension
    modifier_extension: Extension
    container: CodeableConcept
    content: Medication_Package_Content
    batch: Medication_Package_Batch


@dataclass
class Medication_Package_Content:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: Medication_Package_Content_Item
    amount: SimpleQuantity


@dataclass
class Medication_Package_Content_Item:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Medication_Package_Batch:
    id: String
    extension: Extension
    modifier_extension: Extension
    lot_number: String
    expiration_date: DateTime


@dataclass
class MedicationAdministration:
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
    part_of: Reference
    status: MedicationAdministrationStatusCode
    category: CodeableConcept
    medication: MedicationAdministration_Medication
    subject: Reference
    context: Reference
    supporting_information: Reference
    effective: MedicationAdministration_Effective
    performer: MedicationAdministration_Performer
    not_given: Boolean
    reason_not_given: CodeableConcept
    reason_code: CodeableConcept
    reason_reference: Reference
    prescription: Reference
    device: Reference
    note: Annotation
    dosage: MedicationAdministration_Dosage
    event_history: Reference


@dataclass
class MedicationAdministration_Medication:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationAdministration_Effective:
    date_time: DateTime
    period: Period


@dataclass
class MedicationAdministration_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    actor: Reference
    on_behalf_of: Reference


@dataclass
class MedicationAdministration_Dosage:
    id: String
    extension: Extension
    modifier_extension: Extension
    text: String
    site: CodeableConcept
    route: CodeableConcept
    method: CodeableConcept
    dose: SimpleQuantity
    rate: MedicationAdministration_Dosage_Rate


@dataclass
class MedicationAdministration_Dosage_Rate:
    ratio: Ratio
    quantity: SimpleQuantity


@dataclass
class MedicationDispense:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    part_of: Reference
    status: MedicationDispenseStatusCode
    category: CodeableConcept
    medication: MedicationDispense_Medication
    subject: Reference
    context: Reference
    supporting_information: Reference
    performer: MedicationDispense_Performer
    authorizing_prescription: Reference
    type: CodeableConcept
    quantity: SimpleQuantity
    days_supply: SimpleQuantity
    when_prepared: DateTime
    when_handed_over: DateTime
    destination: Reference
    receiver: Reference
    note: Annotation
    dosage_instruction: Dosage
    substitution: MedicationDispense_Substitution
    detected_issue: Reference
    not_done: Boolean
    not_done_reason: MedicationDispense_NotDoneReason
    event_history: Reference


@dataclass
class MedicationDispense_Medication:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationDispense_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    actor: Reference
    on_behalf_of: Reference


@dataclass
class MedicationDispense_Substitution:
    id: String
    extension: Extension
    modifier_extension: Extension
    was_substituted: Boolean
    type: CodeableConcept
    reason: CodeableConcept
    responsible_party: Reference


@dataclass
class MedicationDispense_NotDoneReason:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationRequest:
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
    medication: MedicationRequest_Medication
    subject: Reference
    context: Reference
    supporting_information: Reference
    authored_on: DateTime
    requester: MedicationRequest_Requester
    recorder: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    dosage_instruction: Dosage
    dispense_request: MedicationRequest_DispenseRequest
    substitution: MedicationRequest_Substitution
    prior_prescription: Reference
    detected_issue: Reference
    event_history: Reference


@dataclass
class MedicationRequest_Medication:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationRequest_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class MedicationRequest_DispenseRequest:
    id: String
    extension: Extension
    modifier_extension: Extension
    validity_period: Period
    number_of_repeats_allowed: PositiveInt
    quantity: SimpleQuantity
    expected_supply_duration: Duration
    performer: Reference


@dataclass
class MedicationRequest_Substitution:
    id: String
    extension: Extension
    modifier_extension: Extension
    allowed: Boolean
    reason: CodeableConcept


@dataclass
class MedicationStatement:
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
    medication: MedicationStatement_Medication
    effective: MedicationStatement_Effective
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
class MedicationStatement_Medication:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationStatement_Effective:
    date_time: DateTime
    period: Period


@dataclass
class MessageDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    base: Reference
    parent: Reference
    replaces: Reference
    event: Coding
    category: MessageSignificanceCategoryCode
    focus: MessageDefinition_Focus
    response_required: Boolean
    allowed_response: MessageDefinition_AllowedResponse


@dataclass
class MessageDefinition_Focus:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: ResourceTypeCode
    profile: Reference
    min: UnsignedInt
    max: String


@dataclass
class MessageDefinition_AllowedResponse:
    id: String
    extension: Extension
    modifier_extension: Extension
    message: Reference
    situation: Markdown


@dataclass
class MessageHeader:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    event: Coding
    destination: MessageHeader_MessageDestination
    receiver: Reference
    sender: Reference
    timestamp: Instant
    enterer: Reference
    author: Reference
    source: MessageHeader_MessageSource
    responsible: Reference
    reason: CodeableConcept
    response: MessageHeader_Response
    focus: Reference


@dataclass
class MessageHeader_MessageDestination:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    target: Reference
    endpoint: Uri


@dataclass
class MessageHeader_MessageSource:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    software: String
    version: String
    contact: ContactPoint
    endpoint: Uri


@dataclass
class MessageHeader_Response:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Id
    code: ResponseTypeCode
    details: Reference


@dataclass
class NamingSystem:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    name: String
    status: PublicationStatusCode
    kind: NamingSystemTypeCode
    date: DateTime
    publisher: String
    contact: ContactDetail
    responsible: String
    type: CodeableConcept
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    usage: String
    unique_id: NamingSystem_UniqueId
    replaced_by: Reference


@dataclass
class NamingSystem_UniqueId:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: NamingSystemIdentifierTypeCode
    value: String
    preferred: Boolean
    comment: String
    period: Period


@dataclass
class NutritionOrder:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: NutritionOrderStatusCode
    patient: Reference
    encounter: Reference
    date_time: DateTime
    orderer: Reference
    allergy_intolerance: Reference
    food_preference_modifier: CodeableConcept
    exclude_food_modifier: CodeableConcept
    oral_diet: NutritionOrder_OralDiet
    supplement: NutritionOrder_Supplement
    enteral_formula: NutritionOrder_EnteralFormula


@dataclass
class NutritionOrder_OralDiet:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    schedule: Timing
    nutrient: NutritionOrder_OralDiet_Nutrient
    texture: NutritionOrder_OralDiet_Texture
    fluid_consistency_type: CodeableConcept
    instruction: String


@dataclass
class NutritionOrder_OralDiet_Nutrient:
    id: String
    extension: Extension
    modifier_extension: Extension
    modifier: CodeableConcept
    amount: SimpleQuantity


@dataclass
class NutritionOrder_OralDiet_Texture:
    id: String
    extension: Extension
    modifier_extension: Extension
    modifier: CodeableConcept
    food_type: CodeableConcept


@dataclass
class NutritionOrder_Supplement:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    product_name: String
    schedule: Timing
    quantity: SimpleQuantity
    instruction: String


@dataclass
class NutritionOrder_EnteralFormula:
    id: String
    extension: Extension
    modifier_extension: Extension
    base_formula_type: CodeableConcept
    base_formula_product_name: String
    additive_type: CodeableConcept
    additive_product_name: String
    caloric_density: SimpleQuantity
    routeof_administration: CodeableConcept
    administration: NutritionOrder_EnteralFormula_Administration
    max_volume_to_deliver: SimpleQuantity
    administration_instruction: String


@dataclass
class NutritionOrder_EnteralFormula_Administration:
    id: String
    extension: Extension
    modifier_extension: Extension
    schedule: Timing
    quantity: SimpleQuantity
    rate: NutritionOrder_EnteralFormula_Administration_Rate


@dataclass
class NutritionOrder_EnteralFormula_Administration_Rate:
    quantity: SimpleQuantity
    ratio: Ratio


@dataclass
class Observation:
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
    effective: Observation_Effective
    issued: Instant
    performer: Reference
    value: Observation_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Observation_ReferenceRange
    related: Observation_Related
    component: Observation_Component


@dataclass
class Observation_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Observation_Value:
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
class Observation_ReferenceRange:
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
class Observation_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Observation_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Observation_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Observation_ReferenceRange


@dataclass
class Observation_Component_Value:
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
class OperationDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    version: String
    name: String
    status: PublicationStatusCode
    kind: OperationKindCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    idempotent: Boolean
    code: Code
    comment: String
    base: Reference
    resource: ResourceTypeCode
    system: Boolean
    type: Boolean
    instance: Boolean
    parameter: OperationDefinition_Parameter
    overload: OperationDefinition_Overload


@dataclass
class OperationDefinition_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Code
    use: OperationParameterUseCode
    min: Integer
    max: String
    documentation: String
    type: FHIRAllTypesCode
    search_type: SearchParamTypeCode
    profile: Reference
    binding: OperationDefinition_Parameter_Binding
    part: OperationDefinition_Parameter


@dataclass
class OperationDefinition_Parameter_Binding:
    id: String
    extension: Extension
    modifier_extension: Extension
    strength: BindingStrengthCode
    value_set: OperationDefinition_Parameter_Binding_ValueSet


@dataclass
class OperationDefinition_Parameter_Binding_ValueSet:
    uri: Uri
    reference: Reference


@dataclass
class OperationDefinition_Overload:
    id: String
    extension: Extension
    modifier_extension: Extension
    parameter_name: String
    comment: String


@dataclass
class OperationOutcome:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    issue: OperationOutcome_Issue


@dataclass
class OperationOutcome_Issue:
    id: String
    extension: Extension
    modifier_extension: Extension
    severity: IssueSeverityCode
    code: IssueTypeCode
    details: CodeableConcept
    diagnostics: String
    location: String
    expression: String


@dataclass
class Organization:
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
    contact: Organization_Contact
    endpoint: Reference


@dataclass
class Organization_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    purpose: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address


@dataclass
class Parameters:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    parameter: Parameters_Parameter


@dataclass
class Parameters_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: Parameters_Parameter_Value
    resource: ContainedResource
    part: Parameters_Parameter


@dataclass
class Parameters_Parameter_Value:
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
class Patient:
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
    deceased: Patient_Deceased
    address: Address
    marital_status: CodeableConcept
    multiple_birth: Patient_MultipleBirth
    photo: Attachment
    contact: Patient_Contact
    animal: Patient_Animal
    communication: Patient_Communication
    general_practitioner: Reference
    managing_organization: Reference
    link: Patient_Link


@dataclass
class Patient_Deceased:
    boolean: Boolean
    date_time: DateTime


@dataclass
class Patient_MultipleBirth:
    boolean: Boolean
    integer: Integer


@dataclass
class Patient_Contact:
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
class Patient_Animal:
    id: String
    extension: Extension
    modifier_extension: Extension
    species: CodeableConcept
    breed: CodeableConcept
    gender_status: CodeableConcept


@dataclass
class Patient_Communication:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: CodeableConcept
    preferred: Boolean


@dataclass
class Patient_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    other: Reference
    type: LinkTypeCode


@dataclass
class PaymentNotice:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    request: Reference
    response: Reference
    status_date: Date
    created: DateTime
    target: Reference
    provider: Reference
    organization: Reference
    payment_status: CodeableConcept


@dataclass
class PaymentReconciliation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    period: Period
    created: DateTime
    organization: Reference
    request: Reference
    outcome: CodeableConcept
    disposition: String
    request_provider: Reference
    request_organization: Reference
    detail: PaymentReconciliation_Details
    form: CodeableConcept
    total: Money
    process_note: PaymentReconciliation_Notes


@dataclass
class PaymentReconciliation_Details:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    request: Reference
    response: Reference
    submitter: Reference
    payee: Reference
    date: Date
    amount: Money


@dataclass
class PaymentReconciliation_Notes:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    text: String


@dataclass
class Person:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    name: HumanName
    telecom: ContactPoint
    gender: AdministrativeGenderCode
    birth_date: Date
    address: Address
    photo: Attachment
    managing_organization: Reference
    active: Boolean
    link: Person_Link


@dataclass
class Person_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    target: Reference
    assurance: IdentityAssuranceLevelCode


@dataclass
class PlanDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    type: CodeableConcept
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    description: Markdown
    purpose: Markdown
    usage: String
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    use_context: UsageContext
    jurisdiction: CodeableConcept
    topic: CodeableConcept
    contributor: Contributor
    contact: ContactDetail
    copyright: Markdown
    related_artifact: RelatedArtifact
    library: Reference
    goal: PlanDefinition_Goal
    action: PlanDefinition_Action


@dataclass
class PlanDefinition_Goal:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    description: CodeableConcept
    priority: CodeableConcept
    start: CodeableConcept
    addresses: CodeableConcept
    documentation: RelatedArtifact
    target: PlanDefinition_Goal_Target


@dataclass
class PlanDefinition_Goal_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: PlanDefinition_Goal_Target_Detail
    due: Duration


@dataclass
class PlanDefinition_Goal_Target_Detail:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept


@dataclass
class PlanDefinition_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    label: String
    title: String
    description: String
    text_equivalent: String
    code: CodeableConcept
    reason: CodeableConcept
    documentation: RelatedArtifact
    goal_id: Id
    trigger_definition: TriggerDefinition
    condition: PlanDefinition_Action_Condition
    input: DataRequirement
    output: DataRequirement
    related_action: PlanDefinition_Action_RelatedAction
    timing: PlanDefinition_Action_TimingType
    participant: PlanDefinition_Action_Participant
    type: Coding
    grouping_behavior: ActionGroupingBehaviorCode
    selection_behavior: ActionSelectionBehaviorCode
    required_behavior: ActionRequiredBehaviorCode
    precheck_behavior: ActionPrecheckBehaviorCode
    cardinality_behavior: ActionCardinalityBehaviorCode
    definition: Reference
    transform: Reference
    dynamic_value: PlanDefinition_Action_DynamicValue
    action: PlanDefinition_Action


@dataclass
class PlanDefinition_Action_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: ActionConditionKindCode
    description: String
    language: String
    expression: String


@dataclass
class PlanDefinition_Action_RelatedAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    action_id: Id
    relationship: ActionRelationshipTypeCode
    offset: PlanDefinition_Action_RelatedAction_Offset


@dataclass
class PlanDefinition_Action_RelatedAction_Offset:
    duration: Duration
    range: Range


@dataclass
class PlanDefinition_Action_TimingType:
    date_time: DateTime
    period: Period
    duration: Duration
    range: Range
    timing_value: Timing


@dataclass
class PlanDefinition_Action_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ActionParticipantTypeCode
    role: CodeableConcept


@dataclass
class PlanDefinition_Action_DynamicValue:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    path: String
    language: String
    expression: String


@dataclass
class Practitioner:
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
    qualification: Practitioner_Qualification
    communication: CodeableConcept


@dataclass
class Practitioner_Qualification:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    period: Period
    issuer: Reference


@dataclass
class PractitionerRole:
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
    available_time: PractitionerRole_AvailableTime
    not_available: PractitionerRole_NotAvailable
    availability_exceptions: String
    endpoint: Reference


@dataclass
class PractitionerRole_AvailableTime:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: DaysOfWeekCode
    all_day: Boolean
    available_start_time: Time
    available_end_time: Time


@dataclass
class PractitionerRole_NotAvailable:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    during: Period


@dataclass
class Procedure:
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
    performed: Procedure_Performed
    performer: Procedure_Performer
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
    focal_device: Procedure_FocalDevice
    used_reference: Reference
    used_code: CodeableConcept


@dataclass
class Procedure_Performed:
    date_time: DateTime
    period: Period


@dataclass
class Procedure_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference
    on_behalf_of: Reference


@dataclass
class Procedure_FocalDevice:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: CodeableConcept
    manipulated: Reference


@dataclass
class ProcedureRequest:
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
    requisition: Identifier
    status: RequestStatusCode
    intent: RequestIntentCode
    priority: RequestPriorityCode
    do_not_perform: Boolean
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    context: Reference
    occurrence: ProcedureRequest_Occurrence
    as_needed: ProcedureRequest_AsNeeded
    authored_on: DateTime
    requester: ProcedureRequest_Requester
    performer_type: CodeableConcept
    performer: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    supporting_info: Reference
    specimen: Reference
    body_site: CodeableConcept
    note: Annotation
    relevant_history: Reference


@dataclass
class ProcedureRequest_Occurrence:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class ProcedureRequest_AsNeeded:
    boolean: Boolean
    codeable_concept: CodeableConcept


@dataclass
class ProcedureRequest_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class ProcessRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    action: ActionListCode
    target: Reference
    created: DateTime
    provider: Reference
    organization: Reference
    request: Reference
    response: Reference
    nullify: Boolean
    reference: String
    item: ProcessRequest_Items
    include: String
    exclude: String
    period: Period


@dataclass
class ProcessRequest_Items:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence_link_id: Integer


@dataclass
class ProcessResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    created: DateTime
    organization: Reference
    request: Reference
    outcome: CodeableConcept
    disposition: String
    request_provider: Reference
    request_organization: Reference
    form: CodeableConcept
    process_note: ProcessResponse_ProcessNote
    error: CodeableConcept
    communication_request: Reference


@dataclass
class ProcessResponse_ProcessNote:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    text: String


@dataclass
class Provenance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    target: Reference
    period: Period
    recorded: Instant
    policy: Uri
    location: Reference
    reason: Coding
    activity: Coding
    agent: Provenance_Agent
    entity: Provenance_Entity
    signature: Signature


@dataclass
class Provenance_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    who: Provenance_Agent_Who
    on_behalf_of: Provenance_Agent_OnBehalfOf
    related_agent_type: CodeableConcept


@dataclass
class Provenance_Agent_Who:
    uri: Uri
    reference: Reference


@dataclass
class Provenance_Agent_OnBehalfOf:
    uri: Uri
    reference: Reference


@dataclass
class Provenance_Entity:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: ProvenanceEntityRoleCode
    what: Provenance_Entity_What
    agent: Provenance_Agent


@dataclass
class Provenance_Entity_What:
    uri: Uri
    reference: Reference
    identifier: Identifier


@dataclass
class Questionnaire:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    description: Markdown
    purpose: Markdown
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    use_context: UsageContext
    jurisdiction: CodeableConcept
    contact: ContactDetail
    copyright: Markdown
    code: Coding
    subject_type: ResourceTypeCode
    item: Questionnaire_Item


@dataclass
class Questionnaire_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    link_id: String
    definition: Uri
    code: Coding
    prefix: String
    text: String
    type: QuestionnaireItemTypeCode
    enable_when: Questionnaire_Item_EnableWhen
    required: Boolean
    repeats: Boolean
    read_only: Boolean
    max_length: Integer
    options: Reference
    option: Questionnaire_Item_Option
    initial: Questionnaire_Item_Initial
    item: Questionnaire_Item


@dataclass
class Questionnaire_Item_EnableWhen:
    id: String
    extension: Extension
    modifier_extension: Extension
    question: String
    has_answer_value: Boolean
    answer: Questionnaire_Item_EnableWhen_Answer


@dataclass
class Questionnaire_Item_EnableWhen_Answer:
    boolean: Boolean
    decimal: Decimal
    integer: Integer
    date: Date
    date_time: DateTime
    time: Time
    string_value: String
    uri: Uri
    attachment: Attachment
    coding: Coding
    quantity: Quantity
    reference: Reference


@dataclass
class Questionnaire_Item_Option:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: Questionnaire_Item_Option_Value


@dataclass
class Questionnaire_Item_Option_Value:
    integer: Integer
    date: Date
    time: Time
    string_value: String
    coding: Coding


@dataclass
class Questionnaire_Item_Initial:
    boolean: Boolean
    decimal: Decimal
    integer: Integer
    date: Date
    date_time: DateTime
    time: Time
    string_value: String
    uri: Uri
    attachment: Attachment
    coding: Coding
    quantity: Quantity
    reference: Reference


@dataclass
class QuestionnaireResponse:
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
    parent: Reference
    questionnaire: Reference
    status: QuestionnaireResponseStatusCode
    subject: Reference
    context: Reference
    authored: DateTime
    author: Reference
    source: Reference
    item: QuestionnaireResponse_Item


@dataclass
class QuestionnaireResponse_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    link_id: String
    definition: Uri
    text: String
    subject: Reference
    answer: QuestionnaireResponse_Item_Answer
    item: QuestionnaireResponse_Item


@dataclass
class QuestionnaireResponse_Item_Answer:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: QuestionnaireResponse_Item_Answer_Value
    item: QuestionnaireResponse_Item


@dataclass
class QuestionnaireResponse_Item_Answer_Value:
    boolean: Boolean
    decimal: Decimal
    integer: Integer
    date: Date
    date_time: DateTime
    time: Time
    string_value: String
    uri: Uri
    attachment: Attachment
    coding: Coding
    quantity: Quantity
    reference: Reference


@dataclass
class ReferralRequest:
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
    group_identifier: Identifier
    status: RequestStatusCode
    intent: RequestIntentCode
    type: CodeableConcept
    priority: RequestPriorityCode
    service_requested: CodeableConcept
    subject: Reference
    context: Reference
    occurrence: ReferralRequest_Occurrence
    authored_on: DateTime
    requester: ReferralRequest_Requester
    specialty: CodeableConcept
    recipient: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    description: String
    supporting_info: Reference
    note: Annotation
    relevant_history: Reference


@dataclass
class ReferralRequest_Occurrence:
    date_time: DateTime
    period: Period


@dataclass
class ReferralRequest_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class RelatedPerson:
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
    patient: Reference
    relationship: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    gender: AdministrativeGenderCode
    birth_date: Date
    address: Address
    photo: Attachment
    period: Period


@dataclass
class RequestGroup:
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
    group_identifier: Identifier
    status: RequestStatusCode
    intent: RequestIntentCode
    priority: RequestPriorityCode
    subject: Reference
    context: Reference
    authored_on: DateTime
    author: Reference
    reason: RequestGroup_Reason
    note: Annotation
    action: RequestGroup_Action


@dataclass
class RequestGroup_Reason:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class RequestGroup_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    label: String
    title: String
    description: String
    text_equivalent: String
    code: CodeableConcept
    documentation: RelatedArtifact
    condition: RequestGroup_Action_Condition
    related_action: RequestGroup_Action_RelatedAction
    timing: RequestGroup_Action_TimingType
    participant: Reference
    type: Coding
    grouping_behavior: ActionGroupingBehaviorCode
    selection_behavior: ActionSelectionBehaviorCode
    required_behavior: ActionRequiredBehaviorCode
    precheck_behavior: ActionPrecheckBehaviorCode
    cardinality_behavior: ActionCardinalityBehaviorCode
    resource: Reference
    action: RequestGroup_Action


@dataclass
class RequestGroup_Action_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: ActionConditionKindCode
    description: String
    language: String
    expression: String


@dataclass
class RequestGroup_Action_RelatedAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    action_id: Id
    relationship: ActionRelationshipTypeCode
    offset: RequestGroup_Action_RelatedAction_Offset


@dataclass
class RequestGroup_Action_RelatedAction_Offset:
    duration: Duration
    range: Range


@dataclass
class RequestGroup_Action_TimingType:
    date_time: DateTime
    period: Period
    duration: Duration
    range: Range
    timing_value: Timing


@dataclass
class ResearchStudy:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    title: String
    protocol: Reference
    part_of: Reference
    status: ResearchStudyStatusCode
    category: CodeableConcept
    focus: CodeableConcept
    contact: ContactDetail
    related_artifact: RelatedArtifact
    keyword: CodeableConcept
    jurisdiction: CodeableConcept
    description: Markdown
    enrollment: Reference
    period: Period
    sponsor: Reference
    principal_investigator: Reference
    site: Reference
    reason_stopped: CodeableConcept
    note: Annotation
    arm: ResearchStudy_Arm


@dataclass
class ResearchStudy_Arm:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    code: CodeableConcept
    description: String


@dataclass
class ResearchSubject:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ResearchSubjectStatusCode
    period: Period
    study: Reference
    individual: Reference
    assigned_arm: String
    actual_arm: String
    consent: Reference


@dataclass
class RiskAssessment:
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
    parent: Reference
    status: ObservationStatusCode
    method: CodeableConcept
    code: CodeableConcept
    subject: Reference
    context: Reference
    occurrence: RiskAssessment_Occurrence
    condition: Reference
    performer: Reference
    reason: RiskAssessment_Reason
    basis: Reference
    prediction: RiskAssessment_Prediction
    mitigation: String
    comment: String


@dataclass
class RiskAssessment_Occurrence:
    date_time: DateTime
    period: Period


@dataclass
class RiskAssessment_Reason:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class RiskAssessment_Prediction:
    id: String
    extension: Extension
    modifier_extension: Extension
    outcome: CodeableConcept
    probability: RiskAssessment_Prediction_Probability
    qualitative_risk: CodeableConcept
    relative_risk: Decimal
    when: RiskAssessment_Prediction_When
    rationale: String


@dataclass
class RiskAssessment_Prediction_Probability:
    decimal: Decimal
    range: Range


@dataclass
class RiskAssessment_Prediction_When:
    period: Period
    range: Range


@dataclass
class Schedule:
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
    service_category: CodeableConcept
    service_type: CodeableConcept
    specialty: CodeableConcept
    actor: Reference
    planning_horizon: Period
    comment: String


@dataclass
class SearchParameter:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    version: String
    name: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    code: Code
    base: ResourceTypeCode
    type: SearchParamTypeCode
    derived_from: Uri
    description: Markdown
    expression: String
    xpath: String
    xpath_usage: XPathUsageTypeCode
    target: ResourceTypeCode
    comparator: SearchComparatorCode
    modifier: SearchModifierCodeCode
    chain: String
    component: SearchParameter_Component


@dataclass
class SearchParameter_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    definition: Reference
    expression: String


@dataclass
class Sequence:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: SequenceTypeCode
    coordinate_system: Integer
    patient: Reference
    specimen: Reference
    device: Reference
    performer: Reference
    quantity: Quantity
    reference_seq: Sequence_ReferenceSeq
    variant: Sequence_Variant
    observed_seq: String
    quality: Sequence_Quality
    read_coverage: Integer
    repository: Sequence_Repository
    pointer: Reference


@dataclass
class Sequence_ReferenceSeq:
    id: String
    extension: Extension
    modifier_extension: Extension
    chromosome: CodeableConcept
    genome_build: String
    reference_seq_id: CodeableConcept
    reference_seq_pointer: Reference
    reference_seq_string: String
    strand: Integer
    window_start: Integer
    window_end: Integer


@dataclass
class Sequence_Variant:
    id: String
    extension: Extension
    modifier_extension: Extension
    start: Integer
    end: Integer
    observed_allele: String
    reference_allele: String
    cigar: String
    variant_pointer: Reference


@dataclass
class Sequence_Quality:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: QualityTypeCode
    standard_sequence: CodeableConcept
    start: Integer
    end: Integer
    score: Quantity
    method: CodeableConcept
    truth_tp: Decimal
    query_tp: Decimal
    truth_fn: Decimal
    query_fp: Decimal
    gt_fp: Decimal
    precision: Decimal
    recall: Decimal
    f_score: Decimal


@dataclass
class Sequence_Repository:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: RepositoryTypeCode
    url: Uri
    name: String
    dataset_id: String
    variantset_id: String
    readset_id: String


@dataclass
class ServiceDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    description: Markdown
    purpose: Markdown
    usage: String
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    use_context: UsageContext
    jurisdiction: CodeableConcept
    topic: CodeableConcept
    contributor: Contributor
    contact: ContactDetail
    copyright: Markdown
    related_artifact: RelatedArtifact
    trigger: TriggerDefinition
    data_requirement: DataRequirement
    operation_definition: Reference


@dataclass
class Slot:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    service_category: CodeableConcept
    service_type: CodeableConcept
    specialty: CodeableConcept
    appointment_type: CodeableConcept
    schedule: Reference
    status: SlotStatusCode
    start: Instant
    end: Instant
    overbooked: Boolean
    comment: String


@dataclass
class Specimen:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    accession_identifier: Identifier
    status: SpecimenStatusCode
    type: CodeableConcept
    subject: Reference
    received_time: DateTime
    parent: Reference
    request: Reference
    collection: Specimen_Collection
    processing: Specimen_Processing
    container: Specimen_Container
    note: Annotation


@dataclass
class Specimen_Collection:
    id: String
    extension: Extension
    modifier_extension: Extension
    collector: Reference
    collected: Specimen_Collection_Collected
    quantity: SimpleQuantity
    method: CodeableConcept
    body_site: CodeableConcept


@dataclass
class Specimen_Collection_Collected:
    date_time: DateTime
    period: Period


@dataclass
class Specimen_Processing:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    procedure: CodeableConcept
    additive: Reference
    time: Specimen_Processing_Time


@dataclass
class Specimen_Processing_Time:
    date_time: DateTime
    period: Period


@dataclass
class Specimen_Container:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    description: String
    type: CodeableConcept
    capacity: SimpleQuantity
    specimen_quantity: SimpleQuantity
    additive: Specimen_Container_Additive


@dataclass
class Specimen_Container_Additive:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class StructureDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    keyword: Coding
    fhir_version: Id
    mapping: StructureDefinition_Mapping
    kind: StructureDefinitionKindCode
    abstract: Boolean
    context_type: ExtensionContextCode
    context: String
    context_invariant: String
    type: FHIRDefinedTypeExtCode
    base_definition: Uri
    derivation: TypeDerivationRuleCode
    snapshot: StructureDefinition_Snapshot
    differential: StructureDefinition_Differential


@dataclass
class StructureDefinition_Mapping:
    id: String
    extension: Extension
    modifier_extension: Extension
    identity: Id
    uri: Uri
    name: String
    comment: String


@dataclass
class StructureDefinition_Snapshot:
    id: String
    extension: Extension
    modifier_extension: Extension
    element: ElementDefinition


@dataclass
class StructureDefinition_Differential:
    id: String
    extension: Extension
    modifier_extension: Extension
    element: ElementDefinition


@dataclass
class StructureMap:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    structure: StructureMap_Structure
    import: Uri
    group: StructureMap_Group


@dataclass
class StructureMap_Structure:
    id: String
    extension: Extension
    modifier_extension: Extension
    url: Uri
    mode: StructureMapModelModeCode
    alias: String
    documentation: String


@dataclass
class StructureMap_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    extends: Id
    type_mode: StructureMapGroupTypeModeCode
    documentation: String
    input: StructureMap_Group_Input
    rule: StructureMap_Group_Rule


@dataclass
class StructureMap_Group_Input:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    type: String
    mode: StructureMapInputModeCode
    documentation: String


@dataclass
class StructureMap_Group_Rule:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    source: StructureMap_Group_Rule_Source
    target: StructureMap_Group_Rule_Target
    rule: StructureMap_Group_Rule
    dependent: StructureMap_Group_Rule_Dependent
    documentation: String


@dataclass
class StructureMap_Group_Rule_Source:
    id: String
    extension: Extension
    modifier_extension: Extension
    context: Id
    min: Integer
    max: String
    type: String
    default_value: StructureMap_Group_Rule_Source_DefaultValue
    element: String
    list_mode: StructureMapSourceListModeCode
    variable: Id
    condition: String
    check: String


@dataclass
class StructureMap_Group_Rule_Source_DefaultValue:
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
class StructureMap_Group_Rule_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    context: Id
    context_type: StructureMapContextTypeCode
    element: String
    variable: Id
    list_mode: StructureMapTargetListModeCode
    list_rule_id: Id
    transform: StructureMapTransformCode
    parameter: StructureMap_Group_Rule_Target_Parameter


@dataclass
class StructureMap_Group_Rule_Target_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: StructureMap_Group_Rule_Target_Parameter_Value


@dataclass
class StructureMap_Group_Rule_Target_Parameter_Value:
    id: Id
    string_value: String
    boolean: Boolean
    integer: Integer
    decimal: Decimal


@dataclass
class StructureMap_Group_Rule_Dependent:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: Id
    variable: String


@dataclass
class Subscription:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    status: SubscriptionStatusCode
    contact: ContactPoint
    end: Instant
    reason: String
    criteria: String
    error: String
    channel: Subscription_Channel
    tag: Coding


@dataclass
class Subscription_Channel:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: SubscriptionChannelTypeCode
    endpoint: Uri
    payload: String
    header: String


@dataclass
class Substance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FHIRSubstanceStatusCode
    category: CodeableConcept
    code: CodeableConcept
    description: String
    instance: Substance_Instance
    ingredient: Substance_Ingredient


@dataclass
class Substance_Instance:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    expiry: DateTime
    quantity: SimpleQuantity


@dataclass
class Substance_Ingredient:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: Ratio
    substance: Substance_Ingredient_SubstanceType


@dataclass
class Substance_Ingredient_SubstanceType:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class SupplyDelivery:
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
    status: SupplyDeliveryStatusCode
    patient: Reference
    type: CodeableConcept
    supplied_item: SupplyDelivery_SuppliedItem
    occurrence: SupplyDelivery_Occurrence
    supplier: Reference
    destination: Reference
    receiver: Reference


@dataclass
class SupplyDelivery_SuppliedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: SimpleQuantity
    item: SupplyDelivery_SuppliedItem_Item


@dataclass
class SupplyDelivery_SuppliedItem_Item:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class SupplyDelivery_Occurrence:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class SupplyRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: SupplyRequestStatusCode
    category: CodeableConcept
    priority: RequestPriorityCode
    ordered_item: SupplyRequest_OrderedItem
    occurrence: SupplyRequest_Occurrence
    authored_on: DateTime
    requester: SupplyRequest_Requester
    supplier: Reference
    reason: SupplyRequest_Reason
    deliver_from: Reference
    deliver_to: Reference


@dataclass
class SupplyRequest_OrderedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: Quantity
    item: SupplyRequest_OrderedItem_Item


@dataclass
class SupplyRequest_OrderedItem_Item:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class SupplyRequest_Occurrence:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class SupplyRequest_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class SupplyRequest_Reason:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Task:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition: Task_Definition
    based_on: Reference
    group_identifier: Identifier
    part_of: Reference
    status: TaskStatusCode
    status_reason: CodeableConcept
    business_status: CodeableConcept
    intent: RequestIntentCode
    priority: RequestPriorityCode
    code: CodeableConcept
    description: String
    focus: Reference
    for_value: Reference
    context: Reference
    execution_period: Period
    authored_on: DateTime
    last_modified: DateTime
    requester: Task_Requester
    performer_type: CodeableConcept
    owner: Reference
    reason: CodeableConcept
    note: Annotation
    relevant_history: Reference
    restriction: Task_Restriction
    input: Task_Parameter
    output: Task_Output


@dataclass
class Task_Definition:
    uri: Uri
    reference: Reference


@dataclass
class Task_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class Task_Restriction:
    id: String
    extension: Extension
    modifier_extension: Extension
    repetitions: PositiveInt
    period: Period
    recipient: Reference


@dataclass
class Task_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value: Task_Parameter_Value


@dataclass
class Task_Parameter_Value:
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
class Task_Output:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value: Task_Output_Value


@dataclass
class Task_Output_Value:
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
class TestReport:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    name: String
    status: TestReportStatusCode
    test_script: Reference
    result: TestReportResultCode
    score: Decimal
    tester: String
    issued: DateTime
    participant: TestReport_Participant
    setup: TestReport_Setup
    test: TestReport_Test
    teardown: TestReport_Teardown


@dataclass
class TestReport_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: TestReportParticipantTypeCode
    uri: Uri
    display: String


@dataclass
class TestReport_Setup:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestReport_Setup_SetupAction


@dataclass
class TestReport_Setup_SetupAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestReport_Setup_SetupAction_Operation
    assert_value: TestReport_Setup_SetupAction_Assert


@dataclass
class TestReport_Setup_SetupAction_Operation:
    id: String
    extension: Extension
    modifier_extension: Extension
    result: TestReportActionResultCode
    message: Markdown
    detail: Uri


@dataclass
class TestReport_Setup_SetupAction_Assert:
    id: String
    extension: Extension
    modifier_extension: Extension
    result: TestReportActionResultCode
    message: Markdown
    detail: String


@dataclass
class TestReport_Test:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    description: String
    action: TestReport_Test_TestAction


@dataclass
class TestReport_Test_TestAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestReport_Setup_SetupAction_Operation
    assert_value: TestReport_Setup_SetupAction_Assert


@dataclass
class TestReport_Teardown:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestReport_Teardown_TeardownAction


@dataclass
class TestReport_Teardown_TeardownAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestReport_Setup_SetupAction_Operation


@dataclass
class TestScript:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    origin: TestScript_Origin
    destination: TestScript_Destination
    metadata: TestScript_Metadata
    fixture: TestScript_Fixture
    profile: Reference
    variable: TestScript_Variable
    rule: TestScript_Rule
    ruleset: TestScript_Ruleset
    setup: TestScript_Setup
    test: TestScript_Test
    teardown: TestScript_Teardown


@dataclass
class TestScript_Origin:
    id: String
    extension: Extension
    modifier_extension: Extension
    index: Integer
    profile: Coding


@dataclass
class TestScript_Destination:
    id: String
    extension: Extension
    modifier_extension: Extension
    index: Integer
    profile: Coding


@dataclass
class TestScript_Metadata:
    id: String
    extension: Extension
    modifier_extension: Extension
    link: TestScript_Metadata_Link
    capability: TestScript_Metadata_Capability


@dataclass
class TestScript_Metadata_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    url: Uri
    description: String


@dataclass
class TestScript_Metadata_Capability:
    id: String
    extension: Extension
    modifier_extension: Extension
    required: Boolean
    validated: Boolean
    description: String
    origin: Integer
    destination: Integer
    link: Uri
    capabilities: Reference


@dataclass
class TestScript_Fixture:
    id: String
    extension: Extension
    modifier_extension: Extension
    autocreate: Boolean
    autodelete: Boolean
    resource: Reference


@dataclass
class TestScript_Variable:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    default_value: String
    description: String
    expression: String
    header_field: String
    hint: String
    path: String
    source_id: Id


@dataclass
class TestScript_Rule:
    id: String
    extension: Extension
    modifier_extension: Extension
    resource: Reference
    param: TestScript_Rule_RuleParam


@dataclass
class TestScript_Rule_RuleParam:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: String


@dataclass
class TestScript_Ruleset:
    id: String
    extension: Extension
    modifier_extension: Extension
    resource: Reference
    rule: TestScript_Ruleset_RulesetRule


@dataclass
class TestScript_Ruleset_RulesetRule:
    id: String
    extension: Extension
    modifier_extension: Extension
    rule_id: Id
    param: TestScript_Ruleset_RulesetRule_RulesetRuleParam


@dataclass
class TestScript_Ruleset_RulesetRule_RulesetRuleParam:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: String


@dataclass
class TestScript_Setup:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestScript_Setup_SetupAction


@dataclass
class TestScript_Setup_SetupAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestScript_Setup_SetupAction_Operation
    assert_value: TestScript_Setup_SetupAction_Assert


@dataclass
class TestScript_Setup_SetupAction_Operation:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Coding
    resource: FHIRDefinedTypeCode
    label: String
    description: String
    accept: ContentTypeCode
    content_type: ContentTypeCode
    destination: Integer
    encode_request_url: Boolean
    origin: Integer
    params: String
    request_header: TestScript_Setup_SetupAction_Operation_RequestHeader
    request_id: Id
    response_id: Id
    source_id: Id
    target_id: Id
    url: String


@dataclass
class TestScript_Setup_SetupAction_Operation_RequestHeader:
    id: String
    extension: Extension
    modifier_extension: Extension
    field: String
    value: String


@dataclass
class TestScript_Setup_SetupAction_Assert:
    id: String
    extension: Extension
    modifier_extension: Extension
    label: String
    description: String
    direction: AssertionDirectionTypeCode
    compare_to_source_id: String
    compare_to_source_expression: String
    compare_to_source_path: String
    content_type: ContentTypeCode
    expression: String
    header_field: String
    minimum_id: String
    navigation_links: Boolean
    operator: AssertionOperatorTypeCode
    path: String
    request_method: TestScriptRequestMethodCodeCode
    request_url: String
    resource: FHIRDefinedTypeCode
    response: AssertionResponseTypesCode
    response_code: String
    rule: TestScript_Setup_SetupAction_Assert_ActionAssertRule
    ruleset: TestScript_Setup_SetupAction_Assert_ActionAssertRuleset
    source_id: Id
    validate_profile_id: Id
    value: String
    warning_only: Boolean


@dataclass
class TestScript_Setup_SetupAction_Assert_ActionAssertRule:
    id: String
    extension: Extension
    modifier_extension: Extension
    rule_id: Id
    param: TestScript_Setup_SetupAction_Assert_ActionAssertRule_ActionAssertRuleParam


@dataclass
class TestScript_Setup_SetupAction_Assert_ActionAssertRule_ActionAssertRuleParam:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: String


@dataclass
class TestScript_Setup_SetupAction_Assert_ActionAssertRuleset:
    id: String
    extension: Extension
    modifier_extension: Extension
    ruleset_id: Id
    rule: TestScript_Setup_SetupAction_Assert_ActionAssertRuleset_ActionAssertRulesetRule


@dataclass
class TestScript_Setup_SetupAction_Assert_ActionAssertRuleset_ActionAssertRulesetRule:
    id: String
    extension: Extension
    modifier_extension: Extension
    rule_id: Id
    param: TestScript_Setup_SetupAction_Assert_ActionAssertRuleset_ActionAssertRulesetRule_Param


@dataclass
class TestScript_Setup_SetupAction_Assert_ActionAssertRuleset_ActionAssertRulesetRule_Param:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: String


@dataclass
class TestScript_Test:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    description: String
    action: TestScript_Test_TestAction


@dataclass
class TestScript_Test_TestAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestScript_Setup_SetupAction_Operation
    assert_value: TestScript_Setup_SetupAction_Assert


@dataclass
class TestScript_Teardown:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestScript_Teardown_TeardownAction


@dataclass
class TestScript_Teardown_TeardownAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestScript_Setup_SetupAction_Operation


@dataclass
class ValueSet:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    status: PublicationStatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    immutable: Boolean
    purpose: Markdown
    copyright: Markdown
    extensible: Boolean
    compose: ValueSet_Compose
    expansion: ValueSet_Expansion


@dataclass
class ValueSet_Compose:
    id: String
    extension: Extension
    modifier_extension: Extension
    locked_date: Date
    inactive: Boolean
    include: ValueSet_Compose_ConceptSet
    exclude: ValueSet_Compose_ConceptSet


@dataclass
class ValueSet_Compose_ConceptSet:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    version: String
    concept: ValueSet_Compose_ConceptSet_ConceptReference
    filter: ValueSet_Compose_ConceptSet_Filter
    value_set: Uri


@dataclass
class ValueSet_Compose_ConceptSet_ConceptReference:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    designation: ValueSet_Compose_ConceptSet_ConceptReference_Designation


@dataclass
class ValueSet_Compose_ConceptSet_ConceptReference_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: LanguageCode
    use: Coding
    value: String


@dataclass
class ValueSet_Compose_ConceptSet_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    property: Code
    op: FilterOperatorCode
    value: Code


@dataclass
class ValueSet_Expansion:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Uri
    timestamp: DateTime
    total: Integer
    offset: Integer
    parameter: ValueSet_Expansion_Parameter
    contains: ValueSet_Expansion_Contains


@dataclass
class ValueSet_Expansion_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: ValueSet_Expansion_Parameter_Value


@dataclass
class ValueSet_Expansion_Parameter_Value:
    string_value: String
    boolean: Boolean
    integer: Integer
    decimal: Decimal
    uri: Uri
    code: Code


@dataclass
class ValueSet_Expansion_Contains:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    abstract: Boolean
    inactive: Boolean
    version: String
    code: Code
    display: String
    designation: ValueSet_Compose_ConceptSet_ConceptReference_Designation
    contains: ValueSet_Expansion_Contains


@dataclass
class VisionPrescription:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: FinancialResourceStatusCode
    patient: Reference
    encounter: Reference
    date_written: DateTime
    prescriber: Reference
    reason: VisionPrescription_Reason
    dispense: VisionPrescription_Dispense


@dataclass
class VisionPrescription_Reason:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class VisionPrescription_Dispense:
    id: String
    extension: Extension
    modifier_extension: Extension
    product: CodeableConcept
    eye: VisionEyesCode
    sphere: Decimal
    cylinder: Decimal
    axis: Integer
    prism: Decimal
    base: VisionBaseCode
    add: Decimal
    power: Decimal
    back_curve: Decimal
    diameter: Decimal
    duration: SimpleQuantity
    color: String
    brand: String
    note: Annotation


@dataclass
class Resource:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode


@dataclass
class DomainResource:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: LanguageCode
    text: Narrative
    contained: ContainedResource
    extension: Extension
    modifier_extension: Extension


@dataclass
class ContainedResource:
    account: Account
    activity_definition: ActivityDefinition
    adverse_event: AdverseEvent
    allergy_intolerance: AllergyIntolerance
    appointment: Appointment
    appointment_response: AppointmentResponse
    audit_event: AuditEvent
    basic: Basic
    binary: Binary
    body_site: BodySite
    bundle: Bundle
    capability_statement: CapabilityStatement
    care_plan: CarePlan
    care_team: CareTeam
    charge_item: ChargeItem
    claim: Claim
    claim_response: ClaimResponse
    clinical_impression: ClinicalImpression
    code_system: CodeSystem
    communication: Communication
    communication_request: CommunicationRequest
    compartment_definition: CompartmentDefinition
    composition: Composition
    concept_map: ConceptMap
    condition: Condition
    consent: Consent
    contract: Contract
    coverage: Coverage
    data_element: DataElement
    detected_issue: DetectedIssue
    device: Device
    device_component: DeviceComponent
    device_metric: DeviceMetric
    device_request: DeviceRequest
    device_use_statement: DeviceUseStatement
    diagnostic_report: DiagnosticReport
    document_manifest: DocumentManifest
    document_reference: DocumentReference
    eligibility_request: EligibilityRequest
    eligibility_response: EligibilityResponse
    encounter: Encounter
    endpoint: Endpoint
    enrollment_request: EnrollmentRequest
    enrollment_response: EnrollmentResponse
    episode_of_care: EpisodeOfCare
    expansion_profile: ExpansionProfile
    explanation_of_benefit: ExplanationOfBenefit
    family_member_history: FamilyMemberHistory
    flag: Flag
    goal: Goal
    graph_definition: GraphDefinition
    group: Group
    guidance_response: GuidanceResponse
    healthcare_service: HealthcareService
    imaging_manifest: ImagingManifest
    imaging_study: ImagingStudy
    immunization: Immunization
    immunization_recommendation: ImmunizationRecommendation
    implementation_guide: ImplementationGuide
    library: Library
    linkage: Linkage
    list: List
    location: Location
    measure: Measure
    measure_report: MeasureReport
    media: Media
    medication: Medication
    medication_administration: MedicationAdministration
    medication_dispense: MedicationDispense
    medication_request: MedicationRequest
    medication_statement: MedicationStatement
    message_definition: MessageDefinition
    message_header: MessageHeader
    naming_system: NamingSystem
    nutrition_order: NutritionOrder
    observation: Observation
    operation_definition: OperationDefinition
    operation_outcome: OperationOutcome
    organization: Organization
    parameters: Parameters
    patient: Patient
    payment_notice: PaymentNotice
    payment_reconciliation: PaymentReconciliation
    person: Person
    plan_definition: PlanDefinition
    practitioner: Practitioner
    practitioner_role: PractitionerRole
    procedure: Procedure
    procedure_request: ProcedureRequest
    process_request: ProcessRequest
    process_response: ProcessResponse
    provenance: Provenance
    questionnaire: Questionnaire
    questionnaire_response: QuestionnaireResponse
    referral_request: ReferralRequest
    related_person: RelatedPerson
    request_group: RequestGroup
    research_study: ResearchStudy
    research_subject: ResearchSubject
    risk_assessment: RiskAssessment
    schedule: Schedule
    search_parameter: SearchParameter
    sequence: Sequence
    service_definition: ServiceDefinition
    slot: Slot
    specimen: Specimen
    structure_definition: StructureDefinition
    structure_map: StructureMap
    subscription: Subscription
    substance: Substance
    supply_delivery: SupplyDelivery
    supply_request: SupplyRequest
    task: Task
    test_report: TestReport
    test_script: TestScript
    value_set: ValueSet
    vision_prescription: VisionPrescription

