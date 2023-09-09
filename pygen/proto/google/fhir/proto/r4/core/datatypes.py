# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Address:
    id: String
    extension: Extension
    use: Address_UseCode
    type: Address_TypeCode
    text: String
    line: String
    city: String
    district: String
    state: String
    postal_code: String
    country: String
    period: Period


@dataclass
class Address_UseCode:
    value: AddressUseCode_Value
    id: String
    extension: Extension


@dataclass
class Address_TypeCode:
    value: AddressTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Age:
    id: String
    extension: Extension
    value: Decimal
    comparator: Age_ComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Age_ComparatorCode:
    value: QuantityComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class Annotation:
    id: String
    extension: Extension
    author: Annotation_AuthorX
    time: DateTime
    text: Markdown


@dataclass
class Annotation_AuthorX:
    reference: Reference
    string_value: String


@dataclass
class Attachment:
    id: String
    extension: Extension
    content_type: Attachment_ContentTypeCode
    language: Code
    data: Base64Binary
    url: Url
    size: UnsignedInt
    hash: Base64Binary
    title: String
    creation: DateTime


@dataclass
class Attachment_ContentTypeCode:
    id: String
    extension: Extension
    value: str


@dataclass
class BackboneElement:
    id: String
    extension: Extension
    modifier_extension: Extension


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
class Canonical:
    value: str
    id: String
    extension: Extension


@dataclass
class Code:
    value: str
    id: String
    extension: Extension


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
class ContactDetail:
    id: String
    extension: Extension
    name: String
    telecom: ContactPoint


@dataclass
class ContactPoint:
    id: String
    extension: Extension
    system: ContactPoint_SystemCode
    value: String
    use: ContactPoint_UseCode
    rank: PositiveInt
    period: Period


@dataclass
class ContactPoint_SystemCode:
    value: ContactPointSystemCode_Value
    id: String
    extension: Extension


@dataclass
class ContactPoint_UseCode:
    value: ContactPointUseCode_Value
    id: String
    extension: Extension


@dataclass
class Contributor:
    id: String
    extension: Extension
    type: Contributor_TypeCode
    name: String
    contact: ContactDetail


@dataclass
class Contributor_TypeCode:
    value: ContributorTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Count:
    id: String
    extension: Extension
    value: Decimal
    comparator: Count_ComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Count_ComparatorCode:
    value: QuantityComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class DataRequirement:
    id: String
    extension: Extension
    type: DataRequirement_TypeCode
    profile: Canonical
    subject: DataRequirement_SubjectX
    must_support: String
    code_filter: DataRequirement_CodeFilter
    date_filter: DataRequirement_DateFilter
    limit: PositiveInt
    sort: DataRequirement_Sort


@dataclass
class DataRequirement_TypeCode:
    value: FHIRAllTypesValueSet_Value
    id: String
    extension: Extension


@dataclass
class DataRequirement_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class DataRequirement_CodeFilter:
    id: String
    extension: Extension
    path: String
    search_param: String
    value_set: Canonical
    code: Coding


@dataclass
class DataRequirement_DateFilter:
    id: String
    extension: Extension
    path: String
    search_param: String
    value: DataRequirement_DateFilter_ValueX


@dataclass
class DataRequirement_DateFilter_ValueX:
    date_time: DateTime
    period: Period
    duration: Duration


@dataclass
class DataRequirement_Sort:
    id: String
    extension: Extension
    path: String
    direction: DataRequirement_Sort_DirectionCode


@dataclass
class DataRequirement_Sort_DirectionCode:
    value: SortDirectionCode_Value
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
class Distance:
    id: String
    extension: Extension
    value: Decimal
    comparator: Distance_ComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Distance_ComparatorCode:
    value: QuantityComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class Dosage:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: Integer
    text: String
    additional_instruction: CodeableConcept
    patient_instruction: String
    timing: Timing
    as_needed: Dosage_AsNeededX
    site: CodeableConcept
    route: CodeableConcept
    method: CodeableConcept
    dose_and_rate: Dosage_DoseAndRate
    max_dose_per_period: Ratio
    max_dose_per_administration: SimpleQuantity
    max_dose_per_lifetime: SimpleQuantity


