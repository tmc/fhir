# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Bmi:
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
    code: Bmi_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Bmi_Effective
    issued: Instant
    performer: Reference
    value: Bmi_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Bmi_ReferenceRange
    related: Bmi_Related
    component: Bmi_Component


@dataclass
class Bmi_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    bmi_code: CodingWithFixedCode


@dataclass
class Bmi_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Bmi_Value:
    quantity: Quantity


@dataclass
class Bmi_ReferenceRange:
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
class Bmi_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Bmi_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Bmi_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Bmi_ReferenceRange


@dataclass
class Bmi_Component_Value:
    quantity: Quantity


@dataclass
class Bodyheight:
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
    code: Bodyheight_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Bodyheight_Effective
    issued: Instant
    performer: Reference
    value: Bodyheight_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Bodyheight_ReferenceRange
    related: Bodyheight_Related
    component: Bodyheight_Component


@dataclass
class Bodyheight_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    body_height_code: CodingWithFixedCode


@dataclass
class Bodyheight_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Bodyheight_Value:
    quantity: Quantity


@dataclass
class Bodyheight_ReferenceRange:
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
class Bodyheight_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Bodyheight_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Bodyheight_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Bodyheight_ReferenceRange


@dataclass
class Bodyheight_Component_Value:
    quantity: Quantity


@dataclass
class Bodylength:
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
    code: Bodylength_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Bodylength_Effective
    issued: Instant
    performer: Reference
    value: Bodylength_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Bodylength_ReferenceRange
    related: Bodylength_Related
    component: Bodylength_Component


@dataclass
class Bodylength_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    body_length_code: CodingWithFixedCode


@dataclass
class Bodylength_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Bodylength_Value:
    quantity: Quantity


@dataclass
class Bodylength_ReferenceRange:
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
class Bodylength_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Bodylength_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Bodylength_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Bodylength_ReferenceRange


@dataclass
class Bodylength_Component_Value:
    quantity: Quantity


@dataclass
class Bodytemp:
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
    code: Bodytemp_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Bodytemp_Effective
    issued: Instant
    performer: Reference
    value: Bodytemp_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Bodytemp_ReferenceRange
    related: Bodytemp_Related
    component: Bodytemp_Component


@dataclass
class Bodytemp_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    body_temp_code: CodingWithFixedCode


@dataclass
class Bodytemp_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Bodytemp_Value:
    quantity: Quantity


@dataclass
class Bodytemp_ReferenceRange:
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
class Bodytemp_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Bodytemp_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Bodytemp_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Bodytemp_ReferenceRange


@dataclass
class Bodytemp_Component_Value:
    quantity: Quantity


@dataclass
class Bodyweight:
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
    code: Bodyweight_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Bodyweight_Effective
    issued: Instant
    performer: Reference
    value: Bodyweight_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Bodyweight_ReferenceRange
    related: Bodyweight_Related
    component: Bodyweight_Component


@dataclass
class Bodyweight_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    body_weight_code: CodingWithFixedCode


@dataclass
class Bodyweight_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Bodyweight_Value:
    quantity: Quantity


@dataclass
class Bodyweight_ReferenceRange:
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
class Bodyweight_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Bodyweight_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Bodyweight_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Bodyweight_ReferenceRange


@dataclass
class Bodyweight_Component_Value:
    quantity: Quantity


@dataclass
class Bp:
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
    code: Bp_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Bp_Effective
    issued: Instant
    performer: Reference
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Bp_ReferenceRange
    related: Bp_Related
    component: Bp_Component


@dataclass
class Bp_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    bp_code: CodingWithFixedCode


@dataclass
class Bp_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Bp_ReferenceRange:
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
class Bp_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Bp_Component:


@dataclass
class Cholesterol:
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
    effective: Cholesterol_Effective
    issued: Instant
    performer: Reference
    value: Cholesterol_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Cholesterol_ReferenceRange
    component: Cholesterol_Component


@dataclass
class Cholesterol_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Cholesterol_Value:
    quantity: Quantity


@dataclass
class Cholesterol_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    high: SimpleQuantity
    text: String


@dataclass
class Cholesterol_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Cholesterol_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Cholesterol_ReferenceRange


@dataclass
class Cholesterol_Component_Value:
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
class Clinicaldocument:
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
    attester: Clinicaldocument_Attester
    custodian: Reference
    relates_to: Clinicaldocument_RelatesTo
    event: Clinicaldocument_Event
    section: Clinicaldocument_Section


@dataclass
class Clinicaldocument_Attester:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: CompositionAttestationModeCode
    time: DateTime
    party: Reference


