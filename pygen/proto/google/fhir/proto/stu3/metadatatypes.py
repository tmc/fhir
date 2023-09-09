# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class BackboneElement:
    id: String
    extension: Extension
    modifier_extension: Extension


@dataclass
class ContactDetail:
    id: String
    extension: Extension
    name: String
    telecom: ContactPoint


@dataclass
class Contributor:
    id: String
    extension: Extension
    type: ContributorTypeCode
    name: String
    contact: ContactDetail


@dataclass
class DataRequirement:
    id: String
    extension: Extension
    type: FHIRAllTypesCode
    profile: Uri
    must_support: String
    code_filter: DataRequirement_CodeFilter
    date_filter: DataRequirement_DateFilter


@dataclass
class DataRequirement_CodeFilter:
    id: String
    extension: Extension
    path: String
    value_set: DataRequirement_CodeFilter_ValueSet
    value_code: Code
    value_coding: Coding
    value_codeable_concept: CodeableConcept


@dataclass
class DataRequirement_CodeFilter_ValueSet:
    string_value: String
    reference: Reference


@dataclass
class DataRequirement_DateFilter:
    id: String
    extension: Extension
    path: String
    value: DataRequirement_DateFilter_Value


@dataclass
class DataRequirement_DateFilter_Value:
    date_time: DateTime
    period: Period
    duration: Duration


@dataclass
class Element:
    id: String
    extension: Extension


@dataclass
class ElementDefinition:
    id: String
    extension: Extension
    path: String
    representation: PropertyRepresentationCode
    slice_name: String
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
    default_value: ElementDefinition_DefaultValue
    meaning_when_missing: Markdown
    order_meaning: String
    fixed: ElementDefinition_Fixed
    pattern: ElementDefinition_Pattern
    example: ElementDefinition_Example
    min_value: ElementDefinition_MinValue
    max_value: ElementDefinition_MaxValue
    max_length: Integer
    condition: Id
    constraint: ElementDefinition_Constraint
    must_support: Boolean
    is_modifier: Boolean
    is_summary: Boolean
    binding: ElementDefinition_ElementDefinitionBinding
    mapping: ElementDefinition_Mapping


@dataclass
class ElementDefinition_Slicing:
    id: String
    extension: Extension
    discriminator: ElementDefinition_Slicing_Discriminator
    description: String
    ordered: Boolean
    rules: SlicingRulesCode


@dataclass
class ElementDefinition_Slicing_Discriminator:
    id: String
    extension: Extension
    type: DiscriminatorTypeCode
    path: String


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
    profile: Uri
    target_profile: Uri
    aggregation: AggregationModeCode
    versioning: ReferenceVersionRulesCode


@dataclass
class ElementDefinition_DefaultValue:
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
class ElementDefinition_Fixed:
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
class ElementDefinition_Pattern:
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
class ElementDefinition_Example:
    id: String
    extension: Extension
    label: String
    value: ElementDefinition_Example_Value


@dataclass
class ElementDefinition_Example_Value:
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
class ElementDefinition_MinValue:
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
class ElementDefinition_MaxValue:
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
    severity: ConstraintSeverityCode
    human: String
    expression: String
    xpath: String
    source: Uri


@dataclass
class ElementDefinition_ElementDefinitionBinding:
    id: String
    extension: Extension
    strength: BindingStrengthCode
    description: String
    value_set: ElementDefinition_ElementDefinitionBinding_ValueSet


@dataclass
class ElementDefinition_ElementDefinitionBinding_ValueSet:
    uri: Uri
    reference: Reference


@dataclass
class ElementDefinition_Mapping:
    id: String
    extension: Extension
    identity: Id
    language: MimeTypeCode
    map: String
    comment: String


@dataclass
class Narrative:
    id: String
    extension: Extension
    status: NarrativeStatusCode
    div: Xhtml


@dataclass
class ParameterDefinition:
    id: String
    extension: Extension
    name: Code
    use: OperationParameterUseCode
    min: Integer
    max: String
    documentation: String
    type: FHIRAllTypesCode
    profile: Reference


@dataclass
class RelatedArtifact:
    id: String
    extension: Extension
    type: RelatedArtifactTypeCode
    display: String
    citation: String
    url: Uri
    document: Attachment
    resource: Reference


@dataclass
class TriggerDefinition:
    id: String
    extension: Extension
    type: TriggerTypeCode
    event_name: String
    event_timing: TriggerDefinition_EventTiming
    event_data: DataRequirement


@dataclass
class TriggerDefinition_EventTiming:
    timing: Timing
    reference: Reference
    date: Date
    date_time: DateTime


@dataclass
class UsageContext:
    id: String
    extension: Extension
    code: Coding
    value: UsageContext_Value


@dataclass
class UsageContext_Value:
    codeable_concept: CodeableConcept
    quantity: Quantity
    range: Range