@dataclass
class Dosage_AsNeededX:
    boolean: Boolean
    codeable_concept: CodeableConcept


@dataclass
class Dosage_DoseAndRate:
    id: String
    extension: Extension
    type: CodeableConcept
    dose: Dosage_DoseAndRate_DoseX
    rate: Dosage_DoseAndRate_RateX


@dataclass
class Dosage_DoseAndRate_DoseX:
    range: Range
    quantity: SimpleQuantity


@dataclass
class Dosage_DoseAndRate_RateX:
    ratio: Ratio
    range: Range
    quantity: SimpleQuantity


@dataclass
class Duration:
    id: String
    extension: Extension
    value: Decimal
    comparator: Duration_ComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Duration_ComparatorCode:
    value: QuantityComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    representation: ElementDefinition_RepresentationCode
    slice_name: String
    slice_is_constraining: Boolean
    label: String
    code: Coding
    slicing: ElementDefinition_Slicing
    short: String
    definition: Markdown
    comment: Markdown
    requirements: Markdown
    alias: String
    min: UnsignedInt
    max: String
    base: ElementDefinition_Base
    content_reference: Uri
    type: ElementDefinition_TypeRef
    default_value: ElementDefinition_DefaultValueX
    meaning_when_missing: Markdown
    order_meaning: String
    fixed: ElementDefinition_FixedX
    pattern: ElementDefinition_PatternX
    example: ElementDefinition_Example
    min_value: ElementDefinition_MinValueX
    max_value: ElementDefinition_MaxValueX
    max_length: Integer
    condition: Id
    constraint: ElementDefinition_Constraint
    must_support: Boolean
    is_modifier: Boolean
    is_modifier_reason: String
    is_summary: Boolean
    binding: ElementDefinition_ElementDefinitionBinding
    mapping: ElementDefinition_Mapping


@dataclass
class ElementDefinition_RepresentationCode:
    value: PropertyRepresentationCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition_Slicing:
    id: String
    extension: Extension
    discriminator: ElementDefinition_Slicing_Discriminator
    description: String
    ordered: Boolean
    rules: ElementDefinition_Slicing_RulesCode


@dataclass
class ElementDefinition_Slicing_Discriminator:
    id: String
    extension: Extension
    type: ElementDefinition_Slicing_Discriminator_TypeCode
    path: String


@dataclass
class ElementDefinition_Slicing_Discriminator_TypeCode:
    value: DiscriminatorTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition_Slicing_RulesCode:
    value: SlicingRulesCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition_Base:
    id: String
    extension: Extension
    path: String
    min: UnsignedInt
    max: String


@dataclass
class ElementDefinition_TypeRef:
    id: String
    extension: Extension
    code: Uri
    profile: Canonical
    target_profile: Canonical
    aggregation: ElementDefinition_TypeRef_AggregationCode
    versioning: ElementDefinition_TypeRef_VersioningCode


@dataclass
class ElementDefinition_TypeRef_AggregationCode:
    value: AggregationModeCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition_TypeRef_VersioningCode:
    value: ReferenceVersionRulesCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition_DefaultValueX:
    base64_binary: Base64Binary
    boolean: Boolean
    canonical: Canonical
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
    url: Url
    uuid: Uuid
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
    contact_detail: ContactDetail
    contributor: Contributor
    data_requirement: DataRequirement
    expression: Expression
    parameter_definition: ParameterDefinition
    related_artifact: RelatedArtifact
    trigger_definition: TriggerDefinition
    usage_context: UsageContext
    dosage: Dosage
    meta: Meta