@dataclass
class Clinicaldocument_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: DocumentRelationshipTypeCode
    target: Clinicaldocument_RelatesTo_Target


@dataclass
class Clinicaldocument_RelatesTo_Target:
    identifier: Identifier
    reference: Reference


@dataclass
class Clinicaldocument_Event:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    period: Period
    detail: Reference


@dataclass
class Clinicaldocument_Section:
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
    section: Clinicaldocument_Section


@dataclass
class Devicemetricobservation:
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
    effective: Devicemetricobservation_Effective
    performer: Reference
    value: Devicemetricobservation_Value
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    device: Reference
    reference_range: Devicemetricobservation_ReferenceRange
    related: Devicemetricobservation_Related
    component: Devicemetricobservation_Component


@dataclass
class Devicemetricobservation_Effective:
    date_time: DateTime


@dataclass
class Devicemetricobservation_Value:
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
class Devicemetricobservation_ReferenceRange:
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
class Devicemetricobservation_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Devicemetricobservation_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Devicemetricobservation_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Devicemetricobservation_ReferenceRange


@dataclass
class Devicemetricobservation_Component_Value:
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
class DiagnosticreportGenetics:
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
    effective: DiagnosticreportGenetics_Effective
    issued: Instant
    performer: DiagnosticreportGenetics_Performer
    specimen: Reference
    result: Reference
    imaging_study: Reference
    image: DiagnosticreportGenetics_Image
    conclusion: String
    presented_form: Attachment
    assessed_condition: Reference
    family_member_history: Reference
    analysis: DiagnosticReportAnalysis


@dataclass
class DiagnosticreportGenetics_Effective:
    date_time: DateTime
    period: Period


@dataclass
class DiagnosticreportGenetics_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class DiagnosticreportGenetics_Image:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference


@dataclass
class ElementdefinitionDe:
    id: String
    extension: Extension
    path: String
    slice_name: String
    label: String
    code: Coding
    definition: Markdown
    comment: Markdown
    requirements: Markdown
    alias: String
    min: UnsignedInt
    max: String
    base: ElementdefinitionDe_Base
    type: ElementdefinitionDe_TypeRef
    default_value: ElementdefinitionDe_DefaultValue
    meaning_when_missing: Markdown
    order_meaning: String
    example: ElementdefinitionDe_Example
    min_value: ElementdefinitionDe_MinValue
    max_value: ElementdefinitionDe_MaxValue
    max_length: Integer
    condition: Id
    constraint: ElementdefinitionDe_Constraint
    must_support: Boolean
    binding: ElementdefinitionDe_ElementDefinitionBinding
    mapping: ElementdefinitionDe_Mapping
    question: String
    allowed_units: ElementDefinitionAllowedUnits_Value


@dataclass
class ElementdefinitionDe_Base:
    id: String
    extension: Extension
    path: String
    min: UnsignedInt
    max: String


@dataclass
class ElementdefinitionDe_TypeRef:
    id: String
    extension: Extension
    code: Uri
    target_profile: Uri
    versioning: ReferenceVersionRulesCode


@dataclass
class ElementdefinitionDe_DefaultValue:
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
class ElementdefinitionDe_Example:
    id: String
    extension: Extension
    label: String
    value: ElementdefinitionDe_Example_Value


@dataclass
class ElementdefinitionDe_Example_Value:
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
class ElementdefinitionDe_MinValue:
    date: Date
    date_time: DateTime
    instant: Instant
    time: Time
    decimal: Decimal
    integer: Integer
    positive_int: PositiveInt
    unsigned_int: UnsignedInt
    quantity: Quantity


@dataclass
class ElementdefinitionDe_MaxValue:
    date: Date
    date_time: DateTime
    instant: Instant
    time: Time
    decimal: Decimal
    integer: Integer
    positive_int: PositiveInt
    unsigned_int: UnsignedInt
    quantity: Quantity


@dataclass
class ElementdefinitionDe_Constraint:
    id: String
    extension: Extension
    key: Id
    requirements: String
    severity: ConstraintSeverityCode
    human: String
    expression: String
    xpath: String
    source: Uri


@dataclass
class ElementdefinitionDe_ElementDefinitionBinding:
    id: String
    extension: Extension
    strength: BindingStrengthCode
    description: String
    value_set: ElementdefinitionDe_ElementDefinitionBinding_ValueSet


@dataclass
class ElementdefinitionDe_ElementDefinitionBinding_ValueSet:
    uri: Uri
    reference: Reference


@dataclass
class ElementdefinitionDe_Mapping:
    id: String
    extension: Extension
    identity: Id
    language: MimeTypeCode
    map: String
    comment: String


@dataclass
class FamilymemberhistoryGenetic:
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
    born: FamilymemberhistoryGenetic_Born
    age: FamilymemberhistoryGenetic_AgeType
    estimated_age: Boolean
    deceased: FamilymemberhistoryGenetic_Deceased
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    condition: FamilymemberhistoryGenetic_Condition
    parent: FamilyMemberHistoryParent
    sibling: FamilyMemberHistorySibling
    observation: Reference


@dataclass
class FamilymemberhistoryGenetic_Born:
    period: Period
    date: Date
    string_value: String


@dataclass
class FamilymemberhistoryGenetic_AgeType:
    age_value: Age
    range: Range
    string_value: String


@dataclass
class FamilymemberhistoryGenetic_Deceased:
    boolean: Boolean
    age: Age
    range: Range
    date: Date
    string_value: String


@dataclass
class FamilymemberhistoryGenetic_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    outcome: CodeableConcept
    onset: FamilymemberhistoryGenetic_Condition_Onset
    note: Annotation


@dataclass
class FamilymemberhistoryGenetic_Condition_Onset:
    age: Age
    range: Range
    period: Period
    string_value: String


@dataclass
class HdlCholesterol:
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
    effective: HdlCholesterol_Effective
    issued: Instant
    performer: Reference
    value: HdlCholesterol_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: HdlCholesterol_ReferenceRange
    component: HdlCholesterol_Component


@dataclass
class HdlCholesterol_Effective:
    date_time: DateTime
    period: Period


@dataclass
class HdlCholesterol_Value:
    quantity: Quantity


@dataclass
class HdlCholesterol_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    low: SimpleQuantity
    text: String


@dataclass
class HdlCholesterol_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: HdlCholesterol_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: HdlCholesterol_ReferenceRange


@dataclass
class HdlCholesterol_Component_Value:
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
class Headcircum:
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
    code: Headcircum_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Headcircum_Effective
    issued: Instant
    performer: Reference
    value: Headcircum_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Headcircum_ReferenceRange
    related: Headcircum_Related
    component: Headcircum_Component


@dataclass
class Headcircum_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    head_circum_code: CodingWithFixedCode


@dataclass
class Headcircum_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Headcircum_Value:
    quantity: Quantity


@dataclass
class Headcircum_ReferenceRange:
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
class Headcircum_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Headcircum_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Headcircum_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Headcircum_ReferenceRange


@dataclass
class Headcircum_Component_Value:
    quantity: Quantity


@dataclass
class Heartrate:
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
    code: Heartrate_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Heartrate_Effective
    issued: Instant
    performer: Reference
    value: Heartrate_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Heartrate_ReferenceRange
    related: Heartrate_Related
    component: Heartrate_Component


@dataclass
class Heartrate_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    heart_rate_code: CodingWithFixedCode


@dataclass
class Heartrate_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Heartrate_Value:
    quantity: Quantity


@dataclass
class Heartrate_ReferenceRange:
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
class Heartrate_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Heartrate_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Heartrate_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Heartrate_ReferenceRange


@dataclass
class Heartrate_Component_Value:
    quantity: Quantity


@dataclass
class Hlaresult:
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
    effective: Hlaresult_Effective
    issued: Instant
    performer: Hlaresult_Performer
    specimen: Reference
    result: Reference
    imaging_study: Reference
    image: Hlaresult_Image
    conclusion: String
    coded_diagnosis: CodeableConcept
    presented_form: Attachment
    allele_database: CodeableConcept
    glstring: DiagnosticReportGlstring
    haploid: DiagnosticReportHaploid
    method: CodeableConcept


@dataclass
class Hlaresult_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Hlaresult_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class Hlaresult_Image:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference


@dataclass
class LdlCholesterol:
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
    effective: LdlCholesterol_Effective
    issued: Instant
    performer: Reference
    value: LdlCholesterol_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: LdlCholesterol_ReferenceRange
    component: LdlCholesterol_Component


@dataclass
class LdlCholesterol_Effective:
    date_time: DateTime
    period: Period


@dataclass
class LdlCholesterol_Value:
    quantity: Quantity


@dataclass
class LdlCholesterol_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    high: SimpleQuantity
    text: String


@dataclass
class LdlCholesterol_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: LdlCholesterol_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: LdlCholesterol_ReferenceRange


@dataclass
class LdlCholesterol_Component_Value:
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
class LipidProfile:
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
    effective: LipidProfile_Effective
    issued: Instant
    performer: LipidProfile_Performer
    specimen: Reference
    result: Reference
    imaging_study: Reference
    image: LipidProfile_Image
    conclusion: String
    presented_form: Attachment