@dataclass
class ElementDefinition_FixedX:
    base64_binary: Base64Binary
    boolean: Boolean
    canonical: Canonical
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
    url: Url
    uuid: Uuid
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
    contact_detail: ContactDetail
    contributor: Contributor
    data_requirement: DataRequirement
    expression: Expression
    parameter_definition: ParameterDefinition
    related_artifact: RelatedArtifact
    trigger_definition: TriggerDefinition
    usage_context: UsageContext
    dosage: Dosage
    meta: Meta


@dataclass
class ElementDefinition_PatternX:
    base64_binary: Base64Binary
    boolean: Boolean
    canonical: Canonical
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
    url: Url
    uuid: Uuid
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
    contact_detail: ContactDetail
    contributor: Contributor
    data_requirement: DataRequirement
    expression: Expression
    parameter_definition: ParameterDefinition
    related_artifact: RelatedArtifact
    trigger_definition: TriggerDefinition
    usage_context: UsageContext
    dosage: Dosage
    meta: Meta


@dataclass
class ElementDefinition_Example:
    id: String
    extension: Extension
    label: String
    value: ElementDefinition_Example_ValueX


@dataclass
class ElementDefinition_Example_ValueX:
    base64_binary: Base64Binary
    boolean: Boolean
    canonical: Canonical
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
    url: Url
    uuid: Uuid
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
    contact_detail: ContactDetail
    contributor: Contributor
    data_requirement: DataRequirement
    expression: Expression
    parameter_definition: ParameterDefinition
    related_artifact: RelatedArtifact
    trigger_definition: TriggerDefinition
    usage_context: UsageContext
    dosage: Dosage
    meta: Meta


@dataclass
class ElementDefinition_MinValueX:
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
class ElementDefinition_MaxValueX:
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
class ElementDefinition_Constraint:
    id: String
    extension: Extension
    key: Id
    requirements: String
    severity: ElementDefinition_Constraint_SeverityCode
    human: String
    expression: String
    xpath: String
    source: Canonical


@dataclass
class ElementDefinition_Constraint_SeverityCode:
    value: ConstraintSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition_ElementDefinitionBinding:
    id: String
    extension: Extension
    strength: ElementDefinition_ElementDefinitionBinding_StrengthCode
    description: String
    value_set: Canonical


@dataclass
class ElementDefinition_ElementDefinitionBinding_StrengthCode:
    value: BindingStrengthCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinition_Mapping:
    id: String
    extension: Extension
    identity: Id
    language: ElementDefinition_Mapping_LanguageCode
    map: String
    comment: String


@dataclass
class ElementDefinition_Mapping_LanguageCode:
    id: String
    extension: Extension
    value: str


@dataclass
class Expression:
    id: String
    extension: Extension
    description: String
    name: Id
    language: Code
    expression: String
    reference: Uri


@dataclass
class HumanName:
    id: String
    extension: Extension
    use: HumanName_UseCode
    text: String
    family: String
    given: String
    prefix: String
    suffix: String
    period: Period


@dataclass
class HumanName_UseCode:
    value: NameUseCode_Value
    id: String
    extension: Extension


@dataclass
class Id:
    value: str
    id: String
    extension: Extension


@dataclass
class Identifier:
    id: String
    extension: Extension
    use: Identifier_UseCode
    type: CodeableConcept
    system: Uri
    value: String
    period: Period
    assigner: Reference


@dataclass
class Identifier_UseCode:
    value: IdentifierUseCode_Value
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
class MarketingStatus:
    id: String
    extension: Extension
    modifier_extension: Extension
    country: CodeableConcept
    jurisdiction: CodeableConcept
    status: CodeableConcept
    date_range: Period
    restore_date: DateTime


@dataclass
class Meta:
    id: String
    extension: Extension
    version_id: Id
    last_updated: Instant
    source: Uri
    profile: Canonical
    security: Coding
    tag: Coding


@dataclass
class Money:
    id: String
    extension: Extension
    value: Decimal
    currency: Money_CurrencyCode


@dataclass
class Money_CurrencyCode:
    id: String
    extension: Extension
    value: str