@dataclass
class LipidProfile_Effective:
    date_time: DateTime
    period: Period


@dataclass
class LipidProfile_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class LipidProfile_Image:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference


@dataclass
class MetadataResource:
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
    use_context: UsageContext
    jurisdiction: CodeableConcept
    description: Markdown


@dataclass
class ObservationGenetics:
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
    effective: ObservationGenetics_Effective
    issued: Instant
    performer: Reference
    value: ObservationGenetics_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: ObservationGenetics_ReferenceRange
    related: ObservationGenetics_Related
    component: ObservationGenetics_Component
    dna_sequence_variant_name: CodeableConcept
    dna_variant_id: CodeableConcept
    dna_sequence_variant_type: CodeableConcept
    amino_acid_change_name: CodeableConcept
    amino_acid_change_type: CodeableConcept
    gene_symbol: CodeableConcept
    dna_region_name: String
    allele_name: CodeableConcept
    allelic_state: CodeableConcept
    allelic_frequency: Decimal
    copy_number_event: CodeableConcept
    genomic_source_class: CodeableConcept
    phase_set: Uri
    sequence: Reference
    interpretation_slice: Reference


@dataclass
class ObservationGenetics_Effective:
    date_time: DateTime
    period: Period


@dataclass
class ObservationGenetics_Value:
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
class ObservationGenetics_ReferenceRange:
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
class ObservationGenetics_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class ObservationGenetics_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: ObservationGenetics_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: ObservationGenetics_ReferenceRange


@dataclass
class ObservationGenetics_Component_Value:
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
class Oxygensat:
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
    code: Oxygensat_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Oxygensat_Effective
    issued: Instant
    performer: Reference
    value: Oxygensat_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Oxygensat_ReferenceRange
    related: Oxygensat_Related
    component: Oxygensat_Component


@dataclass
class Oxygensat_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    oxygen_sat_code: CodingWithFixedCode


@dataclass
class Oxygensat_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Oxygensat_Value:
    quantity: Quantity


@dataclass
class Oxygensat_ReferenceRange:
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
class Oxygensat_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Oxygensat_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Oxygensat_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Oxygensat_ReferenceRange


@dataclass
class Oxygensat_Component_Value:
    quantity: Quantity


@dataclass
class ProcedurerequestGenetics:
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
    occurrence: ProcedurerequestGenetics_Occurrence
    as_needed: ProcedurerequestGenetics_AsNeeded
    authored_on: DateTime
    requester: ProcedurerequestGenetics_Requester
    performer_type: CodeableConcept
    performer: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    supporting_info: Reference
    specimen: Reference
    body_site: CodeableConcept
    note: Annotation
    relevant_history: Reference
    item: DiagnosticReportItem


@dataclass
class ProcedurerequestGenetics_Occurrence:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class ProcedurerequestGenetics_AsNeeded:
    boolean: Boolean
    codeable_concept: CodeableConcept


@dataclass
class ProcedurerequestGenetics_Requester:
    id: String
    extension: Extension
    modifier_extension: Extension
    agent: Reference
    on_behalf_of: Reference


@dataclass
class Resprate:
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
    code: Resprate_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Resprate_Effective
    issued: Instant
    performer: Reference
    value: Resprate_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Resprate_ReferenceRange
    related: Resprate_Related
    component: Resprate_Component


@dataclass
class Resprate_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    resp_rate_code: CodingWithFixedCode


@dataclass
class Resprate_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Resprate_Value:
    quantity: Quantity


@dataclass
class Resprate_ReferenceRange:
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
class Resprate_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Resprate_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Resprate_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Resprate_ReferenceRange


@dataclass
class Resprate_Component_Value:
    quantity: Quantity


@dataclass
class Shareablecodesystem:
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
    filter: Shareablecodesystem_Filter
    property: Shareablecodesystem_Property
    concept: Shareablecodesystem_ConceptDefinition


@dataclass
class Shareablecodesystem_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    description: String
    operator: FilterOperatorCode
    value: String


@dataclass
class Shareablecodesystem_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    uri: Uri
    description: String
    type: PropertyTypeCode


@dataclass
class Shareablecodesystem_ConceptDefinition:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    definition: String
    designation: Shareablecodesystem_ConceptDefinition_Designation
    property: Shareablecodesystem_ConceptDefinition_ConceptProperty
    concept: Shareablecodesystem_ConceptDefinition


@dataclass
class Shareablecodesystem_ConceptDefinition_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: LanguageCode
    use: Coding
    value: String