@dataclass
class MoneyQuantity:
    id: String
    extension: Extension
    value: Decimal
    comparator: MoneyQuantity_ComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class MoneyQuantity_ComparatorCode:
    value: QuantityComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class Narrative:
    id: String
    extension: Extension
    status: Narrative_StatusCode
    div: Xhtml


@dataclass
class Narrative_StatusCode:
    value: NarrativeStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Oid:
    value: str
    id: String
    extension: Extension


@dataclass
class ParameterDefinition:
    id: String
    extension: Extension
    name: Code
    use: ParameterDefinition_UseCode
    min: Integer
    max: String
    documentation: String
    type: ParameterDefinition_TypeCode
    profile: Canonical


@dataclass
class ParameterDefinition_UseCode:
    value: OperationParameterUseCode_Value
    id: String
    extension: Extension


@dataclass
class ParameterDefinition_TypeCode:
    value: FHIRAllTypesValueSet_Value
    id: String
    extension: Extension


@dataclass
class Period:
    id: String
    extension: Extension
    start: DateTime
    end: DateTime


@dataclass
class Population:
    id: String
    extension: Extension
    modifier_extension: Extension
    age: Population_AgeX
    gender: CodeableConcept
    race: CodeableConcept
    physiological_condition: CodeableConcept


@dataclass
class Population_AgeX:
    range: Range
    codeable_concept: CodeableConcept


@dataclass
class PositiveInt:
    value: uint32
    id: String
    extension: Extension


@dataclass
class ProdCharacteristic:
    id: String
    extension: Extension
    modifier_extension: Extension
    height: Quantity
    width: Quantity
    depth: Quantity
    weight: Quantity
    nominal_volume: Quantity
    external_diameter: Quantity
    shape: String
    color: String
    imprint: String
    image: Attachment
    scoring: CodeableConcept


@dataclass
class ProductShelfLife:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    period: Quantity
    special_precautions_for_storage: CodeableConcept


@dataclass
class Quantity:
    id: String
    extension: Extension
    value: Decimal
    comparator: Quantity_ComparatorCode
    unit: String
    system: Uri
    code: Code


@dataclass
class Quantity_ComparatorCode:
    value: QuantityComparatorCode_Value
    id: String
    extension: Extension


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
class RelatedArtifact:
    id: String
    extension: Extension
    type: RelatedArtifact_TypeCode
    label: String
    display: String
    citation: Markdown
    url: Url
    document: Attachment
    resource: Canonical


@dataclass
class RelatedArtifact_TypeCode:
    value: RelatedArtifactTypeCode_Value
    id: String
    extension: Extension


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
    who: Reference
    on_behalf_of: Reference
    target_format: Signature_TargetFormatCode
    sig_format: Signature_SigFormatCode
    data: Base64Binary


@dataclass
class Signature_TargetFormatCode:
    id: String
    extension: Extension
    value: str


@dataclass
class Signature_SigFormatCode:
    id: String
    extension: Extension
    value: str


@dataclass
class SimpleQuantity:
    id: String
    extension: Extension
    value: Decimal
    unit: String
    system: Uri
    code: Code


@dataclass
class String:
    value: str
    id: String
    extension: Extension


@dataclass
class SubstanceAmount:
    id: String
    extension: Extension
    modifier_extension: Extension
    amount: SubstanceAmount_AmountX
    amount_type: CodeableConcept
    amount_text: String
    reference_range: SubstanceAmount_ReferenceRange


@dataclass
class SubstanceAmount_AmountX:
    quantity: Quantity
    range: Range
    string_value: String


@dataclass
class SubstanceAmount_ReferenceRange:
    id: String
    extension: Extension
    low_limit: Quantity
    high_limit: Quantity


@dataclass
class Time:
    value_us: int64
    precision: Time_Precision
    id: String
    extension: Extension


@dataclass
class Timing:
    id: String
    extension: Extension
    modifier_extension: Extension
    event: DateTime
    repeat: Timing_Repeat
    code: CodeableConcept