@dataclass
class Shareablecodesystem_ConceptDefinition_ConceptProperty:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    value: Shareablecodesystem_ConceptDefinition_ConceptProperty_Value


@dataclass
class Shareablecodesystem_ConceptDefinition_ConceptProperty_Value:
    code: Code
    coding: Coding
    string_value: String
    integer: Integer
    boolean: Boolean
    date_time: DateTime


@dataclass
class Shareablevalueset:
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
    compose: Shareablevalueset_Compose
    expansion: Shareablevalueset_Expansion


@dataclass
class Shareablevalueset_Compose:
    id: String
    extension: Extension
    modifier_extension: Extension
    locked_date: Date
    inactive: Boolean
    include: Shareablevalueset_Compose_ConceptSet
    exclude: Shareablevalueset_Compose_ConceptSet


@dataclass
class Shareablevalueset_Compose_ConceptSet:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    version: String
    concept: Shareablevalueset_Compose_ConceptSet_ConceptReference
    filter: Shareablevalueset_Compose_ConceptSet_Filter
    value_set: Uri


@dataclass
class Shareablevalueset_Compose_ConceptSet_ConceptReference:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    display: String
    designation: Shareablevalueset_Compose_ConceptSet_ConceptReference_Designation


@dataclass
class Shareablevalueset_Compose_ConceptSet_ConceptReference_Designation:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: LanguageCode
    use: Coding
    value: String


@dataclass
class Shareablevalueset_Compose_ConceptSet_Filter:
    id: String
    extension: Extension
    modifier_extension: Extension
    property: Code
    op: FilterOperatorCode
    value: Code


@dataclass
class Shareablevalueset_Expansion:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Uri
    timestamp: DateTime
    total: Integer
    offset: Integer
    parameter: Shareablevalueset_Expansion_Parameter
    contains: Shareablevalueset_Expansion_Contains


@dataclass
class Shareablevalueset_Expansion_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    value: Shareablevalueset_Expansion_Parameter_Value


@dataclass
class Shareablevalueset_Expansion_Parameter_Value:
    string_value: String
    boolean: Boolean
    integer: Integer
    decimal: Decimal
    uri: Uri
    code: Code


@dataclass
class Shareablevalueset_Expansion_Contains:
    id: String
    extension: Extension
    modifier_extension: Extension
    system: Uri
    abstract: Boolean
    inactive: Boolean
    version: String
    code: Code
    display: String
    designation: Shareablevalueset_Compose_ConceptSet_ConceptReference_Designation
    contains: Shareablevalueset_Expansion_Contains


@dataclass
class Triglyceride:
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
    effective: Triglyceride_Effective
    issued: Instant
    performer: Reference
    value: Triglyceride_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Triglyceride_ReferenceRange
    component: Triglyceride_Component


@dataclass
class Triglyceride_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Triglyceride_Value:
    quantity: Quantity


@dataclass
class Triglyceride_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    high: SimpleQuantity
    text: String


@dataclass
class Triglyceride_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Triglyceride_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Triglyceride_ReferenceRange


@dataclass
class Triglyceride_Component_Value:
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
class Vitalsigns:
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
    effective: Vitalsigns_Effective
    issued: Instant
    performer: Reference
    value: Vitalsigns_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Vitalsigns_ReferenceRange
    related: Vitalsigns_Related
    component: Vitalsigns_Component


@dataclass
class Vitalsigns_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Vitalsigns_Value:
    quantity: Quantity


@dataclass
class Vitalsigns_ReferenceRange:
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
class Vitalsigns_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Vitalsigns_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Vitalsigns_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Vitalsigns_ReferenceRange


@dataclass
class Vitalsigns_Component_Value:
    quantity: Quantity


@dataclass
class Vitalspanel:
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
    code: Vitalspanel_CodeableConceptForCode
    subject: Reference
    context: Reference
    effective: Vitalspanel_Effective
    issued: Instant
    performer: Reference
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    comment: String
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Vitalspanel_ReferenceRange
    related: Vitalspanel_Related
    component: Vitalspanel_Component


@dataclass
class Vitalspanel_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    body_weight_code: CodingWithFixedCode


@dataclass
class Vitalspanel_Effective:
    date_time: DateTime
    period: Period


@dataclass
class Vitalspanel_ReferenceRange:
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
class Vitalspanel_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ObservationRelationshipTypeCode
    target: Reference


@dataclass
class Vitalspanel_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Vitalspanel_Component_Value
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Vitalspanel_ReferenceRange


@dataclass
class Vitalspanel_Component_Value:
    quantity: Quantity