@dataclass
class Timing_Repeat:
    id: String
    extension: Extension
    bounds: Timing_Repeat_BoundsX
    count: PositiveInt
    count_max: PositiveInt
    duration: Decimal
    duration_max: Decimal
    duration_unit: Timing_Repeat_DurationUnitCode
    frequency: PositiveInt
    frequency_max: PositiveInt
    period: Decimal
    period_max: Decimal
    period_unit: Timing_Repeat_PeriodUnitCode
    day_of_week: Timing_Repeat_DayOfWeekCode
    time_of_day: Time
    when: Timing_Repeat_WhenCode
    offset: UnsignedInt


@dataclass
class Timing_Repeat_BoundsX:
    duration: Duration
    range: Range
    period: Period


@dataclass
class Timing_Repeat_DurationUnitCode:
    value: UnitsOfTimeValueSet_Value
    id: String
    extension: Extension


@dataclass
class Timing_Repeat_PeriodUnitCode:
    value: UnitsOfTimeValueSet_Value
    id: String
    extension: Extension


@dataclass
class Timing_Repeat_DayOfWeekCode:
    value: DaysOfWeekCode_Value
    id: String
    extension: Extension


@dataclass
class Timing_Repeat_WhenCode:
    value: EventTimingValueSet_Value
    id: String
    extension: Extension


@dataclass
class TriggerDefinition:
    id: String
    extension: Extension
    type: TriggerDefinition_TypeCode
    name: String
    timing: TriggerDefinition_TimingX
    data: DataRequirement
    condition: Expression


@dataclass
class TriggerDefinition_TypeCode:
    value: TriggerTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TriggerDefinition_TimingX:
    timing: Timing
    reference: Reference
    date: Date
    date_time: DateTime


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
class Url:
    value: str
    id: String
    extension: Extension


@dataclass
class UsageContext:
    id: String
    extension: Extension
    code: Coding
    value: UsageContext_ValueX


@dataclass
class UsageContext_ValueX:
    codeable_concept: CodeableConcept
    quantity: Quantity
    range: Range
    reference: Reference


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
class Element:
    id: String
    extension: Extension


@dataclass
class Extension:
    id: String
    url: Uri
    extension: Extension
    value: Extension_ValueX


@dataclass
class Extension_ValueX:
    base64_binary: Base64Binary
    boolean: Boolean
    canonical: Canonical
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
    url: Url
    uuid: Uuid
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
    contact_detail: ContactDetail
    contributor: Contributor
    data_requirement: DataRequirement
    expression: Expression
    parameter_definition: ParameterDefinition
    related_artifact: RelatedArtifact
    trigger_definition: TriggerDefinition
    usage_context: UsageContext
    dosage: Dosage


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
    type: Uri
    uri: String
    fragment: String
    resource_id: ReferenceId
    account_id: ReferenceId
    activity_definition_id: ReferenceId
    adverse_event_id: ReferenceId
    allergy_intolerance_id: ReferenceId
    appointment_id: ReferenceId
    appointment_response_id: ReferenceId
    audit_event_id: ReferenceId
    basic_id: ReferenceId
    binary_id: ReferenceId
    biologically_derived_product_id: ReferenceId
    body_structure_id: ReferenceId
    bundle_id: ReferenceId
    capability_statement_id: ReferenceId
    care_plan_id: ReferenceId
    care_team_id: ReferenceId
    catalog_entry_id: ReferenceId
    charge_item_id: ReferenceId
    charge_item_definition_id: ReferenceId
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
    coverage_eligibility_request_id: ReferenceId
    coverage_eligibility_response_id: ReferenceId
    detected_issue_id: ReferenceId
    device_id: ReferenceId
    device_definition_id: ReferenceId
    device_metric_id: ReferenceId
    device_request_id: ReferenceId
    device_use_statement_id: ReferenceId
    diagnostic_report_id: ReferenceId
    document_manifest_id: ReferenceId
    document_reference_id: ReferenceId
    domain_resource_id: ReferenceId
    effect_evidence_synthesis_id: ReferenceId
    encounter_id: ReferenceId
    endpoint_id: ReferenceId
    enrollment_request_id: ReferenceId
    enrollment_response_id: ReferenceId
    episode_of_care_id: ReferenceId
    event_definition_id: ReferenceId
    evidence_id: ReferenceId
    evidence_variable_id: ReferenceId
    example_scenario_id: ReferenceId
    explanation_of_benefit_id: ReferenceId
    family_member_history_id: ReferenceId
    flag_id: ReferenceId
    goal_id: ReferenceId
    graph_definition_id: ReferenceId
    group_id: ReferenceId
    guidance_response_id: ReferenceId
    healthcare_service_id: ReferenceId
    imaging_study_id: ReferenceId
    immunization_id: ReferenceId
    immunization_evaluation_id: ReferenceId
    immunization_recommendation_id: ReferenceId
    implementation_guide_id: ReferenceId
    insurance_plan_id: ReferenceId
    invoice_id: ReferenceId
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
    medication_knowledge_id: ReferenceId
    medication_request_id: ReferenceId
    medication_statement_id: ReferenceId
    medicinal_product_id: ReferenceId
    medicinal_product_authorization_id: ReferenceId
    medicinal_product_contraindication_id: ReferenceId
    medicinal_product_indication_id: ReferenceId
    medicinal_product_ingredient_id: ReferenceId
    medicinal_product_interaction_id: ReferenceId
    medicinal_product_manufactured_id: ReferenceId
    medicinal_product_packaged_id: ReferenceId
    medicinal_product_pharmaceutical_id: ReferenceId
    medicinal_product_undesirable_effect_id: ReferenceId
    message_definition_id: ReferenceId
    message_header_id: ReferenceId
    molecular_sequence_id: ReferenceId
    naming_system_id: ReferenceId
    nutrition_order_id: ReferenceId
    observation_id: ReferenceId
    observation_definition_id: ReferenceId
    operation_definition_id: ReferenceId
    operation_outcome_id: ReferenceId
    organization_id: ReferenceId
    organization_affiliation_id: ReferenceId
    parameters_id: ReferenceId
    patient_id: ReferenceId
    payment_notice_id: ReferenceId
    payment_reconciliation_id: ReferenceId
    person_id: ReferenceId
    plan_definition_id: ReferenceId
    practitioner_id: ReferenceId
    practitioner_role_id: ReferenceId
    procedure_id: ReferenceId
    provenance_id: ReferenceId
    questionnaire_id: ReferenceId
    questionnaire_response_id: ReferenceId
    related_person_id: ReferenceId
    request_group_id: ReferenceId
    research_definition_id: ReferenceId
    research_element_definition_id: ReferenceId
    research_study_id: ReferenceId
    research_subject_id: ReferenceId
    risk_assessment_id: ReferenceId
    risk_evidence_synthesis_id: ReferenceId
    schedule_id: ReferenceId
    search_parameter_id: ReferenceId
    service_request_id: ReferenceId
    slot_id: ReferenceId
    specimen_id: ReferenceId
    specimen_definition_id: ReferenceId
    structure_definition_id: ReferenceId
    structure_map_id: ReferenceId
    subscription_id: ReferenceId
    substance_id: ReferenceId
    substance_nucleic_acid_id: ReferenceId
    substance_polymer_id: ReferenceId
    substance_protein_id: ReferenceId
    substance_reference_information_id: ReferenceId
    substance_source_material_id: ReferenceId
    substance_specification_id: ReferenceId
    supply_delivery_id: ReferenceId
    supply_request_id: ReferenceId
    task_id: ReferenceId
    terminology_capabilities_id: ReferenceId
    test_report_id: ReferenceId
    test_script_id: ReferenceId
    value_set_id: ReferenceId
    verification_result_id: ReferenceId
    vision_prescription_id: ReferenceId
    metadata_resource_id: ReferenceId
    identifier: Identifier
    display: String


@dataclass
class ReferenceId:
    value: str
    history: Id
    id: String
    extension: Extension

